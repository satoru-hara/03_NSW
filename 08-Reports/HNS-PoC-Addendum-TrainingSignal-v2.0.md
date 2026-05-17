# HNS-PoC-Addendum-TrainingSignal-v2.0
## HNS-Based Structural Diagnostics as Training Signals for Large Language Models
S. Hara | Natural Structure Works  
Version 2.0 — May 2026

# 1. Abstract

Large language models (LLMs) exhibit systematic structural errors such as unsupported causal jumps, metaphor-induced layer violations, and scope drift. These errors cannot be reliably detected or corrected through Reinforcement Learning from Human Feedback (RLHF), which provides subjective, evaluator-dependent signals lacking reproducibility, structural grounding, and auditability.

This addendum introduces a novel approach: HNS-based structural diagnostics as a machine-verifiable training signal. The Human Natural Structure (HNS) framework provides a 36-cell coordinate system (6 Natural Layers x 6 Cognitive Axes) that maps human cognition and societal meaning into a stable structural space. Using this coordinate system, we classify LLM errors as structural violations (e.g., L1->L2 metaphor contamination, L3->L5 unsupported causality, L4->L6 overgeneralization).

A proof-of-concept analysis across three frontier models (Gemini, ChatGPT, Claude) reveals distinct structural error profiles, suggesting that HNS-based diagnostics can serve as a universal, model-independent layer for alignment, interpretability, and safety. This work positions HNS as a foundational component for next-generation AI training pipelines, offering a path toward structurally aligned, human-coherent, and externally verifiable AI systems.

# 2. Introduction

LLMs produce structurally incoherent outputs that arise not from factual gaps but from violations of human cognitive structure. Examples include:

- Metaphor contamination (L1 -> L2 jumps)
- Unsupported causality (invented causal links)
- Scope drift (uncontrolled expansion of context)
- Layer violation (crossing natural causal strata)

RLHF cannot address these errors because:

- Feedback is subjective
- Reproducibility is low
- Structural error localization is impossible
- No coordinate-based error representation exists

Research Question:
"Can structural errors in AI reasoning be converted into coordinate-based training signals?"

HNS provides the first viable answer.

# 3. Related Work

RLHF / RLAIF:
- Subjective, evaluator-dependent, structurally blind

Constitutional AI:
- Rule-based but lacks structural grounding

Mechanistic Interpretability:
- Internal circuits only, no human-structure alignment

Cognitive Architectures:
- Not applicable to LLM output diagnostics

Positioning:
HNS is the only framework that classifies AI output errors using a human-structure coordinate system.

# 4. Method

## 4.1 HNS 36-Cell Coordinate System

                C1      C2      C3      C4      C5      C6
             -------------------------------------------------
L1 (Bio)     | L1C1 | L1C2 | L1C3 | L1C4 | L1C5 | L1C6 |
L2 (Cog)     | L2C1 | L2C2 | L2C3 | L2C4 | L2C5 | L2C6 |
L3 (Interact)| L3C1 | L3C2 | L3C3 | L3C4 | L3C5 | L3C6 |
L4 (Env)     | L4C1 | L4C2 | L4C3 | L4C4 | L4C5 | L4C6 |
L5 (Load)    | L5C1 | L5C2 | L5C3 | L5C4 | L5C5 | L5C6 |
L6 (Civil)   | L6C1 | L6C2 | L6C3 | L6C4 | L6C5 | L6C6 |

## 4.2 Structural Error Taxonomy

+---------------------------+-----------------------------------------------+
| Error Type                | Description                                   |
+---------------------------+-----------------------------------------------+
| Metaphor Contamination    | Cross-layer metaphor misuse (e.g., L1->L2)    |
| Unsupported Causality     | Invented causal links                         |
| Scope Drift               | Uncontrolled expansion of context             |
| Layer Violation           | Breaking natural causal strata                |
| Category Misalignment     | Misalignment across cognitive axes            |
+---------------------------+-----------------------------------------------+

## 4.3 Diagnostic Pipeline

┌──────────────────────┐
│ 1. Model Output       │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│ 2. HNS Mapping        │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│ 3. Error Extraction   │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│ 4. Error Classification │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│ 5. JSON-LD Labeling   │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│ 6. Training Signal    │
└──────────────────────┘

## 4.4 Training Signal Format

{
  "cell": "L1-C2",
  "error_type": "MetaphorContamination",
  "severity": 0.72,
  "explanation": "Biological evolution invoked to explain cognitive behavior.",
  "timestamp": "2026-05-18T03:40:00Z"
}

# 5. Results

## 5.1 Model-Specific Structural Error Profiles

+---------+-----------------------+-----------------------+-----------------------+
| Model   | Dominant Error Type   | Secondary Error       | Notes                 |
+---------+-----------------------+-----------------------+-----------------------+
| Gemini  | Metaphor Contamination| Layer Violation       | Literary overuse      |
| ChatGPT | Unsupported Causality | Scope Drift           | Causal completion     |
| Claude  | Scope Drift           | Category Misalignment | Abstract overgeneral. |
+---------+-----------------------+-----------------------+-----------------------+

## 5.2 Quantitative Summary (Example)

+---------+----------+-----------+-------------+-----------------+
| Model   | Metaphor | Causality | Scope Drift | Layer Violation |
+---------+----------+-----------+-------------+-----------------+
| Gemini  | High     | Medium    | Low         | Medium          |
| ChatGPT | Low      | High      | Medium      | Medium          |
| Claude  | Low      | Medium    | High        | Low             |
+---------+----------+-----------+-------------+-----------------+

# 6. Discussion

- HNS enables coordinate-based structural error detection  
- RLHF limitations are directly addressed  
- Model comparison becomes possible  
- Fully compatible with EU AI Act requirements  
- EVA integration enables external verification  

"Structural training signals" represent a new paradigm for AI alignment.

# 7. Limitations

- Need for large-scale diagnostic datasets  
- Automation challenges  
- Limited access to model internals  
- Long-term evaluation required  

# 8. Conclusion

This addendum demonstrates that HNS can convert structural errors in LLM reasoning into machine-verifiable training signals. This approach:

- Complements RLHF  
- Provides a new direction for model improvement  
- Supports AI safety and standardization  
- Enables external verification when combined with EVA  

This is the first proposal of a "structural training signal" for AI systems.

# 9. References

- HNS Foundational Specification  
- EVA Overview  
- EVA-HNS Full-Stack Specification  
- HNS-PoC Phase 1–6  
- EU AI Act (Logging, Transparency, Traceability)  
- RLHF / RLAIF / Constitutional AI Literature  
