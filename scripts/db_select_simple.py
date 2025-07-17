#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.8"
# dependencies = ["pandas"]
# ///

import pandas as pd
import re
from pathlib import Path
from typing import List, Set, Tuple
import random

# Simple IC categories that make good benchmarks
BENCHMARK_CATEGORIES = {
    "ldo": {
        "keywords": [
            "ldo",
            "low dropout",
            "linear regulator",
            "voltage regulator linear",
        ],
        "exclude": ["switching", "buck", "boost", "controller"],
        "score": 10,
        "max_count": 20,
    },
    "buck": {
        "keywords": ["buck converter", "buck regulator", "step-down", "buck-boost"],
        "exclude": ["controller only", "complex", "multiphase"],
        "score": 9,
        "max_count": 15,
    },
    "voltage_reference": {
        "keywords": [
            "voltage reference",
            "bandgap",
            "precision reference",
            "shunt reference",
        ],
        "exclude": ["adc", "dac", "complex"],
        "score": 10,
        "max_count": 10,
    },
    "simple_regulator": {
        "keywords": [
            "7805",
            "7812",
            "7815",
            "78xx",
            "79xx",
            "317",
            "337",
            "fixed regulator",
        ],
        "exclude": ["switching", "complex"],
        "score": 8,
        "max_count": 10,
    },
    "charge_pump": {
        "keywords": [
            "charge pump",
            "switched capacitor",
            "voltage doubler",
            "voltage inverter",
        ],
        "exclude": ["complex", "multi-output"],
        "score": 7,
        "max_count": 5,
    },
    "simple_opamp": {
        "keywords": [
            "single opamp",
            "dual opamp",
            "general purpose op",
            "LM358",
            "LM324",
            "TL07",
            "NE555",
        ],
        "exclude": ["instrumentation", "precision", "multi-channel", "complex"],
        "score": 8,
        "max_count": 10,
    },
    "simple_comparator": {
        "keywords": ["comparator", "voltage comparator", "LM339", "LM393"],
        "exclude": ["window", "multi-channel", "complex"],
        "score": 7,
        "max_count": 5,
    },
    "simple_buffer": {
        "keywords": ["buffer", "unity gain", "voltage follower", "line driver"],
        "exclude": ["complex", "multi-channel", "programmable"],
        "score": 6,
        "max_count": 5,
    },
}

# Patterns that indicate simple ICs
SIMPLE_IC_PATTERNS = [
    r"^LM\d{3,4}",  # Classic LM series
    r"^NE\d{3,4}",  # NE555 and similar
    r"^TL0\d{2}",  # TL071, TL072, etc.
    r"^UA\d{3}",  # UA741, etc.
    r"^78[LM]?\d{2}",  # 7805, 78L05, etc.
    r"^79[LM]?\d{2}",  # Negative regulators
    r"^LM317",  # Adjustable regulators
    r"^LM337",
    r"^TPS\d{5}",  # Simple TI regulators
    r"^MCP\d{4}",  # Simple Microchip parts
    r"^REF\d{4}",  # Voltage references
    r"^MAX\d{3}",  # Simple MAX parts (3-digit)
]


def is_simple_ic(symbol: str, description: str) -> bool:
    """Check if an IC appears to be simple based on patterns"""
    symbol_upper = symbol.upper()
    desc_lower = description.lower()

    # Check symbol patterns
    for pattern in SIMPLE_IC_PATTERNS:
        if re.match(pattern, symbol_upper):
            return True

    # Check for simple descriptors
    simple_keywords = ["simple", "general purpose", "basic", "standard", "fixed output"]
    for keyword in simple_keywords:
        if keyword in desc_lower:
            return True

    # Exclude complex ICs
    complex_keywords = [
        "microcontroller",
        "mcu",
        "dsp",
        "fpga",
        "cpld",
        "ethernet",
        "usb",
        "hdmi",
        "pcie",
        "multi-channel",
        "16-channel",
        "32-channel",
        "programmable",
        "configurable",
        "codec",
        "modem",
        "transceiver",
    ]
    for keyword in complex_keywords:
        if keyword in desc_lower:
            return False

    return False


def categorize_benchmark_ic(row: pd.Series) -> Tuple[str, int]:
    """Categorize an IC for benchmark suitability"""
    desc_lower = str(row["Description"]).lower()
    symbol = str(row["Symbol"])
    value_lower = str(row["Value"]).lower()

    # Check each benchmark category
    for category, config in BENCHMARK_CATEGORIES.items():
        # Check positive keywords
        matched = False
        for keyword in config["keywords"]:
            if keyword in desc_lower or keyword in value_lower:
                matched = True
                break

        if matched:
            # Check exclusion keywords
            excluded = False
            for exclude in config["exclude"]:
                if exclude in desc_lower:
                    excluded = True
                    break

            if not excluded:
                # Bonus points for simple ICs
                bonus = 2 if is_simple_ic(symbol, row["Description"]) else 0
                return category, config["score"] + bonus

    # Check if it's a simple IC even if not in specific categories
    if is_simple_ic(symbol, row["Description"]):
        return "other_simple", 5

    return "complex", 0


def select_benchmark_set(df: pd.DataFrame, target_count: int = 100) -> pd.DataFrame:
    """Select a set of simple benchmark ICs"""
    # Categorize all ICs
    categories_scores = df.apply(categorize_benchmark_ic, axis=1)
    df["category"] = categories_scores.apply(lambda x: x[0])
    df["score"] = categories_scores.apply(lambda x: x[1])

    # Remove complex ICs
    df = df[df["category"] != "complex"]

    # Sort by score (highest first)
    df = df.sort_values("score", ascending=False)

    # Select diverse set with category limits and unique datasheets
    selected = []
    category_counts = {}
    seen_datasheets = set()

    for _, row in df.iterrows():
        category = row["category"]
        datasheet = str(row.get("Datasheet", "")).strip()

        # Skip if we've already seen this datasheet (unless it's empty/missing)
        if datasheet and datasheet != "nan" and datasheet in seen_datasheets:
            continue

        if category not in category_counts:
            category_counts[category] = 0

        # Check category limit
        max_count = BENCHMARK_CATEGORIES.get(category, {}).get("max_count", 10)
        if category_counts[category] < max_count:
            selected.append(row)
            category_counts[category] += 1

            # Track this datasheet
            if datasheet and datasheet != "nan":
                seen_datasheets.add(datasheet)

            if len(selected) >= target_count:
                break

    result_df = pd.DataFrame(selected)
    return result_df


def main():
    # Read the CSV file
    csv_file = "data/db_all.csv"

    print("Loading KiCad symbols CSV...")
    df = pd.read_csv(csv_file)
    print(f"Total symbols loaded: {len(df)}")

    # Filter to only IC-like components
    print("\nFiltering for integrated circuits...")

    # Remove obvious non-ICs
    non_ic_keywords = [
        "resistor",
        "capacitor",
        "inductor",
        "ferrite",
        "crystal",
        "antenna",
        "fuse",
        "varistor",
        "connector",
        "jumper",
        "test point",
    ]
    for keyword in non_ic_keywords:
        df = df[~df["Description"].str.lower().str.contains(keyword, na=False)]

    print(f"Symbols after filtering non-ICs: {len(df)}")

    # Select benchmark ICs
    print("\nSelecting simple benchmark ICs (LDOs, buck converters, etc.)...")
    selected_df = select_benchmark_set(df, target_count=100)

    print(f"\nSelected {len(selected_df)} benchmark ICs")

    # Show category distribution
    print("\nCategory distribution:")
    category_counts = selected_df["category"].value_counts()
    for category, count in category_counts.items():
        if category != "other_simple":
            print(f"  {category:<20} {count:>4} ICs")
    if "other_simple" in category_counts:
        print(f"  {'other_simple':<20} {category_counts['other_simple']:>4} ICs")

    # Save to new CSV
    output_file = "data/db_simple.csv"
    selected_df = selected_df.drop(
        columns=["category", "score"]
    )  # Remove helper columns
    selected_df.to_csv(output_file, index=False)
    print(f"\nSaved {len(selected_df)} selected ICs to {output_file}")

    # Show some examples
    print("\nExample benchmark ICs:")
    print("-" * 100)

    # Re-categorize for display
    selected_df["category"] = selected_df.apply(
        lambda row: categorize_benchmark_ic(row)[0], axis=1
    )

    # Show examples from key categories
    for category in [
        "ldo",
        "buck",
        "voltage_reference",
        "simple_regulator",
        "simple_opamp",
    ]:
        cat_df = selected_df[selected_df["category"] == category].head(3)
        if not cat_df.empty:
            print(f"\n{category.upper().replace('_', ' ')}:")
            for _, row in cat_df.iterrows():
                desc_preview = (
                    row["Description"][:60] + "..."
                    if len(row["Description"]) > 60
                    else row["Description"]
                )
                print(f"  {row['Symbol']:<20} - {desc_preview}")


if __name__ == "__main__":
    main()
