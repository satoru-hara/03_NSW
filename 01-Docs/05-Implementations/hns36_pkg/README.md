# HNS-36

**Human Natural Structure — Structural Coordinate System for AI**

The world's first structural OS kernel for human-aligned AI.

[![DOI](https://img.shields.io/badge/DOI-10.2139%2Fssrn.6439661-blue)](https://doi.org/10.2139/ssrn.6439661)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

---

## What is HNS-36?

HNS-36 is a 36-cell coordinate system for positioning any human phenomenon, formed by:

- **6 Human Natural Layers** (causal strata): `L1 PhysicalOS` → `L2 CognitiveOS` → `L3 InteractionOS` → `L4 EnvironmentOS` → `L5 LoadOS` → `L6 PatternOS`
- **6 Abstract Cognitive Categories** (explanatory axes): `C1 Civilization` | `C2 Core` | `C3 Module` | `C4 Application` | `C5 System` | `C6 External`

This library provides:
1. **`analyze(text)`** — detect structural errors in AI responses
2. **`constrain(question)`** — generate structurally coherent responses
3. **`compare(question, a, b)`** — blind comparison of two responses
4. **`coordinate(text)`** — assign HNS-36 coordinates to a passage

---

## Empirical Evidence

The HNS-36 PoC experiment (50 turns, 5 cases, blind evaluation) showed:

| Condition | Structural Errors | Avg Stability |
|-----------|-------------------|---------------|
| Standard  | **37**            | 3.52 / 5      |
| HNS-36    | **0**             | 5.00 / 5      |

Intention Alignment difference: only −0.16 (content quality preserved).

Full data: [EVA-HNS Book](https://github.com/satoru-hara/03_NSW)

---

## Installation

```bash
pip install anthropic
# Then install this package:
git clone https://github.com/satoru-hara/03_NSW
pip install -e 03_NSW/hns36
```

Set your API key:
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

---

## Quick Start

```python
import hns36

# Explore the coordinate system (no API needed)
print(hns36.build_layer_reference())
print(hns36.get_cell("L3", "C5"))

# Detect structural errors in an AI response
result = hns36.analyze(
    text="The dopamine system causes exhaustion because it keeps the brain aroused.",
    question="Why do people feel tired after using social media?"
)
print(result.total_errors)          # 2
print(result.error_types)           # ['UnsupportedCausality', 'MetaphorContamination']
print(result.structural_stability)  # 3.0

# Generate a structurally constrained response
response = hns36.constrain(
    "Why does workplace burnout occur even in well-paid jobs?"
)
print(response)
# [Addressing L4 EnvironmentOS → L5 LoadOS → L3 InteractionOS]
# At L4 EnvironmentOS: ...

# Compare two responses (blind evaluation)
result = hns36.compare(
    question="Is burnout personal or organizational?",
    response_a=standard_response,
    response_b=hns_response,
    label_a="Standard",
    label_b="HNS-36",
)
print(result.summary())

# Assign HNS-36 coordinates
coord = hns36.coordinate("Cultural norms shape behavior across generations.")
print(coord)  # L6×C1 (PatternOS × Civilization)
```

---

## The 5 Structural Error Types

| Error | Definition |
|-------|------------|
| `LayerJump` | Moving across HNS layers without a bridge mechanism |
| `ScopeDrift` | Shifting individual → societal without intermediate step |
| `UnsupportedCausality` | Causal claim without a stated mechanism |
| `MetaphorContamination` | L1 Physical concept explains L3/L4 without bridge |
| `CategoryAmbiguity` | Causes, symptoms, effects treated as equivalent |

---

## HNS-36 Coordinate System

| Layer | Name | Domain |
|-------|------|--------|
| L1 | PhysicalOS | Physical and biological foundations |
| L2 | CognitiveOS | Perception, memory, internal processing |
| L3 | InteractionOS | Human-to-human and human-to-environment |
| L4 | EnvironmentOS | Physical, social, institutional environments |
| L5 | LoadOS | Internal and external loads, pressures |
| L6 | PatternOS | Emergent patterns and long-term regularities |

| Category | Name | Role |
|----------|------|------|
| C1 | Civilization | Macro-scale, civilizational framing |
| C2 | Core | Foundational principles |
| C3 | Module | Components and functional units |
| C4 | Application | Practical uses |
| C5 | System | Organized systems |
| C6 | External | Outer contextual factors |

---

## Architecture

HNS-36 is the kernel layer of the EVA-HNS Full-Stack OS:

```
EVA  — External Verification Architecture (audit, safety)
SOHU — Structural OS for Human Understanding (OS layer)
HNS  — Human Natural Structure (kernel: this library)
```

---

## References

- Hara, S. (2026). *Human Natural Structure (HNS)*. SSRN. https://doi.org/10.2139/ssrn.6439661
- Hara, S. (2026). *Structural OS for Human Understanding (SOHU)*. SSRN / Zenodo.
- Hara, S. (2026). *EVA-HNS Structural Full-Stack OS*. KDP.
- Full specifications: https://github.com/satoru-hara/03_NSW

---

## License

CC BY 4.0 — Satoru Hara / Natural Structure Works (NSW)
