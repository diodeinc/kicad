#!/usr/bin/env uv run
"""
Generate reference designs for all interesting ICs from selected_interesting_ics.csv
Final production version with progress tracking and summary reporting
"""

import csv
import os
import subprocess
import re
import time
from pathlib import Path
from datetime import datetime
import argparse
import random
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
import multiprocessing
from functools import partial
import shutil


def clean_mpn(symbol_name):
    """Extract a clean MPN from the symbol name"""
    # Remove any suffixes like -xXX, _XX, etc.
    mpn = re.sub(r"[-_]x[A-Z]+$", "", symbol_name)
    mpn = re.sub(r"[-_][A-Z]+$", "", mpn)
    # For complex names, take the base part
    if "x" in mpn:
        parts = mpn.split("x")
        if len(parts[0]) > 3:  # Likely the main part number
            mpn = parts[0]
    return mpn


def download_datasheet(url, output_path, mpn=None):
    """Download a datasheet from the given URL to the specified path"""
    if not url or url == "~" or url.strip() == "":
        return False

    try:
        # Use MPN as filename if provided, otherwise parse from URL
        if mpn:
            filename = f"{mpn}.pdf"
        else:
            # Fallback to URL filename if MPN not provided
            parsed_url = urllib.parse.urlparse(url)
            url_filename = os.path.basename(parsed_url.path)

            # If no filename in URL, use a default
            if not url_filename or not url_filename.endswith(".pdf"):
                url_filename = "datasheet.pdf"

            filename = url_filename

        # Full path for the datasheet
        datasheet_path = output_path / filename

        # Skip if already exists
        if datasheet_path.exists():
            print(f"  → Datasheet already exists: {filename}")
            return True

        print(f"  → Downloading datasheet from: {url}")

        # Set a user agent to avoid being blocked
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        request = urllib.request.Request(url, headers=headers)

        # Download with timeout
        with urllib.request.urlopen(request, timeout=30) as response:
            with open(datasheet_path, "wb") as f:
                f.write(response.read())

        # Validate it's actually a PDF
        if not is_valid_pdf(datasheet_path):
            print(f"  ✗ Downloaded file is not a valid PDF (might be HTML error page)")
            datasheet_path.unlink()  # Remove the invalid file
            return False

        print(f"  ✓ Downloaded datasheet: {filename}")
        return True

    except HTTPError as e:
        print(f"  ✗ HTTP Error {e.code} downloading datasheet")
        # Clean up partial download if it exists
        if "datasheet_path" in locals() and datasheet_path.exists():
            datasheet_path.unlink()
        return False
    except URLError as e:
        print(f"  ✗ URL Error downloading datasheet: {e.reason}")
        # Clean up partial download if it exists
        if "datasheet_path" in locals() and datasheet_path.exists():
            datasheet_path.unlink()
        return False
    except Exception as e:
        print(f"  ✗ Error downloading datasheet: {str(e)}")
        # Clean up partial download if it exists
        if "datasheet_path" in locals() and datasheet_path.exists():
            datasheet_path.unlink()
        return False


def scan_datasheet_to_markdown(pdf_path, output_dir):
    """Run pcb pro scan to convert datasheet PDF to markdown"""
    try:
        # Ensure pdf_path is a Path object
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            print(f"  ✗ PDF not found for scanning: {pdf_path}")
            return False

        # Check if markdown already exists
        md_path = output_dir / f"{pdf_path.stem}.md"
        if md_path.exists():
            print(f"  → Markdown already exists: {md_path.name}")
            return True

        print(f"  → Scanning datasheet to markdown: {pdf_path.name}")

        # Run pcb pro scan
        result = subprocess.run(
            ["pcb", "pro", "scan", "-p", str(pdf_path.parent)],
            capture_output=True,
            text=True,
            timeout=60,  # Give it 60 seconds to process
        )

        if result.returncode == 0:
            print(f"  ✓ Generated markdown: {md_path.name}")
            return True
        else:
            print(f"  ✗ Failed to scan datasheet: {result.stderr.strip()}")
            return False

    except subprocess.TimeoutExpired:
        print(f"  ✗ Scan timeout - datasheet might be too large")
        return False
    except FileNotFoundError:
        print(f"  ✗ pcb pro command not available")
        return False
    except Exception as e:
        print(f"  ✗ Error scanning datasheet: {str(e)}")
        return False


def cleanup_failed_directory(dir_path):
    """Remove a directory and all its contents if processing failed"""
    try:
        if dir_path.exists():
            # Use shutil.rmtree for robust directory removal
            shutil.rmtree(dir_path)
            print(f"  ✗ Cleaned up failed directory: {dir_path.name}")
        return True
    except Exception as e:
        print(f"  ✗ Failed to clean up directory {dir_path}: {str(e)}")
        return False


def is_valid_pdf(file_path):
    """Check if a file is a valid PDF by examining its header"""
    try:
        with open(file_path, "rb") as f:
            header = f.read(5)
            # PDF files start with %PDF-
            return header == b"%PDF-"
    except Exception:
        return False


def validate_component_directory(
    dir_path, download_datasheets=True, scan_datasheets=True, check_all_files=True
):
    """Validate that a component directory has all expected files

    Args:
        dir_path: Path to the component directory
        download_datasheets: Whether datasheets should be present
        scan_datasheets: Whether markdown files should be present
        check_all_files: If True, check all files. If False, only check .zen file exists
    """
    if not dir_path.exists():
        return False, "Directory does not exist"

    component_name = dir_path.name

    # Check for required .zen file
    zen_file = dir_path / f"{component_name}.zen"
    if not zen_file.exists():
        return False, "Missing .zen file"

    # If we're only checking basic validity (for existing components), stop here
    if not check_all_files:
        return True, "Valid"

    # Check for PDF if downloads are enabled
    if download_datasheets:
        pdf_file = dir_path / f"{component_name}.pdf"
        if not pdf_file.exists():
            return False, "Missing PDF datasheet"

        # Validate it's actually a PDF
        if not is_valid_pdf(pdf_file):
            return False, "Invalid PDF file (might be HTML error page)"

        # Check for markdown if scans are enabled
        # Note: We're more lenient here - if scan fails, we don't fail the whole component
        if scan_datasheets:
            md_file = dir_path / f"{component_name}.md"
            # Only warn about missing markdown, don't fail
            if not md_file.exists():
                print(
                    f"  ⚠ Warning: Markdown file not generated (scan may have failed)"
                )

    return True, "Valid"


def extract_pin_names_from_error(error_message):
    """Extract pin names from the build error message"""
    # Look for "Unconnected pin(s): pin1, pin2, ..."
    match = re.search(r"Unconnected pin\(s\): (.+?)(?:\n|$)", error_message)
    if match:
        pins_str = match.group(1)
        # Split by comma and clean up
        pins = [pin.strip() for pin in pins_str.split(",")]
        return pins

    # Also look for "expected one of: pin1, pin2, ..." pattern
    match = re.search(r"expected one of: (.+?)\)\)", error_message, re.DOTALL)
    if match:
        pins_str = match.group(1)
        # Clean up and split the pins
        pins = [pin.strip() for pin in pins_str.replace("\n", " ").split(",")]
        return pins

    return []


def generate_zen_file(ic_data, output_path, pin_names=None):
    """Generate a .zen file for the IC"""

    mpn = ic_data["Symbol"]
    clean_name = clean_mpn(mpn)
    library = ic_data["Library"]
    footprint = ic_data["Footprint"]
    description = ic_data["Description"]

    # Parse footprint path
    footprint_parts = footprint.split(":")
    if len(footprint_parts) == 2:
        footprint_lib, footprint_name = footprint_parts
        footprint_path = (
            f"@kicad-footprints/{footprint_lib}.pretty/{footprint_name}.kicad_mod"
        )
    else:
        footprint_path = f"@kicad-footprints/{footprint}"

    # Generate pin mappings
    if pin_names:
        # Use actual pin names
        pins_lines = []
        for i, pin in enumerate(pin_names):
            # Clean the pin name
            pin_clean = pin.strip()
            # Create a net name from the pin name (remove special chars)
            net_name = re.sub(r"[~{}]", "", pin_clean)
            net_name = net_name.replace("_{", "_").replace("}", "")

            # Add comma except for last pin
            comma = "," if i < len(pin_names) - 1 else ""
            pins_lines.append(f'        "{pin_clean}": Net("{net_name}"){comma}')

        pins_section = "\n".join(pins_lines)
    else:
        # Use a dummy pin to trigger the error message
        pins_section = '        "DUMMY_PIN": Net("DUMMY")'

    zen_content = f"""# {description}
Component(
    name = "{clean_name}",
    symbol = Symbol(library = "@kicad-symbols/{library}.kicad_sym", name = "{mpn}"),
    footprint = File("{footprint_path}"),
    pins = {{
{pins_section}
    }},
)
"""

    with open(output_path, "w") as f:
        f.write(zen_content)

    return zen_content


def run_pcb_build(zen_file_path):
    """Run pcb build to verify the generated file"""
    try:
        result = subprocess.run(
            ["pcb", "build", str(zen_file_path)],
            capture_output=True,
            text=True,
            timeout=10,
        )

        return result
    except subprocess.TimeoutExpired:
        return None
    except FileNotFoundError:
        return None
    except Exception:
        return None


def process_ic(
    ic_data,
    ic_number,
    total_ics,
    skip_existing=True,
    download_datasheets=True,
    scan_datasheets=True,
    output_folder="parts",
):
    """Process a single IC, attempting to extract pin names if initial build fails"""
    mpn = ic_data["Symbol"]
    clean_name = clean_mpn(mpn)

    # Check if already exists - now in specified output directory
    dir_path = Path(output_folder) / clean_name
    zen_file_path = dir_path / f"{clean_name}.zen"

    if skip_existing and zen_file_path.exists():
        # Try a quick build to see if it's valid
        result = run_pcb_build(zen_file_path)
        if result and result.returncode == 0:
            print(
                f"[{ic_number}/{total_ics}] {mpn} - Already exists and builds successfully, skipping..."
            )
            # Still try to download datasheet if enabled and missing
            if download_datasheets and "Datasheet" in ic_data:
                if download_datasheet(ic_data["Datasheet"], dir_path, clean_name):
                    # Scan to markdown if enabled
                    if scan_datasheets:
                        scan_datasheet_to_markdown(
                            dir_path / f"{clean_name}.pdf", dir_path
                        )
            return "skipped"

    print(f"\n[{ic_number}/{total_ics}] Processing {mpn} ({clean_name})...")

    # Track if this is a new component
    is_new_component = not dir_path.exists()

    # Create directory (including output parent if needed)
    dir_path.mkdir(parents=True, exist_ok=True)

    # Track result
    build_success = False

    # Download datasheet if enabled
    if download_datasheets and "Datasheet" in ic_data:
        if download_datasheet(ic_data["Datasheet"], dir_path, clean_name):
            # Scan to markdown if enabled
            if scan_datasheets:
                scan_datasheet_to_markdown(dir_path / f"{clean_name}.pdf", dir_path)

    # First attempt with dummy pin to get pin list
    generate_zen_file(ic_data, zen_file_path)

    # Try to build
    result = run_pcb_build(zen_file_path)

    if result is None:
        print(f"  ⚠ pcb command not available or error occurred")
    elif result.returncode == 0:
        print(f"  ✓ Build successful")
        build_success = True
    elif "not found in library" in result.stderr:
        print(f"  ✗ Symbol '{mpn}' not found in library '{ic_data['Library']}'")
        # Clean up immediately for symbol not found
        cleanup_failed_directory(dir_path)
        return "symbol_not_found"
    else:
        # Extract pin names from error
        pin_names = extract_pin_names_from_error(result.stderr)

        if pin_names:
            print(f"  Extracted {len(pin_names)} pin names")

            # Regenerate with actual pins
            generate_zen_file(ic_data, zen_file_path, pin_names)

            # Try building again
            result2 = run_pcb_build(zen_file_path)

            if result2 and result2.returncode == 0:
                print(f"  ✓ Build successful after regeneration")
                build_success = True
            else:
                print(f"  ✗ Build still failed after regeneration")
        else:
            print(f"  ✗ Build failed - couldn't extract pin names")

    # Validate the component directory
    is_valid, reason = validate_component_directory(
        dir_path,
        download_datasheets,
        scan_datasheets,
        check_all_files=is_new_component,  # Only do full validation for new components
    )

    if not is_valid:
        print(f"  ✗ Validation failed: {reason}")
        cleanup_failed_directory(dir_path)
        return False

    return build_success


def process_ic_wrapper(args):
    """Wrapper function for multiprocessing that unpacks arguments and handles exceptions"""
    (
        ic_data,
        ic_number,
        total_ics,
        skip_existing,
        download_datasheets,
        scan_datasheets,
        output_folder,
    ) = args

    try:
        result = process_ic(
            ic_data,
            ic_number,
            total_ics,
            skip_existing,
            download_datasheets,
            scan_datasheets,
            output_folder,
        )
        return (ic_data, result, None)
    except Exception as e:
        # Return the exception so we can handle it in the main thread
        return (ic_data, False, str(e))


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Generate reference designs for interesting ICs"
    )
    parser.add_argument(
        "-d",
        "--database",
        type=str,
        default="scripts/data/selected_interesting_ics.csv",
        help="Path to the CSV database file (default: scripts/data/selected_interesting_ics.csv)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="parts",
        help="Output folder for generated components (default: parts)",
    )
    parser.add_argument(
        "-n", "--count", type=int, help="Number of ICs to process (default: all)"
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=42,
        help="Random seed for deterministic subset selection (default: 42)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip ICs that already have valid .zen files (default: True)",
    )
    parser.add_argument(
        "--no-skip-existing",
        dest="skip_existing",
        action="store_false",
        help="Process all ICs even if they already exist",
    )
    parser.add_argument(
        "--download-datasheets",
        action="store_true",
        default=True,
        help="Download datasheets for components (default: True)",
    )
    parser.add_argument(
        "--no-download-datasheets",
        dest="download_datasheets",
        action="store_false",
        help="Skip downloading datasheets",
    )
    parser.add_argument(
        "--scan-datasheets",
        action="store_true",
        default=True,
        help="Scan datasheets to markdown using pcb pro scan (default: True)",
    )
    parser.add_argument(
        "--no-scan-datasheets",
        dest="scan_datasheets",
        action="store_false",
        help="Skip scanning datasheets to markdown",
    )
    parser.add_argument(
        "-b",
        "--batch-size",
        type=int,
        default=16,
        help="Number of ICs to process in parallel (default: 16)",
    )

    args = parser.parse_args()

    csv_file = args.database
    output_folder = args.output

    if not os.path.exists(csv_file):
        print(f"Error: Database file '{csv_file}' not found!")
        return

    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Read all ICs from CSV
    all_ics = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        all_ics = list(reader)

    total_available = len(all_ics)

    # Apply deterministic subset selection if count is specified
    if args.count and args.count < total_available:
        # Set random seed for reproducibility
        random.seed(args.seed)
        # Shuffle the list deterministically
        random.shuffle(all_ics)
        # Take the first n items
        all_ics = all_ics[: args.count]
        print(
            f"Selected {args.count} ICs from {total_available} total (seed: {args.seed})"
        )

    total_count = len(all_ics)

    # Configuration from args
    skip_existing = args.skip_existing
    download_datasheets = args.download_datasheets
    scan_datasheets = args.scan_datasheets

    # Tracking
    successful_builds = 0
    failed_builds = 0
    skipped = 0
    symbol_not_found = 0
    total_ics = 0

    start_time = time.time()

    print(f"Processing {total_count} ICs from {csv_file}")
    print(f"Output folder: {output_folder}")
    print(f"Skip existing: {skip_existing}")
    print(f"Download datasheets: {download_datasheets}")
    print(f"Scan datasheets to markdown: {scan_datasheets}")
    print("-" * 60)

    # Create a summary file
    summary_file = f"scripts/data/reference_designs_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    summary_lines = []

    # Process ICs in batches
    batch_size = args.batch_size
    num_workers = min(multiprocessing.cpu_count(), batch_size)

    print(f"Using {num_workers} parallel workers with batch size {batch_size}")
    print("-" * 60)

    for batch_start in range(0, total_count, batch_size):
        batch_end = min(batch_start + batch_size, total_count)
        batch_ics = all_ics[batch_start:batch_end]

        print(f"\nProcessing batch {batch_start + 1}-{batch_end} of {total_count}")

        # Prepare arguments for each IC in the batch
        batch_args = []
        for i, ic_data in enumerate(batch_ics):
            ic_number = batch_start + i + 1
            batch_args.append(
                (
                    ic_data,
                    ic_number,
                    total_count,
                    skip_existing,
                    download_datasheets,
                    scan_datasheets,
                    output_folder,
                )
            )

        # Process batch in parallel
        with multiprocessing.Pool(processes=num_workers) as pool:
            results = pool.map(process_ic_wrapper, batch_args)

        # Process results
        for ic_data, result, error_msg in results:
            total_ics += 1

            if error_msg:
                print(f"Error processing {ic_data['Symbol']}: {error_msg}")
                failed_builds += 1
                summary_lines.append(
                    f"Error processing {ic_data['Symbol']}: {error_msg}"
                )
            elif result == "skipped":
                skipped += 1
            elif result == "symbol_not_found":
                symbol_not_found += 1
                summary_lines.append(
                    f"Symbol not found: {ic_data['Symbol']} in {ic_data['Library']}"
                )
            elif result is True:
                successful_builds += 1
            elif result is False:
                failed_builds += 1
                summary_lines.append(f"Build failed: {ic_data['Symbol']}")

        # Progress update after each batch
        elapsed = time.time() - start_time
        if elapsed > 0:
            rate = total_ics / elapsed
            eta = (total_count - total_ics) / rate if rate > 0 else 0
            print(
                f"\n--- Batch complete: {total_ics}/{total_count} ({total_ics/total_count*100:.1f}%) - ETA: {eta/60:.1f} min ---"
            )

    # Final summary
    elapsed_total = time.time() - start_time

    # Calculate success rate, avoiding division by zero
    total_processed = successful_builds + failed_builds + symbol_not_found
    if total_processed > 0:
        success_rate = successful_builds / total_processed * 100
        success_rate_str = f"{success_rate:.1f}%"
    else:
        success_rate_str = "N/A (all skipped)"

    summary = f"""
============================================================
FINAL SUMMARY
============================================================
Database: {csv_file}
Output folder: {output_folder}
Total ICs processed: {total_ics}
Successful builds: {successful_builds}
Failed builds: {failed_builds}
Symbol not found: {symbol_not_found}
Skipped (existing): {skipped}
Total time: {elapsed_total/60:.1f} minutes
Success rate: {success_rate_str} (excluding skipped)
Download datasheets: {download_datasheets}
Scan datasheets to markdown: {scan_datasheets}
Batch size: {batch_size} (using {num_workers} workers)
Random seed: {args.seed if args.count else 'N/A'}
============================================================
"""

    print(summary)

    # Write summary file
    with open(summary_file, "w") as f:
        f.write(summary)
        if summary_lines:
            f.write("\nDETAILS:\n")
            f.write("\n".join(summary_lines))

    print(f"Summary saved to: {summary_file}")

    if successful_builds > 0:
        print(f"\n✓ Successfully generated {successful_builds} reference designs!")
        print("  The .zen files with correct pin mappings are ready to use.")


if __name__ == "__main__":
    main()
