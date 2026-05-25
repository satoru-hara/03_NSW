# Human Natural Structure (HNS)
**The Operating Structure for Human Cognition — A Foundation for Alignment**  
**S. Hara | Natural Structure Works**

---

## Overview

Human Natural Structure (HNS) is an **Operating Structure (OS)** designed to formally describe human cognition, behavior, and meaning generation in a structured, hierarchical manner.

**HNS enables structurally aligned reasoning, interpretable AI behavior, and human-consistent meaning generation.**

This repository shares the theory, design, and strategy of HNS in a progressive and open manner.

**[HNS Strategic Roadmap v1.1](./07-Strategy/HNS-Strategic-Roadmap-v1.1.md)**  
(The complete overview and four-phase strategy are available here)

---

## The Structural Misalignment HNS Solves

Current AI systems treat language as probabilistic token sequences. As a result, they inevitably encounter the following **structural failure modes**:

| Type | Description |
|------|-------------|
| **Layer Jump** | A response skips across meaning layers without an explicit bridge |
| **Category Ambiguity** | Cognitive, emotional, and intentional categories become conflated |
| **Metaphor Contamination** | Metaphorical or symbolic expressions distort the underlying structural coordinates |
| **Scope Drift** | The response structurally departs from the user's intended scope |
| **Unsupported Causality** | A causal claim is generated without a mechanism grounded in the layer hierarchy |

HNS addresses these issues at the structural level.  
→ See [HNS Structural Hallucination Taxonomy](./08-Reports/HNS_Structural_Hallucination_Taxonomy.md) for formal definitions and validation results.

---

## HNS Structure (36 → 144 → 864)

HNS is organized in the following hierarchical coordinate system:

- **HNS-36** — The minimal structure for human meaning generation
- **HNS-144** — Extended causal structure built upon HNS-36
- **HNS-864** — Full deployment covering behavior, cognition, and social structures

This layered architecture allows human thought, action, and meaning to be described in the same way an operating system manages processes.

---

## EVA (External Verification Architecture)

HNS is externally verifiable through **EVA** — the only architecture that allows AI outputs to be externally validated against a human-structured coordinate system.

This external verification dramatically improves AI transparency, safety, and explainability.

---

## HNS Structural Hallucination Taxonomy

A framework for classifying AI coherence violations as deviations from human cognitive structure (HNS-36), beyond conventional semantic hallucination categories.

**Five Types**

| Type | Description |
|------|-------------|
| **Layer Jump** | Skips meaning layers without an explicit bridge |
| **Category Ambiguity** | Conflates cognitive, emotional, and intentional categories |
| **Metaphor Contamination** | Metaphorical expressions distort structural coordinates |
| **Scope Drift** | Departs from the user's intended structural scope |
| **Unsupported Causality** | Causal claims without a layer-grounded mechanism |

**Initial Validation (50-Turn PoC, May 2026)**  
Structural errors: 31 → 0 under HNS constraint condition.  
*Note: Single-model evaluation; cross-model replication pending.*

→ [Full Report](./08-Reports/HNS_Structural_Hallucination_Taxonomy.md)

---

## Path to Standardization

HNS is designed with compatibility for future standardization under CEN/CENELEC and ISO/IEC JTC1/SC42.

---

## Repository Structure

- **01-Docs** — Foundational concepts and definitions
  - **05-Implementations** — Python package (hns36) — structural error detector
- **02-Papers** — Theoretical papers and reflections
- **03-Books** — Complete HNS Series (11 volumes with ISBN)
- **07-Strategy** — Strategic documents for HNS and EVA
- **08-Reports** — PoC and implementation reports

---

## HNS-36 Python Package

The first implementation of HNS-36 as a Python library.

- **Location:** `01-Docs/05-Implementations/hns36_pkg/`
- **Tests:** 19/19 passing
- **Core functions:**
  - `hns36.analyze(text)` — detect structural errors in AI responses
  - `hns36.constrain(question)` — generate HNS-36 constrained response
  - `hns36.compare(question, a, b)` — blind structural comparison
- **Install:** `pip install anthropic` → `pip install -e 01-Docs/05-Implementations/hns36_pkg`

---

## Next Steps

For those interested in HNS:

1. Read the **[HNS Strategic Roadmap v1.1](./07-Strategy/HNS-Strategic-Roadmap-v1.1.md)**
2. Explore the HNS-36 / 144 / 864 coordinate system
3. Experiment with EVA-based external verification (optional)
4. Apply HNS in your own research or implementation (optional)

---

**HNS serves as the structural foundation for human–AI alignment.**

**Natural Structure Works**  
© 2026 S. Hara. All rights reserved.
