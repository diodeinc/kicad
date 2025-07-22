<p align="center">
  <a href="https://github.com/diodeinc/kicad/actions/workflows/ci.yaml">
    <img src="https://github.com/diodeinc/kicad/actions/workflows/ci.yaml/badge.svg" alt="CI">
  </a>
</p>

# KiCad reference designs

A repository of configurable modules that expand on top of the KiCad standard library.

This work is made possible by the open-source **Zener compiler** and its accompanying **standard library**:

- 🛠️ [diodeinc/pcb – Zener compiler](https://github.com/diodeinc/pcb)
- 📚 [diodeinc/stdlib – Zener standard library](https://github.com/diodeinc/stdlib)

If you're new to Zener, start by installing the compiler and browsing the standard library to build and customize these reference designs.

The modules can be configured with the Zener visualizer tool and directly copy-pasted into KiCad.

## Updating the package index

To update `pcb.toml` with all available packages:

```bash
.utils/index.py
```
