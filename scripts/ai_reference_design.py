#!/usr/bin/env uv run
# /// script
# dependencies = ["anthropic", "openai", "google-generativeai"]
# ///
"""
Generate reference designs for electronic components using various LLM providers.
This script uses an agentic workflow to iteratively improve designs until they compile.
Supports OpenAI, Anthropic (Claude), and Google (Gemini) models.
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple, List
import json
import time
import argparse
from datetime import datetime
from abc import ABC, abstractmethod
import random

# Try to import LLM packages
try:
    import anthropic

    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

try:
    import openai

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import google.generativeai as genai

    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""

    @abstractmethod
    def __init__(self, api_key: str, model: str):
        """Initialize the provider with API key and model name"""
        self.api_key = api_key
        self.model = model

    @abstractmethod
    def generate(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ) -> str:
        """Generate a response from the LLM"""
        pass

    @abstractmethod
    def generate_stream(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ):
        """Generate a streaming response from the LLM. Yields text chunks."""
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """Get the model name for display/logging"""
        pass


class AnthropicProvider(LLMProvider):
    """Anthropic (Claude) provider"""

    def __init__(self, api_key: str, model: str = "claude-opus-4-20250514"):
        super().__init__(api_key, model)
        if not ANTHROPIC_AVAILABLE:
            raise ImportError(
                "anthropic package not installed. Install with: pip install anthropic"
            )
        self.client = anthropic.Anthropic(api_key=api_key)

    def generate(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ) -> str:
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")

    def generate_stream(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ):
        try:
            stream = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            for event in stream:
                if event.type == "content_block_delta":
                    yield event.delta.text
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")

    def get_model_name(self) -> str:
        return f"Anthropic/{self.model}"


class OpenAIProvider(LLMProvider):
    """OpenAI provider"""

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        super().__init__(api_key, model)
        if not OPENAI_AVAILABLE:
            raise ImportError(
                "openai package not installed. Install with: pip install openai"
            )
        self.client = openai.OpenAI(api_key=api_key)

    def generate(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ) -> str:
        try:
            # O1/O3 models don't support temperature parameter
            if self.model.startswith("o1") or self.model == "o3":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                )
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    temperature=temperature,
                    messages=[{"role": "user", "content": prompt}],
                )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

    def generate_stream(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ):
        # O1 models don't support streaming
        if self.model.startswith("o1") or self.model == "o3":
            # Fallback to non-streaming for reasoning models
            result = self.generate(prompt, max_tokens, temperature)
            # Simulate streaming by yielding the entire result
            yield result
            return

        try:
            # Regular models support temperature
            stream = self.client.chat.completions.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

    def get_model_name(self) -> str:
        return f"OpenAI/{self.model}"


class GeminiProvider(LLMProvider):
    """Google Gemini provider"""

    def __init__(self, api_key: str, model: str = "gemini-2.5-pro"):
        super().__init__(api_key, model)
        if not GEMINI_AVAILABLE:
            raise ImportError(
                "google-generativeai package not installed. Install with: pip install google-generativeai"
            )
        genai.configure(api_key=api_key)

        # Configure safety settings to be less restrictive for code generation
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]

        # System instruction to help with code generation
        system_instruction = (
            "You are an expert electronics engineer generating Zen hardware description "
            "language (based on Starlark) code for electronic components. Focus on technical accuracy and "
            "proper syntax. Generate only valid code without any inappropriate content."
        )

        self.model_instance = genai.GenerativeModel(
            model,
            safety_settings=safety_settings,
            system_instruction=system_instruction,
        )

    def generate(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ) -> str:
        try:
            generation_config = genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=temperature,
            )
            response = self.model_instance.generate_content(
                prompt, generation_config=generation_config
            )

            # Check if response was blocked
            if not response.parts:
                # Try to get the safety ratings for debugging
                if hasattr(response, "prompt_feedback"):
                    raise Exception(
                        f"Gemini blocked the response. Reason: {response.prompt_feedback}"
                    )
                else:
                    raise Exception(
                        "Gemini returned an empty response (possibly blocked by safety filters)"
                    )

            return response.text
        except AttributeError as e:
            # Handle case where response.text is not accessible
            if "response.text" in str(e):
                raise Exception(
                    "Gemini response was blocked by safety filters or returned no content"
                )
            raise Exception(f"Gemini API error: {str(e)}")
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")

    def generate_stream(
        self, prompt: str, max_tokens: int = 8192, temperature: float = 0.3
    ):
        try:
            generation_config = genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=temperature,
            )
            response = self.model_instance.generate_content(
                prompt,
                generation_config=generation_config,
                stream=True,
            )

            has_content = False
            for chunk in response:
                if hasattr(chunk, "text") and chunk.text:
                    has_content = True
                    yield chunk.text
                elif hasattr(chunk, "parts") and chunk.parts:
                    # Try to extract text from parts
                    for part in chunk.parts:
                        if hasattr(part, "text") and part.text:
                            has_content = True
                            yield part.text

            if not has_content:
                raise Exception(
                    "Gemini streaming returned no content (possibly blocked by safety filters)"
                )

        except AttributeError as e:
            if "text" in str(e):
                raise Exception(
                    "Gemini streaming response was blocked by safety filters"
                )
            raise Exception(f"Gemini API error: {str(e)}")
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")

    def get_model_name(self) -> str:
        return f"Google/{self.model}"


# Available models for each provider
AVAILABLE_MODELS = {
    "anthropic": [
        "claude-opus-4-20250514",  # Claude Opus 4 - most powerful
        "claude-sonnet-4-20250514",  # Claude Sonnet 4 - balanced
        "claude-3-7-sonnet-20250219",  # Claude Sonnet 3.7 - enhanced reasoning
        "claude-3-5-haiku-20241022",  # Claude Haiku 3.5 - fastest
        # Legacy models (kept for compatibility)
        "claude-3-5-sonnet-20241022",
        "claude-3-opus-20240229",
    ],
    "openai": [
        "o3",  # Latest reasoning model
        "o1",  # Advanced reasoning
        "o1-mini",  # Smaller reasoning model
        "gpt-4o-2024-11-20",
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-4",
        "gpt-3.5-turbo",
    ],
    "gemini": [
        "gemini-2.5-pro",  # Enhanced thinking and reasoning, multimodal
        "gemini-2.5-flash",  # Adaptive thinking, cost efficient
        "gemini-2.5-flash-lite-preview-06-17",  # Most cost-efficient
        # Legacy models (kept for compatibility)
        "gemini-2.0-flash-exp",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
    ],
}


def create_llm_provider(
    provider: str, api_key: str, model: Optional[str] = None
) -> LLMProvider:
    """Factory function to create LLM provider instances"""
    provider = provider.lower()

    if provider == "anthropic":
        if model is None:
            model = AVAILABLE_MODELS["anthropic"][0]
        return AnthropicProvider(api_key, model)
    elif provider == "openai":
        if model is None:
            model = AVAILABLE_MODELS["openai"][0]
        return OpenAIProvider(api_key, model)
    elif provider == "gemini":
        if model is None:
            model = AVAILABLE_MODELS["gemini"][0]
        return GeminiProvider(api_key, model)
    else:
        raise ValueError(
            f"Unknown provider: {provider}. Available: anthropic, openai, gemini"
        )


class ReferenceDesignGenerator:
    """Generate reference designs using various LLM providers"""

    def __init__(
        self,
        llm_provider: LLMProvider,
        enable_streaming: bool = True,
        example_parts: Optional[List[Tuple[str, str]]] = None,
    ):
        """Initialize with LLM provider"""
        self.llm = llm_provider
        self.enable_streaming = enable_streaming
        self.example_designs = self._load_example_designs(example_parts)

    def _load_example_designs(
        self, custom_example_parts: Optional[List[Tuple[str, str]]] = None
    ) -> List[Tuple[str, str]]:
        """Load multiple example designs as (name, content) tuples"""
        examples = []

        # Use custom examples if provided, otherwise use defaults
        if custom_example_parts:
            example_parts = custom_example_parts
            print(f"Loading {len(example_parts)} custom example(s)...")

            # Load the custom examples
            for category, part_name in example_parts:
                example_path = (
                    Path(__file__).parent.parent
                    / "parts"
                    / category
                    / part_name
                    / f"{part_name}.zen"
                )
                if example_path.exists():
                    content = example_path.read_text()
                    examples.append((part_name, content))
                else:
                    print(
                        f"  ⚠ Warning: Example {part_name} not found at {example_path}"
                    )
        else:
            # Automatically load all .zen files from the examples folder
            examples_dir = Path(__file__).parent.parent / "parts" / "examples"

            if examples_dir.exists() and examples_dir.is_dir():
                # Find all .zen files in subdirectories of the examples folder
                zen_files = []
                for part_dir in examples_dir.iterdir():
                    if part_dir.is_dir():
                        zen_file = part_dir / f"{part_dir.name}.zen"
                        if zen_file.exists():
                            zen_files.append((part_dir.name, zen_file))

                print(f"Loading {len(zen_files)} example(s) from examples folder...")

                # Load all found .zen files
                for part_name, zen_path in sorted(zen_files):
                    try:
                        content = zen_path.read_text()
                        examples.append((part_name, content))
                    except Exception as e:
                        print(f"  ⚠ Warning: Failed to load {part_name}: {str(e)}")
            else:
                print(f"  ⚠ Warning: Examples directory not found at {examples_dir}")

        if examples:
            print(
                f"  ✓ Successfully loaded {len(examples)} example design(s): {', '.join([name for name, _ in examples])}"
            )
        else:
            print(f"  ⚠ Warning: No example designs could be loaded")

        return examples

    def _has_reference_design(self, zen_file_path: Path) -> bool:
        """Check if a file already has a reference design (has proper docstring)"""
        if not zen_file_path.exists():
            return False

        content = zen_file_path.read_text()
        # Check for docstring with author and datasheet
        has_author = "author:" in content.lower()
        has_datasheet = "datasheet:" in content.lower()
        has_docstring = '"""' in content[:200]  # Check first 200 chars for docstring

        return has_author and has_datasheet and has_docstring

    def _create_initial_prompt(
        self,
        part_name: str,
        datasheet_content: str,
        existing_zen: str = "",
        model_name: str = "",
    ) -> str:
        """Create the initial prompt"""
        existing_section = ""
        if existing_zen:
            existing_section = f"""
## Existing Basic Design

Here's the current basic .zen file that already compiles successfully:

```zen
{existing_zen}
```

Please enhance this existing design by:
- Adding a proper docstring with description, author (@{model_name}), and datasheet URL
- Adding necessary imports from @stdlib
- Adding configuration options
- Adding supporting components (capacitors, resistors, etc.)
- Improving the overall design based on the datasheet

CRITICAL: DO NOT MODIFY:
- The Component name
- The symbol library and name
- The footprint path
- The pin names (you can modify the nets attached to the pins)
These are already validated and MUST remain exactly as they are in the existing design.

"""

        # Extract model name for author field (remove provider prefix)
        model_name = self.llm.get_model_name()
        if "/" in model_name:
            model_name = model_name.split("/", 1)[1]

        # Format all examples
        examples_section = ""
        if self.example_designs:
            examples_section = "## Example Reference Designs\n\n"
            examples_section += "Study these examples to understand the expected structure and style:\n\n"

            for i, (example_name, example_content) in enumerate(
                self.example_designs, 1
            ):
                examples_section += f"### Example {i}: {example_name}\n\n"
                examples_section += f"```zen\n{example_content}\n```\n\n"
        else:
            # Fallback if no examples loaded
            examples_section = "## Note\n\nNo example designs were loaded. Please follow Zen language best practices.\n\n"

        return f"""
You are an expert electronics engineer tasked with creating a reference design in the Zen hardware description language.
Zen or Zener is based on Starlark (the same language used for Bazel build files).

{examples_section}{existing_section}
## Task

Create a reference design for the {part_name} component. The design should:

1. Start with a docstring containing:
   - A description of the component
   - Author: @{model_name}
   - Reviewer: <not_reviewed>
   - Datasheet: [URL if available in the datasheet content]

2. Include appropriate imports from @stdlib (e.g., interfaces, generics)

3. Define configuration options using config() for customizable features

4. Define external IO pins using io()

5. Create the main Component with:
   - Correct symbol from @kicad-symbols library
   - Correct footprint from @kicad-footprints
   - All pins properly connected

6. Add supporting components like:
   - Decoupling capacitors
   - Pull-up/pull-down resistors
   - Input/output filtering
   - Protection circuits
   
7. Use proper Zen language syntax and idioms

## Datasheet Content

{datasheet_content[:50000]}  # Limit to first 50k chars to avoid token limits

## Instructions

Based on the datasheet information above, create a complete reference design for {part_name}. Make sure to:
- Keep the existing Component definition EXACTLY as is (name, symbol, footprint, pins)
- Add appropriate supporting components around the main component
- DO NOT OVERCOMPLICATE THE DESIGN, WE WANT TO KEEP IT SIMPLE AND EASY TO UNDERSTAND
- Use configuration options for flexibility
- Follow the style and patterns from the examples
- Add proper imports and type definitions

If an existing design was provided, preserve the Component block entirely and only add enhancements around it.

Generate only the .zen file content, no explanations needed."""

    def _create_iteration_prompt(self, current_design: str, build_output: str) -> str:
        """Create a prompt for fixing build errors"""
        return f"""The reference design failed to compile with the following error:

```
{build_output}
```

Current design:
```zen
{current_design}
```

Please fix the error and provide the corrected .zen file content. Common issues:
- Syntax errors in Zen language
- Missing imports
- Incorrect references to nets or components
- Type mismatches

CRITICAL REMINDER: DO NOT MODIFY:
- The Component name, symbol, or footprint
- The pin names in the Component pins mapping
These are validated and must remain unchanged from the original design.

Generate only the corrected .zen file content."""

    def _call_llm(self, prompt: str, show_progress: bool = True) -> str:
        """Call LLM API and return the response"""
        try:
            if self.enable_streaming and show_progress:
                return self._call_llm_stream(prompt)
            else:
                return self.llm.generate(prompt)
        except Exception as e:
            print(f"  ✗ LLM API error: {str(e)}")
            return ""

    def _call_llm_stream(self, prompt: str) -> str:
        """Call LLM API with streaming and display progress"""
        print("  → Generating response", end="", flush=True)
        collected_text = []
        spinner = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        spinner_idx = 0
        chunk_count = 0

        try:
            for chunk in self.llm.generate_stream(prompt):
                collected_text.append(chunk)
                chunk_count += 1

                # Update spinner every few chunks
                if chunk_count % 5 == 0:
                    print(
                        f"\r  → Generating response {spinner[spinner_idx]} ",
                        end="",
                        flush=True,
                    )
                    spinner_idx = (spinner_idx + 1) % len(spinner)

            # Clear the line and print completion
            print(
                f"\r  → Generated response ({len(''.join(collected_text))} chars)    "
            )
            return "".join(collected_text)
        except Exception as e:
            print("\r  ✗ Generation failed" + " " * 20)  # Clear the line
            raise e

    def _extract_zen_code(self, response: str) -> str:
        """Extract .zen code response"""
        # Look for code blocks
        if "```zen" in response:
            start = response.find("```zen") + 6
            end = response.find("```", start)
            if end > start:
                return response[start:end].strip()
        elif "```" in response:
            # Generic code block
            start = response.find("```") + 3
            # Skip language identifier if present
            if (
                response[start : start + 10].strip()
                and "\n" in response[start : start + 10]
            ):
                start = response.find("\n", start) + 1
            end = response.find("```", start)
            if end > start:
                return response[start:end].strip()

        # If no code blocks, return the whole response (might be just code)
        return response.strip()

    def _run_pcb_build(self, zen_file_path: Path) -> Tuple[bool, str]:
        """Run pcb build and return success status and output"""
        try:
            result = subprocess.run(
                ["pcb", "build", str(zen_file_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )

            success = result.returncode == 0
            output = result.stdout if success else result.stderr
            return success, output

        except subprocess.TimeoutExpired:
            return False, "Build timeout - process took too long"
        except FileNotFoundError:
            return False, "pcb command not found - make sure it's installed"
        except Exception as e:
            return False, f"Build error: {str(e)}"

    def _create_position_optimization_prompt(
        self, zen_content: str, part_name: str
    ) -> str:
        """Create a prompt for optimizing component positions"""
        return f"""You are an experienced electronics engineer tasked with optimizing the schematic layout of a reference design.

## Current Design

```zen
{zen_content}
```

## Task

Please analyze the current design and provide optimized position annotations for all components to create a professional, readable schematic initial layout.

If the schematics are complex, prefer arranging the components in a grid without overlapping them, with appropriate spacing, this way the user can easily modify the layout.

## Required Output Format

Provide ONLY the position annotations in this exact format:

```
# pcb:sch COMPONENT_NAME x=VALUE y=VALUE rot=ROTATION
```

Where:
- COMPONENT_NAME matches exactly the component names in the design
- x and y are coordinates (can be negative)
- rot is rotation in degrees (0, 90, 180, or 270)

Example:
```
# pcb:sch AD7171 x=241.3000 y=203.2000 rot=0
# pcb:sch C_BULK.CAPACITOR x=558.8000 y=88.9000 rot=0
# pcb:sch C_DEC.CAPACITOR x=495.3000 y=88.9000 rot=0
# pcb:sch R_PULLUP.R x=63.5000 y=355.6000 rot=0
```

Generate position annotations for ALL components in the design. Ensure the layout would be clear and professional when rendered."""

    def _extract_position_annotations(self, response: str) -> List[str]:
        """Extract position annotations response"""
        # First try to extract from code blocks
        content = response.strip()
        if "```" in content:
            # Extract content from code block
            start = content.find("```")
            if start != -1:
                start = content.find("\n", start) + 1
                end = content.find("```", start)
                if end > start:
                    content = content[start:end].strip()

        lines = content.split("\n")
        annotations = []

        for line in lines:
            line = line.strip()
            # Look for lines that match the position annotation format
            if line.startswith("# pcb:sch") and " x=" in line and " y=" in line:
                annotations.append(line)

        return annotations

    def _apply_position_annotations(
        self, zen_content: str, annotations: List[str]
    ) -> str:
        """Apply position annotations to the zen file content"""
        # Remove any existing position annotations
        lines = zen_content.split("\n")
        filtered_lines = []

        for line in lines:
            if not (
                line.strip().startswith("# pcb:sch") and " x=" in line and " y=" in line
            ):
                filtered_lines.append(line)

        # Add new annotations at the end of the file
        result = "\n".join(filtered_lines).rstrip()
        if annotations:
            result += "\n\n" + "\n".join(annotations)

        return result

    def generate_design(self, part_dir: Path, max_iterations: int = 5) -> bool:
        """Generate a reference design for a part with iterative improvements"""
        part_name = part_dir.name
        zen_file_path = part_dir / f"{part_name}.zen"
        md_file_path = part_dir / f"{part_name}.md"

        print(f"\nProcessing {part_name}...")

        # Check if already has a reference design
        if self._has_reference_design(zen_file_path):
            print(f"  → Already has a reference design, skipping")
            return True

        # Check if markdown datasheet exists
        if not md_file_path.exists():
            print(f"  ✗ No markdown datasheet found")
            return False

        # Load datasheet content
        datasheet_content = md_file_path.read_text()

        # Load existing .zen file if it exists
        existing_zen = ""
        if zen_file_path.exists():
            existing_zen = zen_file_path.read_text()
            print(f"  → Found existing basic design to enhance")

        # Generate initial design
        print(f"  → Generating initial design with {self.llm.get_model_name()}...")
        initial_prompt = self._create_initial_prompt(
            part_name, datasheet_content, existing_zen, self.llm.get_model_name()
        )
        response = self._call_llm(initial_prompt)

        if not response:
            print(f"  ✗ Failed to get response from the model")
            return False

        # Extract and save the design
        zen_content = self._extract_zen_code(response)
        zen_file_path.write_text(zen_content)

        # Iterative improvement loop
        for iteration in range(max_iterations):
            print(f"  → Building (iteration {iteration + 1}/{max_iterations})...")
            success, output = self._run_pcb_build(zen_file_path)

            if success:
                print(f"  ✓ Build successful!")

                # Position optimization pass
                print(f"  → Optimizing component positions...")
                position_prompt = self._create_position_optimization_prompt(
                    zen_content, part_name
                )
                position_response = self._call_llm(position_prompt)

                if position_response:
                    annotations = self._extract_position_annotations(position_response)
                    if annotations:
                        print(
                            f"  → Applying {len(annotations)} position annotations..."
                        )
                        optimized_content = self._apply_position_annotations(
                            zen_content, annotations
                        )
                        zen_file_path.write_text(optimized_content)

                        # Verify the optimized design still builds
                        print(f"  → Verifying optimized design...")
                        verify_success, verify_output = self._run_pcb_build(
                            zen_file_path
                        )

                        if verify_success:
                            print(f"  ✓ Position optimization complete!")
                            return True
                        else:
                            print(f"  ⚠ Optimized design failed to build, reverting...")
                            # Revert to the working version
                            zen_file_path.write_text(zen_content)
                            print(f"  ✓ Reverted to working design")
                            return True
                    else:
                        print(f"  ⚠ No position annotations extracted")
                else:
                    print(
                        f"  ⚠ Failed to get position optimization from {self.llm.get_model_name()}"
                    )

                # Return True even if position optimization failed - we still have a working design
                return True

            print(f"  → Build failed, asking {self.llm.get_model_name()} to fix...")

            # Get fix from LLM
            fix_prompt = self._create_iteration_prompt(zen_content, output)
            response = self._call_llm(fix_prompt)

            if not response:
                print(f"  ✗ Failed to get fix from {self.llm.get_model_name()}")
                return False

            # Update design
            zen_content = self._extract_zen_code(response)
            zen_file_path.write_text(zen_content)

        print(f"  ✗ Failed after {max_iterations} iterations")
        return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Generate reference designs using various LLM providers"
    )
    parser.add_argument(
        "--provider",
        choices=["anthropic", "openai", "gemini"],
        default="anthropic",
        help="LLM provider to use (default: anthropic)",
    )
    parser.add_argument(
        "--model",
        default="claude-4-opus-20250514",
        help="Specific model to use (see AVAILABLE_MODELS for options)",
    )
    parser.add_argument(
        "--api-key",
        help="API key for the provider (or set PROVIDER_API_KEY env var)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=5,
        help="Maximum iterations to try fixing build errors (default: 5)",
    )
    parser.add_argument(
        "--parts", nargs="+", help="Specific parts to process (default: all parts)"
    )
    parser.add_argument(
        "--directory",
        type=str,
        default="parts",
        help="Directory containing parts to process (default: parts)",
    )
    parser.add_argument(
        "--max-designs",
        type=int,
        default=1,
        help="Maximum number of designs to generate (default: 1)",
    )
    parser.add_argument(
        "--random",
        action="store_true",
        help="Randomly select parts instead of alphabetical order",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip parts that already have reference designs (default: True)",
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available models for each provider and exit",
    )
    parser.add_argument(
        "--no-streaming",
        action="store_true",
        help="Disable streaming output (default: streaming enabled)",
    )
    parser.add_argument(
        "--examples",
        nargs=2,
        action="append",
        metavar=("CATEGORY", "PART_NAME"),
        help="Add a custom example design. Format: --examples <category> <part_name>. "
        "Example: --examples interesting LTC3555. Can be used multiple times. "
        "If not specified, automatically loads all .zen files from the parts/examples folder",
    )

    args = parser.parse_args()

    # Handle --list-models
    if args.list_models:
        print("\nAvailable models by provider:\n")
        for provider, models in AVAILABLE_MODELS.items():
            print(f"{provider.upper()}:")
            for model in models:
                print(f"  - {model}")
            print()
        sys.exit(0)

    # Get API key
    api_key = args.api_key
    if not api_key:
        # Try environment variables based on provider
        env_vars = {
            "anthropic": "ANTHROPIC_API_KEY",
            "openai": "OPENAI_API_KEY",
            "gemini": "GOOGLE_API_KEY",
        }
        env_var = env_vars.get(args.provider)
        if env_var:
            api_key = os.environ.get(env_var)

    if not api_key:
        print(
            f"Error: API key required for {args.provider}. "
            f"Set {env_vars.get(args.provider, 'API_KEY')} env var or use --api-key"
        )
        sys.exit(1)

    # Create LLM provider
    try:
        llm_provider = create_llm_provider(args.provider, api_key, args.model)
        print(f"Using LLM: {llm_provider.get_model_name()}")
        if args.provider == "gemini":
            print("  → Configured with relaxed safety settings for code generation")
    except Exception as e:
        print(f"Error creating LLM provider: {str(e)}")
        sys.exit(1)

    # Initialize generator
    generator = ReferenceDesignGenerator(
        llm_provider,
        enable_streaming=not args.no_streaming,
        example_parts=args.examples,
    )

    # Get parts directory
    script_dir = Path(__file__).parent
    if args.directory.startswith("/"):
        # Absolute path
        parts_dir = Path(args.directory)
    else:
        # Relative path from script parent
        parts_dir = script_dir.parent / args.directory

    if not parts_dir.exists():
        print(f"Error: parts directory not found at {parts_dir}")
        sys.exit(1)

    # Get list of parts to process
    if args.parts:
        part_dirs = [parts_dir / part for part in args.parts]
        # Filter out non-existent directories
        part_dirs = [d for d in part_dirs if d.exists()]
    else:
        # Get all subdirectories
        all_part_dirs = [d for d in parts_dir.iterdir() if d.is_dir()]

        if args.random:
            # Randomly shuffle the parts
            random.shuffle(all_part_dirs)
        else:
            # Sort for consistent ordering
            all_part_dirs.sort()

        # Limit to max_designs
        part_dirs = all_part_dirs[: args.max_designs]

    if not args.parts:
        total_available = len([d for d in parts_dir.iterdir() if d.is_dir()])
        print(f"Found {total_available} total parts in {parts_dir}")
        selection_mode = "randomly selected" if args.random else "first"
        print(
            f"Processing {len(part_dirs)} {selection_mode} parts (limited by --max-designs={args.max_designs})"
        )
    else:
        print(f"Processing {len(part_dirs)} specified parts")

    print(f"Max iterations per part: {args.max_iterations}")
    print(f"Skip existing: {args.skip_existing}")
    print("-" * 60)

    # Track statistics
    total = len(part_dirs)
    successful = 0
    failed = 0
    skipped = 0

    start_time = time.time()

    # Process each part
    for i, part_dir in enumerate(part_dirs, 1):
        try:
            if generator.generate_design(part_dir, args.max_iterations):
                if generator._has_reference_design(part_dir / f"{part_dir.name}.zen"):
                    successful += 1
                else:
                    skipped += 1
            else:
                failed += 1

            # Progress update
            elapsed = time.time() - start_time
            if elapsed > 0 and i < total:
                rate = i / elapsed
                eta = (total - i) / rate
                print(
                    f"  Progress: {i}/{total} ({i/total*100:.1f}%) - ETA: {eta/60:.1f} min"
                )

        except KeyboardInterrupt:
            print("\n\nInterrupted by user")
            break
        except Exception as e:
            print(f"  ✗ Unexpected error: {str(e)}")
            failed += 1

    # Final summary
    elapsed_total = time.time() - start_time
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total parts: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")
    print(f"Total time: {elapsed_total/60:.1f} minutes")

    if successful > 0:
        print(f"\n✓ Successfully generated {successful} reference designs!")


if __name__ == "__main__":
    main()
