# KiCad reference designs

A repository of configurable modules that expand on top of the KiCad standard library.

The modules can be configured with the zener visualizer tool and directly copy pasted into KiCad

## Updating the package index

To update `pcb.toml` with all available packages:

```bash
find . -name "*.zen" -not -path "*/.pcb/*" -not -path "./staging/*" | sort | while read f; do echo "$(basename "$f" .zen) = \"${f#./}\""; done > pcb.toml
```
