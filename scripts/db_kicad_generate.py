#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

import os
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple


class KiCadSymbolParser:
    """Parser for KiCad symbol library files (.kicad_sym)"""

    def __init__(self, symbol_lib_path: str):
        self.symbol_lib_path = Path(symbol_lib_path)

    def parse_symbol_properties(self, symbol_content: str) -> Dict[str, Optional[str]]:
        """Extract properties from a symbol definition"""
        properties = {
            "name": None,
            "footprint": None,
            "datasheet": None,
            "description": None,
            "value": None,
        }

        # Extract symbol name
        name_match = re.search(
            r'^\s*\(symbol\s+"([^"]+)"', symbol_content, re.MULTILINE
        )
        if name_match:
            properties["name"] = name_match.group(1)

        # Extract properties using a more robust pattern
        # Looking for (property "PropertyName" "PropertyValue" ...)
        property_pattern = r'\(property\s+"(\w+)"\s+"([^"]*)"'

        for match in re.finditer(property_pattern, symbol_content):
            prop_name = match.group(1).lower()
            prop_value = match.group(2)

            if prop_name == "footprint" and prop_value:
                properties["footprint"] = prop_value
            elif prop_name == "datasheet" and prop_value:
                properties["datasheet"] = prop_value
            elif prop_name == "description" and prop_value:
                properties["description"] = prop_value
            elif prop_name == "value" and prop_value:
                properties["value"] = prop_value

        return properties

    def extract_symbols_from_file(
        self, file_path: Path
    ) -> List[Dict[str, Optional[str]]]:
        """Extract all symbols from a .kicad_sym file"""
        symbols = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Split content into individual symbol definitions
            # Each symbol starts with (symbol and we need to handle nested parentheses
            symbol_starts = []
            paren_count = 0
            in_symbol = False
            current_symbol_start = 0

            i = 0
            while i < len(content):
                if i < len(content) - 7 and content[i : i + 7] == "(symbol":
                    if not in_symbol:
                        in_symbol = True
                        current_symbol_start = i
                        paren_count = 0

                if in_symbol:
                    if content[i] == "(":
                        paren_count += 1
                    elif content[i] == ")":
                        paren_count -= 1

                        if paren_count == 0:
                            # Found the end of a symbol
                            symbol_content = content[current_symbol_start : i + 1]
                            properties = self.parse_symbol_properties(symbol_content)
                            if properties[
                                "name"
                            ]:  # Only add if we successfully parsed a name
                                properties["library"] = file_path.stem
                                symbols.append(properties)
                            in_symbol = False

                i += 1

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

        return symbols

    def scan_all_libraries(self) -> List[Dict[str, Optional[str]]]:
        """Scan all .kicad_sym files in the symbol library path"""
        all_symbols = []

        if not self.symbol_lib_path.exists():
            print(f"Error: Symbol library path does not exist: {self.symbol_lib_path}")
            return all_symbols

        # Get all .kicad_sym files
        kicad_sym_files = list(self.symbol_lib_path.glob("*.kicad_sym"))

        print(f"Found {len(kicad_sym_files)} symbol library files")

        for i, sym_file in enumerate(kicad_sym_files, 1):
            print(f"Processing {i}/{len(kicad_sym_files)}: {sym_file.name}")
            symbols = self.extract_symbols_from_file(sym_file)
            all_symbols.extend(symbols)

        return all_symbols

    def filter_symbols_with_footprint_and_datasheet(
        self, symbols: List[Dict[str, Optional[str]]]
    ) -> List[Dict[str, Optional[str]]]:
        """Filter symbols that have both a dedicated footprint and a datasheet"""
        filtered = []

        for symbol in symbols:
            # Check if both footprint and datasheet are present and not empty
            if (
                symbol.get("footprint")
                and symbol["footprint"].strip()
                and symbol.get("datasheet")
                and symbol["datasheet"].strip()
                and symbol["datasheet"].lower() not in ["~", ""]
            ):
                filtered.append(symbol)

        return filtered


def main():
    # KiCad symbol library path on macOS
    kicad_symbols_path = "/Applications/KiCad/KiCad.app/Contents/SharedSupport/symbols"

    print("KiCad Symbol Library Scanner")
    print("=" * 50)
    print(f"Scanning path: {kicad_symbols_path}")
    print()

    # Create parser and scan libraries
    parser = KiCadSymbolParser(kicad_symbols_path)
    all_symbols = parser.scan_all_libraries()

    print(f"\nTotal symbols found: {len(all_symbols)}")

    # Filter symbols with both footprint and datasheet
    filtered_symbols = parser.filter_symbols_with_footprint_and_datasheet(all_symbols)

    print(f"Symbols with both footprint and datasheet: {len(filtered_symbols)}")
    print()

    # Display results
    if filtered_symbols:
        print("Found symbols with dedicated footprint and datasheet:")
        print("-" * 100)
        print(f"{'Library':<25} {'Symbol':<30} {'Footprint':<40} {'Datasheet'}")
        print("-" * 100)

        # Sort by library and symbol name
        filtered_symbols.sort(key=lambda x: (x.get("library", ""), x.get("name", "")))

        # Limit output for readability
        max_display = 50
        for i, symbol in enumerate(filtered_symbols[:max_display]):
            library = symbol.get("library", "Unknown")
            name = symbol.get("name", "Unknown")
            footprint = symbol.get("footprint", "")[:40]  # Truncate for display
            datasheet = symbol.get("datasheet", "")

            # Truncate long datasheets for display
            if len(datasheet) > 60:
                datasheet = datasheet[:57] + "..."

            print(f"{library:<25} {name:<30} {footprint:<40} {datasheet}")

        if len(filtered_symbols) > max_display:
            print(f"\n... and {len(filtered_symbols) - max_display} more symbols")

        # Summary by library
        print("\n" + "=" * 50)
        print("Summary by library:")
        print("-" * 50)

        library_counts = {}
        for symbol in filtered_symbols:
            lib = symbol.get("library", "Unknown")
            library_counts[lib] = library_counts.get(lib, 0) + 1

        for lib, count in sorted(
            library_counts.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"{lib:<30} {count:>5} symbols")

        # Export option
        print("\n" + "=" * 50)
        export_file = "data/kicad_symbols_with_footprint_and_datasheet.csv"
        print(f"Exporting results to: {export_file}")

        with open(export_file, "w", encoding="utf-8") as f:
            # Write CSV header
            f.write("Library,Symbol,Value,Description,Footprint,Datasheet\n")

            # Write data
            for symbol in filtered_symbols:
                library = symbol.get("library", "")
                name = symbol.get("name", "")
                value = symbol.get("value", "")
                description = symbol.get("description", "").replace('"', '""')
                footprint = symbol.get("footprint", "")
                datasheet = symbol.get("datasheet", "")

                f.write(
                    f'"{library}","{name}","{value}","{description}","{footprint}","{datasheet}"\n'
                )

        print(f"Export complete! Total {len(filtered_symbols)} symbols exported.")

    else:
        print("No symbols found with both footprint and datasheet.")


if __name__ == "__main__":
    main()
