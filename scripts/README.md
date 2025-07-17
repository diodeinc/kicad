# Reference Design Generator for KiCad ICs

This project generates reference designs in `.zen` format for interesting ICs from the KiCad symbol libraries.

## Overview

The scripts automatically:

1. Read IC information from the CSV file
2. Create directory structure `<MPN>/<MPN>.zen`
3. Extract actual pin names from KiCad symbols (via build errors)
4. Generate `.zen` files with correct pin mappings
5. Verify builds using `pcb build`

## Scripts

### `generate_reference_designs.py`

- Basic version that generates files with generic pin templates
- Good for understanding the structure but requires manual pin mapping

### `generate_reference_designs_v2.py`

- Attempts to extract pin names from build errors
- Initial attempt at automation (limited success)

### `generate_reference_designs_v3.py`

- **Recommended for testing**
- Successfully extracts pin names from "Unconnected pin(s)" errors
- Processes first 10 ICs as a test
- 90% success rate in testing

### `generate_all_reference_designs.py`

- **Production version**
- Processes all 500+ ICs from the CSV
- Progress tracking and ETA
- Skips already processed ICs
- Generates summary report
- Handles symbol not found errors gracefully

### `ai_reference_design.py`

- **AI-powered version supporting multiple LLM providers**
- Supports latest models:
  - Anthropic: Claude Opus 4, Sonnet 4, Sonnet 3.7, Haiku 3.5
  - OpenAI: GPT-4o, O3, O1 reasoning models
  - Google: Gemini 2.5 Pro, Flash, and Flash Lite
- Generates complete reference designs with supporting components
- Uses an agentic workflow with iterative improvements
- Reads datasheet markdown content for context
- Includes proper docstrings with author and datasheet links
- Supports configuration options for flexible designs
- Automatically fixes build errors through multiple iterations
- Real-time streaming output shows generation progress with animated spinner
- Smart fallback for models that don't support streaming (e.g., OpenAI O1/O3 reasoning models)
- Automatic safety filter configuration for Gemini to enable code generation

### `benchmark_llm_providers.py`

- **Benchmark tool for comparing LLM providers**
- Tests success rate, speed, and quality across different models
- Measures API calls and time per design
- Generates detailed comparison reports
- Helps identify the best model for your use case

## Usage

### Test Run (10 ICs)

```bash
python3 generate_reference_designs_v3.py
```

### Process All ICs

```bash
python3 generate_all_reference_designs.py
```

### Generate with AI Models

```bash
# Set API keys (based on provider)
export ANTHROPIC_API_KEY="your-anthropic-key"
export OPENAI_API_KEY="your-openai-key"
export GOOGLE_API_KEY="your-google-key"

# List available models
./ai_reference_design.py --list-models

# Process single design (default)
./ai_reference_design.py

# Process multiple designs from a directory
./ai_reference_design.py --max-designs 5

# Process from a specific directory
./ai_reference_design.py --directory parts/simple --max-designs 3

# Random selection instead of alphabetical
./ai_reference_design.py --directory parts/interesting --max-designs 10 --random

# Process specific parts (backward compatible)
./ai_reference_design.py --parts AD7171 CC2500

# Process with specific provider
./ai_reference_design.py --provider openai --max-designs 2
./ai_reference_design.py --provider gemini --max-designs 2

# Use specific model
./generate_reference_designs.py --provider openai --model gpt-4o-mini
./generate_reference_designs.py --provider anthropic --model claude-opus-4-20250514
./generate_reference_designs.py --provider gemini --model gemini-2.5-flash

# Process specific parts
./generate_reference_designs.py --parts AD7171 LTC2299

# Adjust max iterations for error fixing
./generate_reference_designs.py --max-iterations 10

# Disable streaming output (useful for logging/debugging)
./generate_reference_designs.py --no-streaming
```

### Benchmark LLM Providers

```bash
# Run benchmark on default components
./benchmark_llm_providers.py

# Test specific components
./benchmark_llm_providers.py --components AD7171 MAX31913

# Test specific providers only
./benchmark_llm_providers.py --providers openai gemini

# Adjust max iterations for faster benchmarking
./benchmark_llm_providers.py --max-iterations 2
```

## Example Generated Files

### Basic Version (generate_all_reference_designs.py)

```zen
# High-Side, Current-Sense Amplifiers with 12-Bit ADC...
Component(
    name = "MAX9612",
    symbol = Symbol(library = "@kicad-symbols/Power_Management.kicad_sym", name = "MAX9612"),
    footprint = File("@kicad-footprints/Package_SO.pretty/MSOP-10_3x3mm_P0.5mm.kicad_mod"),
    pins = {
        "RS+": Net("RS+"),
        "RS-": Net("RS-"),
        "SET": Net("SET"),
        "V_{CC}": Net("V_CC"),
        "GND": Net("GND"),
        "OUT": Net("OUT"),
        "SDA": Net("SDA"),
        "SCL": Net("SCL"),
        "A0": Net("A0"),
        "A1": Net("A1")
    },
)
```

### AI-Generated Version (generate_reference_designs.py)

```zen
"""AD7171 ADC from Analog Devices

Author: @claude-opus-4-20250514  # or @gpt-4o, @gemini-2.5-pro, etc.
Datasheet: https://www.analog.com/media/en/technical-documentation/data-sheets/AD7171.pdf
"""

load("@stdlib/interfaces.zen", "Ground", "Spi")

# Dependencies
Resistor = Module("@stdlib/generics/Resistor.zen")
Capacitor = Module("@stdlib/generics/Capacitor.zen")

# Configuration
add_decoupling = config("decoupling", bool, default = True)
add_input_filter = config("input_filter", bool, default = True)

# External IO
VDD = io("VDD", Net, default = Net("VDD"))
GND = io("GND", Net, default = Net("GND"))
spi = io("SPI", Spi, default = Spi("SPI"))

# Main component
Component(
    name = "AD7171",
    symbol = Symbol(library = "@kicad-symbols/Analog_ADC.kicad_sym", name = "AD7171"),
    footprint = File("@kicad-footprints/Package_DFN_QFN.pretty/DFN-10-1EP_3x3mm_P0.5mm_EP1.55x2.48mm.kicad_mod"),
    pins = {
        "VDD": VDD,
        "GND": GND,
        # ... other pins ...
    },
)

# Supporting components
if add_decoupling:
    Capacitor(name = "C_DEC", value = "100nF", package = "0402", P1 = VDD, P2 = GND)
```

## How It Works

### Basic Version (generate_all_reference_designs.py)

1. **Initial Generation**: Creates a `.zen` file with a dummy pin
2. **Build Attempt**: Runs `pcb build` which fails with "Unconnected pin(s): ..."
3. **Pin Extraction**: Parses the error message to get actual pin names
4. **Regeneration**: Creates new `.zen` file with correct pins
5. **Verification**: Runs `pcb build` again to ensure success

### AI-Powered Version (generate_reference_designs.py)

1. **Context Loading**: Reads the markdown datasheet and example design (AD7171)
2. **Initial Generation**: The LLM creates a complete reference design with:
   - Proper docstring with author (model name) and datasheet link
   - All necessary imports and dependencies
   - Configuration options for flexibility
   - Main component with all pins
   - Supporting components (capacitors, resistors, etc.)
3. **Build & Iterate**: Runs `pcb build` and if it fails:
   - Feeds error message back to the LLM
   - LLM analyzes and fixes the issue
   - Process repeats up to max iterations
4. **Verification**: Ensures final design compiles successfully

## Features

- Automatic pin name extraction from KiCad symbols
- Progress tracking with ETA
- Skip already processed ICs
- Handle missing symbols gracefully
- Generate summary reports
- Clean net names (removes special characters)

## Requirements

- Python 3.6+
- `pcb` command available in PATH
- Access to KiCad symbol libraries (handled by pcb tool)

## Output Structure

```
kicad/
├── MAX9612/
│   └── MAX9612.zen
├── LTC1748/
│   └── LTC1748.zen
├── ADS8685RUM/
│   └── ADS8685RUM.zen
└── ... (one directory per IC)
```

## Summary Report

After processing, a summary file is generated with:

- Total ICs processed
- Success/failure counts
- Symbol not found errors
- Processing time
- Success rate

## Notes

- Some symbols may not be found in the KiCad libraries (e.g., ES8388)
- The script automatically cleans up failed attempts
- Net names are derived from pin names with special characters removed
- Each IC gets its own directory for potential future expansion

## Troubleshooting

### Gemini Safety Filter Errors

If you encounter errors like:

```
Gemini API error: Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason] is 2.
```

This means Gemini's safety filters blocked the response. The script automatically configures relaxed safety settings, but if issues persist:

1. **Try a different Gemini model**: `gemini-2.5-flash` may be less restrictive than `gemini-2.5-pro`

   ```bash
   ./generate_reference_designs.py --provider gemini --model gemini-2.5-flash
   ```

2. **Use a different provider temporarily**:

   ```bash
   ./generate_reference_designs.py --provider anthropic
   ./generate_reference_designs.py --provider openai
   ```

3. **Check if the component name or datasheet content might trigger filters** and try with a different component first
