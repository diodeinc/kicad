#!/usr/bin/env uv run
# /// script
# dependencies = ["anthropic", "openai", "google-generativeai", "tabulate"]
# ///
"""
Benchmark different LLM providers for generating reference designs.

This script tests various models on a subset of components and measures:
- Success rate (designs that compile)
- Time per design
- API cost estimation
- Quality metrics
"""

import os
import sys
import time
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
from tabulate import tabulate

# Import the reference design generator
sys.path.insert(0, str(Path(__file__).parent))
from scripts.ai_reference_design import (
    ReferenceDesignGenerator,
    create_llm_provider,
    AVAILABLE_MODELS,
)


class BenchmarkResult:
    """Store benchmark results for a single model/component combination"""

    def __init__(self, provider: str, model: str, component: str):
        self.provider = provider
        self.model = model
        self.component = component
        self.success = False
        self.iterations = 0
        self.time_elapsed = 0.0
        self.has_positions = False
        self.error_message = ""
        self.api_calls = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "provider": self.provider,
            "model": self.model,
            "component": self.component,
            "success": self.success,
            "iterations": self.iterations,
            "time_elapsed": self.time_elapsed,
            "has_positions": self.has_positions,
            "error_message": self.error_message,
            "api_calls": self.api_calls,
        }


class LLMBenchmark:
    """Benchmark different LLM providers for reference design generation"""

    def __init__(self, test_components: List[str], max_iterations: int = 3):
        self.test_components = test_components
        self.max_iterations = max_iterations
        self.results: List[BenchmarkResult] = []

    def run_single_test(
        self, provider: str, model: str, api_key: str, component: str
    ) -> BenchmarkResult:
        """Run a single benchmark test"""
        result = BenchmarkResult(provider, model, component)

        # Create temporary directory for test
        test_dir = Path(f"/tmp/llm_benchmark/{provider}_{model}_{component}")
        test_dir.mkdir(parents=True, exist_ok=True)

        # Copy component files
        parts_dir = Path(__file__).parent.parent / "parts"
        component_dir = parts_dir / component

        if not component_dir.exists():
            result.error_message = f"Component directory not found: {component}"
            return result

        # Copy files to test directory
        for file in component_dir.iterdir():
            if file.suffix in [".md", ".pdf", ".zen"]:
                target = test_dir / file.name
                target.write_bytes(file.read_bytes())

        # Remove author line from existing .zen to force regeneration
        zen_file = test_dir / f"{component}.zen"
        if zen_file.exists():
            content = zen_file.read_text()
            lines = content.split("\n")
            filtered_lines = [
                line
                for line in lines
                if not line.strip().startswith("Author:")
                and not line.strip().startswith("author:")
            ]
            zen_file.write_text("\n".join(filtered_lines))

        try:
            # Create LLM provider
            llm_provider = create_llm_provider(provider, api_key, model)

            # Create generator
            generator = ReferenceDesignGenerator(llm_provider)

            # Track API calls
            original_generate = llm_provider.generate
            api_call_count = 0

            def tracked_generate(*args, **kwargs):
                nonlocal api_call_count
                api_call_count += 1
                return original_generate(*args, **kwargs)

            llm_provider.generate = tracked_generate

            # Run generation
            start_time = time.time()
            success = generator.generate_design(test_dir, self.max_iterations)
            end_time = time.time()

            result.success = success
            result.time_elapsed = end_time - start_time
            result.api_calls = api_call_count

            # Check if positions were added
            if success and zen_file.exists():
                content = zen_file.read_text()
                result.has_positions = "# pcb:sch" in content and " x=" in content

        except Exception as e:
            result.error_message = str(e)

        return result

    def run_benchmark(self, providers_config: Dict[str, Dict[str, str]]) -> None:
        """Run benchmark for all configured providers"""
        print("Starting LLM Provider Benchmark")
        print("=" * 60)
        print(f"Test components: {', '.join(self.test_components)}")
        print(f"Max iterations per design: {self.max_iterations}")
        print()

        total_tests = sum(
            len(config["models"]) * len(self.test_components)
            for config in providers_config.values()
        )
        current_test = 0

        for provider, config in providers_config.items():
            api_key = config["api_key"]
            models = config["models"]

            for model in models:
                for component in self.test_components:
                    current_test += 1
                    print(
                        f"[{current_test}/{total_tests}] Testing {provider}/{model} "
                        f"on {component}..."
                    )

                    result = self.run_single_test(provider, model, api_key, component)
                    self.results.append(result)

                    if result.success:
                        print(f"  ✓ Success in {result.time_elapsed:.1f}s")
                    else:
                        print(f"  ✗ Failed: {result.error_message or 'Build failed'}")

        print("\n" + "=" * 60)
        self._print_summary()
        self._save_results()

    def _print_summary(self):
        """Print benchmark summary"""
        # Group results by provider/model
        model_stats = {}

        for result in self.results:
            key = f"{result.provider}/{result.model}"
            if key not in model_stats:
                model_stats[key] = {
                    "total": 0,
                    "success": 0,
                    "with_positions": 0,
                    "total_time": 0,
                    "api_calls": 0,
                }

            stats = model_stats[key]
            stats["total"] += 1
            if result.success:
                stats["success"] += 1
                if result.has_positions:
                    stats["with_positions"] += 1
            stats["total_time"] += result.time_elapsed
            stats["api_calls"] += result.api_calls

        # Prepare table data
        table_data = []
        for model_key, stats in model_stats.items():
            success_rate = (
                stats["success"] / stats["total"] * 100 if stats["total"] > 0 else 0
            )
            position_rate = (
                stats["with_positions"] / stats["success"] * 100
                if stats["success"] > 0
                else 0
            )
            avg_time = stats["total_time"] / stats["total"] if stats["total"] > 0 else 0
            avg_api_calls = (
                stats["api_calls"] / stats["total"] if stats["total"] > 0 else 0
            )

            table_data.append(
                [
                    model_key,
                    f"{success_rate:.0f}%",
                    f"{position_rate:.0f}%",
                    f"{avg_time:.1f}s",
                    f"{avg_api_calls:.1f}",
                    f"{stats['total_time']:.1f}s",
                ]
            )

        # Sort by success rate
        table_data.sort(key=lambda x: float(x[1].rstrip("%")), reverse=True)

        headers = [
            "Model",
            "Success Rate",
            "With Positions",
            "Avg Time",
            "Avg API Calls",
            "Total Time",
        ]

        print("\nBENCHMARK RESULTS")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def _save_results(self):
        """Save detailed results to JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = Path(f"benchmark_results_{timestamp}.json")

        data = {
            "timestamp": timestamp,
            "test_components": self.test_components,
            "max_iterations": self.max_iterations,
            "results": [r.to_dict() for r in self.results],
        }

        output_file.write_text(json.dumps(data, indent=2))
        print(f"\nDetailed results saved to: {output_file}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Benchmark LLM providers for reference design generation"
    )
    parser.add_argument(
        "--components",
        nargs="+",
        default=["AD7171", "LTC3555", "MAX6070BAUT12+T"],
        help="Components to test (default: AD7171, LTC3555, MAX6070BAUT12+T)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=3,
        help="Maximum iterations per design (default: 3)",
    )
    parser.add_argument(
        "--providers",
        nargs="+",
        choices=["anthropic", "openai", "gemini"],
        default=["anthropic", "openai", "gemini"],
        help="Providers to benchmark (default: all)",
    )

    args = parser.parse_args()

    # Configure providers
    providers_config = {}

    if "anthropic" in args.providers:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if api_key:
            providers_config["anthropic"] = {
                "api_key": api_key,
                "models": [
                    "claude-opus-4-20250514",  # Most powerful
                    "claude-sonnet-4-20250514",  # Balanced performance
                    "claude-3-5-haiku-20241022",  # Fastest
                ],
            }
        else:
            print("Warning: ANTHROPIC_API_KEY not set, skipping Anthropic")

    if "openai" in args.providers:
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key:
            providers_config["openai"] = {
                "api_key": api_key,
                "models": [
                    "gpt-4o",  # Latest GPT-4 optimized
                    "gpt-4o-mini",  # Cost-efficient
                    "o1-mini",  # Reasoning model
                ],
            }
        else:
            print("Warning: OPENAI_API_KEY not set, skipping OpenAI")

    if "gemini" in args.providers:
        api_key = os.environ.get("GOOGLE_API_KEY")
        if api_key:
            providers_config["gemini"] = {
                "api_key": api_key,
                "models": [
                    "gemini-2.5-pro",  # Enhanced reasoning
                    "gemini-2.5-flash",  # Adaptive, cost-efficient
                    "gemini-2.5-flash-lite-preview-06-17",  # Most cost-efficient
                ],
            }
        else:
            print("Warning: GOOGLE_API_KEY not set, skipping Gemini")

    if not providers_config:
        print("Error: No providers configured. Set API keys in environment.")
        sys.exit(1)

    # Run benchmark
    benchmark = LLMBenchmark(args.components, args.max_iterations)
    benchmark.run_benchmark(providers_config)


if __name__ == "__main__":
    main()
