# Human Natural Structure (HNS)
**The Operating Structure for Human Cognition — A Foundation for Alignment**  
**S. Hara | Natural Structure Works**

---

## Why HNS Exists

AI systems generate language statistically. They have no structural model of what a human means, intends, or values.

The result is a class of failures that conventional hallucination research does not capture — not wrong facts, but **structurally mispositioned reasoning**.

HNS calls these **structural hallucinations**. It classifies them. And it solves them.

---

## HNS Structural Hallucination Taxonomy

Five recurring failure modes, identified and validated across a 50-Turn blinded PoC:

| # | Type | What Goes Wrong |
|---|------|-----------------|
| 1 | **Layer Jump** | Skips across meaning layers without an explicit bridge |
| 2 | **Category Ambiguity** | Conflates cognitive, emotional, and intentional categories |
| 3 | **Scope Drift** | Departs from the user's intended structural scope |
| 4 | **Metaphor Contamination** | Metaphorical expressions distort structural coordinates |
| 5 | **Unsupported Causality** | Causal claims without a layer-grounded mechanism |

These are not surface errors. They are structural failures — and they are systematic.

**50-Turn PoC Result (May 2026):** Structural errors reduced from 31 → 0 under HNS constraint condition.

→ [Full Taxonomy Report](./08-Reports/HNS_Structural_Hallucination_Taxonomy.md)

---

## What HNS Is

If structural hallucination is the problem, HNS is the structural layer that solves it.

HNS provides a formal coordinate system for human cognition — a hierarchical OS that gives AI systems a stable reference for understanding what humans mean, intend, and value.

**Three levels of resolution:**

- **HNS-36** — The minimal structure for human meaning generation
- **HNS-144** — Extended causal structure built upon HNS-36
- **HNS-864** — Full deployment covering behavior, cognition, and social structures

This layered architecture allows human thought, action, and meaning to be positioned with the same precision that an operating system uses to manage processes.

→ **[HNS Strategic Roadmap v1.1](./07-Strategy/HNS-Strategic-Roadmap-v1.1.md)** — The complete overview and four-phase strategy

---

## EVA (External Verification Architecture)

HNS reasoning is externally verifiable through **EVA** — an independent architecture that validates AI outputs against human-structured coordinates without accessing internal model weights.

EVA provides structural audit trails compatible with EU AI Act / ISO 42001 requirements.

---

## Path to Standardization

HNS is designed for future standardization under CEN/CENELEC and ISO/IEC JTC1/SC42.

---

## HNS-36 Python Package

The first implementation of HNS-36 as a Python library.

- **Location:** `01-Docs/05-Implementations/hns36_pkg/`
- **Tests:** 19/19 passing
- **Core functions:**
  - `hns36.analyze(text)` — detect structural hallucinations in AI responses
  - `hns36.constrain(question)` — generate HNS-36 constrained response
  - `hns36.compare(question, a, b)` — blind structural comparison
- **Install:** `pip install anthropic` → `pip install -e 01-Docs/05-Implementations/hns36_pkg`

---

## Repository Structure

- **01-Docs** — Foundational concepts and definitions
  - **05-Implementations** — Python package (hns36)
- **02-Papers** — Theoretical papers and reflections
- **03-Books** — Complete HNS Series (19 volumes with ISBN)
- **07-Strategy** — Strategic documents for HNS and EVA
- **08-Reports** — PoC and implementation reports

---

## Where to Start

1. **Curious about the problem?** → [HNS Structural Hallucination Taxonomy](./08-Reports/HNS_Structural_Hallucination_Taxonomy.md)
2. **Want the full picture?** → [HNS Strategic Roadmap v1.1](./07-Strategy/HNS-Strategic-Roadmap-v1.1.md)
3. **Ready to implement?** → HNS-36 Python Package above

---

**HNS is the structural foundation for human–AI alignment.**

**Natural Structure Works**  
© 2026 S. Hara. All rights reserved.
