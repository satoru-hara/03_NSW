# HNS-SF: HNS Structural Feedback
**Definition Document v1.0**

Author: Satoru Hara / Natural Structure Works
Date: May 18, 2026
Status: Conceptual specification with preliminary empirical basis
Naming Standard: HNS-36 Canonical Specification v1.0

---

> **Note on Status**
> HNS-SF is a proposed feedback mechanism grounded in preliminary empirical
> work (HNS-36 PoC, n=5, single evaluator, May 2026). The concept has
> not been implemented at scale or validated through independent review.
> This document is offered as a formal definition for discussion and
> future research.

---

## 1. Core Definition

**HNS-SF (HNS Structural Feedback)**

A coordinate-based feedback mechanism that uses HNS-36 structural
diagnoses — including named error types and layer/category coordinates —
as training and correction signals for AI systems.

Unlike conventional RLHF, which provides scalar preference judgments,
HNS-SF delivers interpretable, reproducible, and structurally grounded
feedback that identifies **where** and **why** reasoning failed within
a human-aligned cognitive coordinate system.

By converting HNS diagnostic outputs into a structured training signal,
HNS-SF enables AI models to internalize causal constraints, avoid structural
reasoning errors, and achieve more stable cognitive alignment across domains.

---

## 2. Background: The Limitation of Existing Feedback

### 2.1 RLHF (Reinforcement Learning from Human Feedback)

Current AI alignment relies primarily on RLHF:

```
Human evaluator: "Response A is better than Response B"
        ↓
Scalar preference signal (A > B)
        ↓
Model update in the direction of preference
```

**Problems with RLHF:**

| Problem | Description |
|---|---|
| Subjectivity | Preference judgments vary by evaluator |
| Opacity | Cannot specify which aspect was better or worse |
| Irreproducibility | Same pair may be judged differently by different evaluators |
| Non-specificity | Cannot target specific error types for reduction |
| Unmeasurable progress | Improvement cannot be tracked at the structural level |

### 2.2 What Is Missing

RLHF answers: **"Which output is preferred?"**

It cannot answer: **"Where did the reasoning fail, and why?"**

This gap becomes critical as AI systems are deployed in high-stakes
domains where structural reasoning quality — not just surface fluency —
determines reliability.

---

## 3. HNS-SF: The Structural Alternative

### 3.1 How HNS-SF Works

```
AI-generated output
        ↓
HNS-36 structural diagnosis
        ↓
Named error type + coordinate assignment
        ↓
Structured feedback signal
        ↓
Targeted model correction
```

### 3.2 The HNS-SF Signal

Where RLHF produces:
> "Response A > Response B" (scalar)

HNS-SF produces:
> "Layer Jump detected: L3 Internal × C3 Interpretation →
>  L6 Societal × C1 Existence, bridge logic missing,
>  severity: medium"

This signal is:
- **Named** — the error has a specific, reproducible category
- **Located** — the coordinate identifies where in the reasoning
- **Explained** — the diagnosis states why it is a problem
- **Graded** — severity provides a continuous correction signal
- **Auditable** — the full diagnostic record is preserved

---

## 4. HNS-SF Error Types as Feedback Signals

HNS-SF uses five structural error types as its diagnostic vocabulary:

| Error Type | Signal Meaning | Correction Direction |
|---|---|---|
| Layer Jump | Reasoning crossed layer boundaries without bridge logic | Add explicit transition between L-n and L-m |
| Scope Drift | Individual claim expanded to societal scale without steps | Insert intermediate relational or institutional logic |
| Unsupported Causality | Causal claim made without mechanism | Require stated mechanism for all A → B assertions |
| Metaphor Contamination | L1 Physical used to explain L3/L4 phenomena | Separate biological and psychological explanations |
| Category Ambiguity | Multiple cognitive categories conflated | Distinguish Existence, Perception, Interpretation, Intention, Action, Interaction |

Each error type provides a **directional correction signal** — not just
"this is wrong" but "this is wrong in this specific structural way."

---

## 5. HNS-SF vs RLHF: Comparison

| Dimension | RLHF | HNS-SF |
|---|---|---|
| Signal type | Scalar preference (A > B) | Named error + coordinate |
| Evaluator requirement | Human preference judgment | HNS-36 structural diagnosis |
| Reproducibility | Evaluator-dependent | Coordinate-based (reproducible) |
| Specificity | General direction | Targeted error type |
| Auditability | Minimal | Full diagnostic record |
| Progress measurement | Indirect (reward model) | Direct (error frequency by type) |
| Domain portability | Limited | Cross-domain (universal coordinate system) |
| Complementarity | Standalone | Complementary to RLHF |

> **Note:** HNS-SF is not a replacement for RLHF. It is a complementary
> mechanism that adds structural precision to existing feedback pipelines.

---

## 6. Two Modes of HNS-SF

### 6.1 Corrective HNS-SF (post-hoc)

Applied after generation as a diagnostic and correction layer:

```
AI output generated
        ↓
HNS-36 diagnosis applied
        ↓
Errors identified and logged
        ↓
Corrective feedback sent to model
        ↓
Revised output generated
```

**Current status:** Demonstrated in HNS-36 PoC v1.0 (May 2026)

### 6.2 Preventive HNS-SF (proactive)

Applied as a system-prompt constraint before generation:

```
HNS-36 constraints embedded in system prompt
        ↓
Model generates output within structural constraints
        ↓
Layer Jump, Scope Drift, etc. reduced at source
```

**Current status:** Under investigation (Multi-Turn PoC, May 2026)

---

## 7. Relationship to Existing Frameworks

| Framework | Relationship to HNS-SF |
|---|---|
| RLHF | HNS-SF complements RLHF by adding structural precision |
| HITL (Human-in-the-Loop) | HNS-SF provides structured diagnostic records for human reviewers |
| EVA (External Verification Architecture) | HNS-SF diagnostic logs integrate with EVA PROV-O records |
| ISO/IEC 42001 | HNS-SF supports transparency and auditability requirements |
| EU AI Act Art. 13 | HNS-SF enables coordinate-based explainability |

---

## 8. Empirical Basis

HNS-SF is grounded in the following preliminary empirical work:

| Study | Finding |
|---|---|
| HNS-36 PoC Internal Experiment (n=5, May 2026) | All 3 hypotheses supported; Unsupported Causality in 100% of cases |
| Gemini Output Validation (n=3, May 2026) | Avg. structural score: 68 → 84 after HNS constraint (+16 pts) |
| Human Blind Evaluation (n=3, May 2026) | HNS wins on structural clarity 3/3; loses on readability 1/3 |
| Gemini Diagnostic Case (May 2026) | Metaphor Contamination identified as model-specific pattern |

> **Limitation:** All evidence is preliminary. Scale validation (30+ cases,
> multiple evaluators) is required before stronger claims can be made.

---

## 9. Potential Applications

### 9.1 Model-Specific Error Profiling

Accumulate HNS-SF diagnostic data across AI models:

> "Gemini: Metaphor Contamination rate = X%"
> "ChatGPT: Unsupported Causality rate = Y%"

This would provide the first coordinate-based structural comparison
of major AI models — replacing subjective style assessments with
reproducible structural diagnostics.

### 9.2 Targeted Fine-Tuning

Use HNS-SF error records as training signals to reduce specific error
types in AI models, with measurable, coordinate-level progress tracking.

### 9.3 AI Safety Audit

HNS-SF diagnostic records provide a structural audit trail for AI outputs,
supporting external verification and regulatory compliance.

### 9.4 Cross-Domain Alignment

Because HNS-36 coordinates are domain-independent, HNS-SF signals apply
consistently across education, healthcare, governance, and technical domains.

---

## 10. Limitations

| Limitation | Implication |
|---|---|
| Small empirical base | Current n=5-8; scale validation required |
| Single evaluator | Independent replication needed |
| Manual coordinate mapping | Automation required for scale |
| No training implementation | HNS-SF as training signal is theoretical at this stage |
| Model access | Retraining major models requires developer cooperation |

---

## 11. Development Roadmap

| Phase | Deliverable |
|---|---|
| Phase 1 (Complete) | HNS-36 PoC: demonstrate diagnostic capability |
| Phase 2 (In progress) | Multi-Turn PoC: test preventive HNS-SF |
| Phase 3 | 30-case validation dataset |
| Phase 4 | Automated coordinate mapper |
| Phase 5 | HNS-SF as corrective feedback: measure revision quality |
| Phase 6 | HNS-SF as training signal: measure model-level error reduction |
| Phase 7 | Cross-model structural comparison using HNS-SF profiles |

---

## 12. Conclusion

HNS-SF addresses a structural gap in current AI alignment methodology.

Where RLHF asks "which output do you prefer?", HNS-SF asks "where and
why did the reasoning fail?" This shift from preference to structure
enables feedback that is interpretable, reproducible, and targeted.

The preliminary evidence from HNS-36 PoC work suggests that structural
reasoning errors are real, recurring, and nameable. HNS-SF converts these
diagnoses into signals that can guide AI improvement at the coordinate level.

HNS-SF is not a replacement for existing alignment methods. It is a
structural layer that makes AI reasoning more transparent, more
correctable, and more aligned with the causal structure of human
understanding.

---

## Appendix: One-Sentence Definitions

**HNS-36:** A 36-cell coordinate system (6 Human Natural Layers ×
6 Abstract Cognitive Categories) for diagnosing structural reasoning
errors in AI-generated text.

**HNS-SF (HNS Structural Feedback):** A coordinate-based feedback mechanism
that uses HNS-36 structural diagnoses — named error types and
layer/category coordinates — as training and correction signals for
AI systems, enabling more precise and reproducible structural alignment
than conventional RLHF.

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
