# HNS Structural Hallucination Taxonomy
## A Human‑Structure‑Based Framework for AI Coherence Violations

**Author:** Satoru Hara, Natural Architecture Works (NAW), 2026

---

## 1. Overview

Modern LLMs operate through statistical generation and are therefore unable to produce responses grounded in human structural meaning (HNS‑36). This gives rise to **structural coherence violations** that fall outside the scope of conventional "semantic hallucination" classifications. Existing taxonomies focus on content-level errors — factual, reasoning, and retrieval failures — and do not provide a systematic framework for deviations from human cognitive structure.

This report introduces the Structural Hallucination Taxonomy proposed by HNS, a classification framework grounded in the HNS Structural OS, and presents initial validation results.

---

## 2. The Five Structural Hallucination Types

Five types formally defined in HNS‑PoC‑Package v1.0:

| Type | Definition |
|------|------------|
| **Layer Jump** | A response skips across meaning layers without an explicit bridge |
| **Category Ambiguity** | Cognitive, emotional, and intentional categories become conflated |
| **Metaphor Contamination** | Metaphorical or symbolic expressions distort the underlying structural coordinates |
| **Scope Drift** | The response structurally departs from the user's intended scope |
| **Unsupported Causality** | A causal claim is generated without a mechanism grounded in the layer hierarchy |

---

## 3. Empirical Validation — 50‑Turn PoC (May 2026)

A blinded comparative experiment was conducted using Claude (Anthropic) across 5 topics × 10 turns. All five error types were consistently detectable across all turns.

### Results

| Metric | Standard Condition | HNS Condition |
|--------|--------------------|---------------|
| Structural Errors | 31 | 0 |
| Intention Alignment (1–5) | 4.72 | 5.00 |
| Structural Stability (1–5) | 3.52 | 5.00 |

### Interpretive Caveats

In this experiment, both response generation and evaluation were performed by the same model, meaning the evaluation was not independent. Additionally, whether the observed improvements in the HNS condition reflect the HNS framework specifically or the general effect of structured prompting cannot be determined from this experiment alone. Independent replication by human evaluators is the necessary next step.

---

## 4. Implications

This classification framework has potential applications in the following areas:

- AI safety and alignment evaluation
- Structural foundations for explainability (XAI)
- Audit log design for EU AI Act / ISO 42001 compliance
- Consistency verification in multi-agent systems
- Reconstruction of LLM evaluation standards

---

## 5. Conclusion

The HNS Structural Hallucination Taxonomy presents a framework for classifying AI response failures as deviations from a human Structural OS. The initial PoC confirmed consistent applicability of all five types across all turns.

Establishing the scientific validity of this framework requires independent human evaluation and comparison against existing structured prompting approaches. Through future independent validation, the goal is to develop this into a foundational technology — Structural Alignment — for ensuring coherence between AI systems and human structural meaning.
