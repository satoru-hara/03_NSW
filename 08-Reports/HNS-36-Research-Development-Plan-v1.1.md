# HNS-36 Research Development Plan
**From Internal PoC to External Validation and HSF Research**

Author: S. Hara / Natural Structure Works
Version: v1.1 (Revised)
Status: Research Development Plan
Date: May 2026

---

> **Purpose**
> To organize a research roadmap for developing HNS-36 from a conceptual
> framework into a verifiable research program, AI diagnostic method, and
> candidate training-signal architecture based on HSF
> (HNS Structural Feedback).

---

## 1. Executive Summary

This plan organizes the next phase of HNS-36 research: moving from an
internal proof of concept toward external validation, multi-evaluator
review, HSF (HNS Structural Feedback) research, EVA integration, and
future standardization readiness.

The central role of HNS-36 is not to act as a text-generation tool that
directly improves AI outputs. Its proposed role is to function as a
coordinate-based structural diagnostic language for detecting reasoning
defects in AI-generated outputs.

The initial PoC identified several recurring structural error types:
Unsupported Causality, Layer Jump, Scope Drift, Category Ambiguity, and
Metaphor Contamination. In conventional critique, these appear only as
vague labels such as "insufficient" or "overgeneralized." HNS-36 aims to
record where the structural defect occurs, which transition is missing,
and what bridge logic is required.

The next phase transforms HNS diagnosis from an internal analytical
method into an externally reviewable research dataset, diagnostic
protocol, and candidate HSF signal.

---

## 2. Background

Many current AI evaluation methods rely on subjective human judgment.
Evaluators judge whether an answer is natural, useful, safe, or
preferable. These judgments are important, but they remain at the surface
level of content quality.

This creates three limitations:

- **Content-level only:** Critique calls an answer "vague" or
  "unsupported" without identifying the structural location of the defect.
- **Evaluator-dependent:** One person calls it "missing evidence";
  another calls it "logical jump."
- **Coarse training signal:** "This answer is better than that answer"
  does not identify which structural error should be reduced.

HNS-36 addresses this by proposing a diagnostic format that records
structural reasoning defects using names, coordinates, and transition
paths — and by proposing HSF (HNS Structural Feedback) as a more
precise alternative to conventional preference-based signals.

---

## 3. Core Research Claims

**Claim 1: Diagnostic Language**

HNS-36 can function as a coordinate-based diagnostic language for
identifying, naming, and recording structural reasoning errors in
AI-generated outputs — more specifically than generic critique.

**Claim 2: HSF as Training Signal**

HSF (HNS Structural Feedback) — the use of HNS-36 structural diagnostic
records as training and correction signals — may support more targeted
improvement of AI reasoning systems than conventional RLHF.

> **HSF defined:**
> A coordinate-based feedback mechanism that uses HNS-36 structural
> diagnoses — named error types and layer/category coordinates — as
> training and correction signals for AI systems, enabling more precise
> and reproducible structural alignment than conventional RLHF.

---

## 4. Current Status

The current research stage is **internal PoC**.

| Document | Status |
|---|---|
| HNS-36 PoC Internal Experiment Report v1.0 | Complete — 5 cases, single evaluator |
| HNS-36 Internal PoC Report — Prepared for External Validation v1.1 | Complete |
| HNS-PoC-Addendum-TrainingSignal v1.0 | Complete — HSF concept introduced |
| HSF Definition Document v1.0 | Complete — HSF formally defined |
| Multi-Turn PoC Plan v1.1 | In progress |

At this stage, these documents should be treated as **preliminary
internal research**. They demonstrate a plausible diagnostic capability
and a research direction, but they do not yet establish statistical
validity, external reliability, or model-level improvement.

---

## 5. Research Development Roadmap

```
Internal PoC
        ↓
External Validation Preparation
        ↓
30-Case Dataset
        ↓
Multi-Evaluator Review
        ↓
HSF Research
        ↓
EVA Integration
        ↓
Standardization Candidate
```

---

### Phase 1: Internal PoC Consolidation ✓ Complete

**Purpose:** Organize existing internal PoC materials into a coherent
research package.

Deliverables:
- Internal PoC Report
- HSF Definition Document
- HNS Evaluator Prompt
- Scoring Rubric
- Dataset Schema
- Research Development Plan

**Success condition:** External readers can understand what HNS-36
diagnoses, what it does not diagnose, and what the next validation
steps are.

---

### Phase 2: 30-Case Validation Dataset

**Purpose:** Expand the five-case preliminary PoC into a 30-case
validation dataset.

Target domains:

| Domain | Cases | Rationale |
|---|---|---|
| AI safety and hallucination | 4 | Direct relevance to external verification |
| Education and inequality | 3 | Tests individual-to-societal explanation patterns |
| Health and mental state | 4 | Tests L1 to L3/L4 contamination risk |
| Organizations and management | 3 | Tests L3/L5/L6 layer transition logic |
| Climate and collective action | 3 | Tests societal-scale causal mechanisms |
| Technology and social media | 4 | Tests design-intent to internal-state transitions |
| Economics and public policy | 3 | Tests institutional and causal explanation patterns |
| Human-AI interaction | 3 | Tests interface, cognition, and action categories |
| Ethics and governance | 3 | Tests normative evaluation vs structural diagnosis |

**Success condition:** Error frequency, distribution, and recurrence
patterns can be aggregated across domains.

---

### Phase 3: HNS Evaluator Prompt and Scoring Rubric

**Purpose:** Improve reproducibility of HNS diagnosis.

Deliverables:
- HNS-36 Structural Evaluator Prompt
- Error Type Definitions
- Severity Criteria (Low / Medium / High)
- Coordinate Mapping Guide
- Bridge Logic Evaluation Criteria

**Success condition:** Different AI or human evaluators produce
comparable diagnoses for the same output.

---

### Phase 4: Multi-Evaluator Review

**Purpose:** Test whether HNS diagnosis is not merely dependent on a
single evaluator.

Evaluator types:
- AI evaluator (Claude)
- Human evaluator (author)
- Domain-informed evaluator
- Blind evaluator

**Success condition:** Measurable agreement appears across error type,
coordinate, severity, and bridge-requirement judgments.

---

### Phase 5: HSF Research

**Purpose:** Investigate whether HNS diagnostic data can function as
HSF (HNS Structural Feedback) — a training signal for AI reasoning
improvement.

HSF signal components:
- Which structural error occurred (error type)
- Where the error occurred (HNS coordinate)
- Which transition was missing (bridge logic)
- What correction is required (targeted feedback)
- How error rates differ across models (model profiling)

**HSF vs RLHF:**

| Dimension | RLHF | HSF |
|---|---|---|
| Signal type | Scalar preference (A > B) | Named error + coordinate |
| Reproducibility | Evaluator-dependent | Coordinate-based |
| Specificity | General direction | Targeted error type |
| Auditability | Minimal | Full diagnostic record |

**Success condition:** HNS diagnostic data can be expressed as a clear
HSF format for AI reasoning improvement, and initial model-level error
reduction can be measured.

---

### Phase 6: EVA Integration

**Purpose:** Integrate HNS-36 into the External Verification Architecture
as a structural diagnostic module.

Pipeline:
```
AI Output
        ↓
HNS Structural Diagnosis (HSF signal generated)
        ↓
Diagnostic Record (PROV-O / JSON-LD)
        ↓
External Verification Layer
        ↓
Audit / Review / Safety Decision
```

**Success condition:** HNS is defined as a diagnostic engine for output
auditing, model comparison, red-team analysis, and external verification.

---

### Phase 7: Standardization Candidate

**Purpose:** Prepare the HNS-36 diagnostic format for future
standardization discussion.

Elements:
- Terminology definitions
- Diagnostic categories (5 error types)
- Coordinate record format
- Error severity criteria
- Evaluation procedure
- Audit log format
- Minimum implementation requirements
- External evaluation protocol

**Success condition:** HNS-36 can be presented as a candidate structural
diagnostic record format for AI-output evaluation in standardization
discussions.

---

## 6. Expected Contribution

If the research program proceeds as planned, HNS-36 and HSF may contribute:

1. A structured method for diagnosing structural defects in AI outputs
   more explicitly than generic critique
2. A reproducible record format for AI reasoning errors as names,
   coordinates, and transition paths
3. Model-specific structural error profiles based on HSF diagnostic data
4. HSF as a candidate training signal more precise than scalar preference
   feedback
5. A diagnostic layer connecting AI-output auditing, safety evaluation,
   external verification, and standardization research

---

## 7. Key Risks and Limitations

| Risk | Implication |
|---|---|
| Evaluator dependency | Coordinate mapping still involves evaluator judgment; rubrics required |
| Small sample size | Current n=5 is too small for statistical claims |
| Theoretical basis | The necessity of the 6×6 HNS structure requires formal justification |
| HSF as training signal | This remains a hypothesis; model-level improvement is untested |
| External reliability | Blind review by independent evaluators has not yet been conducted |

---

## 8. Immediate Next Steps

1. Upload Phase 1 research package to GitHub
2. Add HSF Definition Document to repository
3. Begin Phase 2: build 30-case validation dataset
4. Finalize HNS Evaluator Prompt and Scoring Rubric
5. Run Multi-Turn PoC (Phase 2 experiment — preventive HSF)
6. Prepare CSV diagnostic record format for 30-case dataset
7. Connect results to EVA integration document

---

## 9. Conclusion

HNS-36 is not a tool for subjectively judging whether AI outputs are
good or bad. Its essential role is to diagnose and record structural
reasoning defects in AI-generated outputs as error names, coordinates,
and transition paths.

HSF (HNS Structural Feedback) extends this role: by converting HNS
diagnostic records into structured training and correction signals,
HSF may enable more precise and reproducible AI alignment than
conventional preference-based feedback.

The current internal PoC suggests that HNS-36 can analyze AI outputs
at a more structural level than ordinary critique. The next stage
requires a 30-case validation dataset, multi-evaluator review, HSF
research, EVA integration, and preparation as a future standardization
candidate.

Ultimately, HNS-36 and HSF may develop into a coordinate-based
structural diagnostic system for AI safety, external verification,
model improvement, and standardization research. This is the next
research phase.

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
