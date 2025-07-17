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

# Categories of ICs that typically need passive components
INTERESTING_CATEGORIES = {
    "adc": ["adc", "analog-to-digital", "a/d converter", "a-d converter"],
    "dac": ["dac", "digital-to-analog", "d/a converter", "d-a converter"],
    "amplifier": [
        "amplifier",
        "amp",
        "opamp",
        "op-amp",
        "instrumentation",
        "audio amp",
    ],
    "regulator": ["regulator", "ldo", "switching", "buck", "boost", "converter"],
    "pll": ["pll", "phase locked", "clock", "oscillator", "timer"],
    "interface": ["uart", "spi", "i2c", "can", "ethernet", "usb", "rs485", "rs232"],
    "driver": ["driver", "motor", "led driver", "display driver", "fet driver"],
    "sensor_interface": [
        "sensor",
        "temperature",
        "pressure",
        "humidity",
        "current sense",
    ],
    "power": ["power management", "pmic", "battery", "charger", "fuel gauge"],
    "codec": ["codec", "audio", "video"],
    "memory": ["eeprom", "flash", "ram", "nvram"],
    "mcu": ["microcontroller", "mcu", "microprocessor", "cpu"],
    "dsp": ["dsp", "digital signal"],
    "rf": ["rf", "radio", "wireless", "transceiver", "bluetooth", "wifi"],
    "fpga": ["fpga", "cpld", "programmable logic"],
    "shift_register": ["shift register", "595", "165", "4094"],
    "multiplexer": ["multiplexer", "mux", "analog switch", "4051", "4052", "4053"],
    "comparator": ["comparator", "voltage comparator"],
    "reference": ["reference", "voltage reference", "current reference", "bandgap"],
}

# Categories to de-prioritize or exclude
BORING_CATEGORIES = [
    "single gate",
    "dual gate",
    "triple gate",
    "quad gate",
    "hex inverter",
    "hex buffer",
    "nand gate",
    "nor gate",
    "and gate",
    "or gate",
    "xor gate",
    "flip-flop",
    "latch",
    "counter",
    "divider",
    "connector",
    "mounting",
    "transistor array",
    "darlington",
]


def categorize_ic(row: pd.Series) -> Tuple[str, int]:
    """Categorize an IC based on its properties and return category and score"""
    desc_lower = str(row["Description"]).lower()
    symbol_lower = str(row["Symbol"]).lower()
    value_lower = str(row["Value"]).lower()

    # Check if it's a boring category first
    for boring in BORING_CATEGORIES:
        if boring in desc_lower:
            return "boring", 0

    # Check for interesting categories
    best_category = "other"
    best_score = 1

    for category, keywords in INTERESTING_CATEGORIES.items():
        for keyword in keywords:
            if (
                keyword in desc_lower
                or keyword in symbol_lower
                or keyword in value_lower
            ):
                # Higher scores for more complex categories
                category_scores = {
                    "adc": 10,
                    "dac": 10,
                    "amplifier": 8,
                    "regulator": 7,
                    "pll": 9,
                    "interface": 8,
                    "driver": 7,
                    "sensor_interface": 9,
                    "power": 8,
                    "codec": 10,
                    "memory": 6,
                    "mcu": 5,  # Lower because there are many MCUs
                    "dsp": 9,
                    "rf": 9,
                    "fpga": 7,
                    "shift_register": 8,
                    "multiplexer": 8,
                    "comparator": 7,
                    "reference": 9,
                }
                score = category_scores.get(category, 5)
                if score > best_score:
                    best_category = category
                    best_score = score

    return best_category, best_score


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate ICs (same base part number, different packages)"""

    # Extract base part number (remove package suffixes)
    def get_base_part(symbol: str) -> str:
        # Common package suffixes to remove
        suffixes = [
            r"[_-]?DIP\d*",
            r"[_-]?SOIC\d*",
            r"[_-]?TSSOP\d*",
            r"[_-]?QFN\d*",
            r"[_-]?LQFP\d*",
            r"[_-]?MSOP\d*",
            r"[_-]?SOT\d*",
            r"[_-]?TO\d*",
            r"[_-]?[A-Z]{1,4}$",
            r"[_-]?\d+[A-Z]{1,3}$",
        ]

        base = symbol
        for suffix in suffixes:
            base = re.sub(suffix, "", base, flags=re.IGNORECASE)

        return base.strip("_-")

    df["base_part"] = df["Symbol"].apply(get_base_part)

    # Keep the first occurrence of each base part
    # But prefer certain packages (SMD over through-hole)
    def package_priority(footprint: str) -> int:
        footprint_lower = str(footprint).lower()
        if "qfn" in footprint_lower:
            return 1
        if "soic" in footprint_lower:
            return 2
        if "tssop" in footprint_lower:
            return 3
        if "msop" in footprint_lower:
            return 4
        if "sot" in footprint_lower:
            return 5
        if "dip" in footprint_lower:
            return 10
        return 6

    df["package_priority"] = df["Footprint"].apply(package_priority)
    df = df.sort_values(["base_part", "package_priority"])
    df = df.drop_duplicates(subset=["base_part"], keep="first")

    return df.drop(columns=["base_part", "package_priority"])


def select_diverse_set(df: pd.DataFrame, target_count: int = 500) -> pd.DataFrame:
    """Select a diverse set of ICs based on categories and scores"""
    # Categorize all ICs
    categories_scores = df.apply(categorize_ic, axis=1)
    df["category"] = categories_scores.apply(lambda x: x[0])
    df["score"] = categories_scores.apply(lambda x: x[1])

    # Remove boring categories
    df = df[df["category"] != "boring"]

    # Remove duplicates
    df = remove_duplicates(df)

    # Sort by score (highest first)
    df = df.sort_values("score", ascending=False)

    # Ensure diversity by limiting per category
    selected = []
    category_counts = {}
    max_per_category = (
        target_count // len(INTERESTING_CATEGORIES) * 2
    )  # Allow some flexibility

    for _, row in df.iterrows():
        category = row["category"]
        if category not in category_counts:
            category_counts[category] = 0

        if category_counts[category] < max_per_category:
            selected.append(row)
            category_counts[category] += 1

            if len(selected) >= target_count:
                break

    # If we haven't reached target, add more high-scoring items
    if len(selected) < target_count:
        remaining = df[~df.index.isin([r.name for r in selected])]
        additional = remaining.head(target_count - len(selected))
        selected.extend(additional.itertuples(index=False, name=None))

    result_df = pd.DataFrame(selected)
    return result_df


def main():
    # Read the CSV file
    csv_file = "kicad_symbols_with_footprint_and_datasheet.csv"

    print("Loading KiCad symbols CSV...")
    df = pd.read_csv(csv_file)
    print(f"Total symbols loaded: {len(df)}")

    # Filter to only IC-like components (exclude passive components)
    # Simple heuristic: ICs usually have more complex descriptions and multiple pins
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
    ]
    for keyword in non_ic_keywords:
        df = df[~df["Description"].str.lower().str.contains(keyword, na=False)]

    print(f"Symbols after filtering non-ICs: {len(df)}")

    # Select interesting ICs
    print("\nSelecting interesting ICs that typically need passive components...")
    selected_df = select_diverse_set(df, target_count=500)

    print(f"\nSelected {len(selected_df)} interesting ICs")

    # Show category distribution
    print("\nCategory distribution:")
    category_counts = selected_df["category"].value_counts()
    for category, count in category_counts.items():
        print(f"  {category:<20} {count:>4} ICs")

    # Save to new CSV
    output_file = "data/selected_interesting_ics.csv"
    selected_df = selected_df.drop(
        columns=["category", "score"]
    )  # Remove helper columns
    selected_df.to_csv(output_file, index=False)
    print(f"\nSaved {len(selected_df)} selected ICs to {output_file}")

    # Show some examples
    print("\nExample selected ICs:")
    print("-" * 100)

    # Group examples by category for display
    selected_df["category"] = selected_df.apply(
        lambda row: categorize_ic(row)[0], axis=1
    )

    for category in ["adc", "dac", "amplifier", "regulator", "interface"]:
        cat_df = selected_df[selected_df["category"] == category].head(3)
        if not cat_df.empty:
            print(f"\n{category.upper()}:")
            for _, row in cat_df.iterrows():
                print(f"  {row['Symbol']:<25} - {row['Description'][:60]}...")


if __name__ == "__main__":
    main()
