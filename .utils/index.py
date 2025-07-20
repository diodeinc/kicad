#!/usr/bin/env uv run
import re
import sys
from pathlib import Path

"""Utility script to regenerate `pcb.toml` workspace index from metadata
embedded in each *.zen file.

Usage::

    python utils/index.py [ROOT]

If *ROOT* is omitted the script assumes it is executed from the workspace root
(the directory that contains ``pcb.toml``) and uses ``Path.cwd()``.

The script looks for all ``*.zen`` files underneath *ROOT* (recursively) and
extracts the following metadata:

* name:  Component name (first token before the dash in the docstring title)
* description:  Short description (portion after the dash in the docstring
  title, or the second line of the docstring if no dash is present)
* datasheet:  URL found after a line starting with "Datasheet:" inside the
  docstring.
* category:  The first-level directory name that contains the *.zen* file (for
  instance ``Analog_ADC`` for ``Analog_ADC/AD7171.zen``).
* path:  The relative path to the zen file from *ROOT* converted to POSIX
  notation.

With this information an output ``pcb.toml`` file is generated that mirrors the
format already used in the repository::

    [workspace]

    [[workspace.AD7171]]
    name = "AD7171"
    path = "Analog_ADC/AD7171.zen"
    category = "Analog_ADC"
    description = "16-Bit Sigma-Delta ADC with SPI Interface"
    datasheet = "https://www.analog.com/media/en/technical-documentation/data-sheets/AD7171.pdf"

Sections are emitted in alphabetical order by *category* then *name* to provide
stable diffs.
"""

DOCSTRING_RE = re.compile(r'^"""(.*?)"""', re.DOTALL)


class ComponentMetadata(dict):
    """Simple mapping subclass with helpers for TOML output."""

    def toml(self) -> str:
        lines = [f"[[workspace.{self['name'].replace('-', '_')}]]"]
        for key in (
            "name",
            "path",
            "category",
            "description",
            "datasheet",
        ):
            if key in self and self[key]:
                value = self[key].replace('"', '\\"')
                lines.append(f'{key} = "{value}"')
        return "\n".join(lines) + "\n"


def parse_zen(zen_path: Path, root: Path) -> ComponentMetadata | None:
    """Extract metadata from a single *.zen* file.

    Returns *None* if required fields cannot be extracted.
    """
    rel_path = zen_path.relative_to(root).as_posix()
    category = rel_path.split("/", 1)[0]

    text = zen_path.read_text(encoding="utf-8", errors="replace")

    doc_match = DOCSTRING_RE.search(text)
    if not doc_match:
        return None  # No top-level docstring – skip

    doc = doc_match.group(1).strip().splitlines()
    if not doc:
        return None

    # First line may be "NAME - description"
    first_line = doc[0].strip()
    if " - " in first_line:
        name, description = [part.strip() for part in first_line.split(" - ", 1)]
    else:
        name = first_line.strip()
        description = doc[1].strip() if len(doc) > 1 else ""

    datasheet = ""
    for line in doc:
        if line.lower().startswith("datasheet:"):
            datasheet = line.split(":", 1)[1].strip()
            break

    return ComponentMetadata(
        name=name,
        path=rel_path,
        category=category,
        description=description,
        datasheet=datasheet,
    )


def collect_components(root: Path) -> list[ComponentMetadata]:
    comps: list[ComponentMetadata] = []
    for zen_path in root.rglob("*.zen"):
        meta = parse_zen(zen_path, root)
        if meta:
            comps.append(meta)
    # Sort for stable output
    return sorted(comps, key=lambda m: (m["category"], m["name"].upper()))


def build_toml(components: list[ComponentMetadata]) -> str:
    lines = ["[workspace]\n"]
    for comp in components:
        lines.append(comp.toml())
        lines.append("")  # blank line between entries for readability
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> None:
    argv = argv or sys.argv[1:]
    root = Path(argv[0]).resolve() if argv else Path.cwd().resolve()

    pcb_toml = root / "pcb.toml"
    if not pcb_toml.exists():
        print(f"error: {pcb_toml} not found", file=sys.stderr)
        sys.exit(1)

    components = collect_components(root)
    toml_text = build_toml(components)

    pcb_toml.write_text(toml_text, encoding="utf-8")
    print(f"Updated {pcb_toml} with {len(components)} components.")


if __name__ == "__main__":
    main()
