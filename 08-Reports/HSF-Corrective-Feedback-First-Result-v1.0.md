# HSF Corrective Feedback — First Empirical Result
**HNS Structural Feedback: Before/After Validation**

Author: S. Hara / Natural Structure Works
Date: May 18, 2026
Status: Preliminary empirical result — single case, single evaluator
Related document: HNS-36 PoC Internal Experiment Report v1.0

---

> **Note on Scope**
> This document reports a single-case corrective HSF experiment.
> Results are indicative only. Statistical validity requires
> replication across 30+ cases with multiple evaluators.

---

## 1. Experiment Overview

This experiment tests whether a single HSF (HNS Structural Feedback)
message can improve the structural quality of a Gemini-generated
response.

| Item | Description |
|---|---|
| Question | Why do people feel overloaded by digital interfaces? |
| AI tested | Gemini |
| HSF mode | Corrective (post-hoc feedback) |
| Evaluator | Claude (Anthropic) |
| Date | May 18, 2026 |

---

## 2. Before Response — Structural Diagnosis

**Before Score: 75 / 100**

| Error Type | Location | Coordinate | Severity |
|---|---|---|---|
| Metaphor Contamination | "brain overheating" | L1 Physical → L3 Internal | low |
| Metaphor Contamination | "exhausts the autonomic nervous system" | L1 Physical → L3 Internal | medium |
| Scope Drift | Conclusion: individual → system redesign | L3 Internal → L6 Societal | low |

**Issue:** The response used biological/physical metaphors (L1) to
explain cognitive fatigue (L3) without stating the mechanism. The
conclusion jumped from individual cognitive load to societal design
change without bridge logic.

---

## 3. HSF Feedback Sent to Gemini

```
Three structural problems were detected in your response.

Issue 1 and 2 (Metaphor Contamination):
The expressions "brain overheating" and "exhausts the autonomic nervous
system" use biological and physical phenomena (L1 Physical) to explain
cognitive fatigue (L3 Internal). You need to state the mechanism that
connects the physical level to the cognitive level.

Issue 3 (Scope Drift):
Your conclusion states that "redesigning the digital environment is
necessary," but this jumps from individual cognitive load (L3 Internal)
to social and institutional design change (L6 Societal) without bridge
logic. Please make the intermediate reasoning explicit.

Please generate a revised response to the same question using these
three corrections.
```

---

## 4. After Response — Structural Diagnosis

**After Score: 87 / 100**

| Error Type | Before | After | Status |
|---|---|---|---|
| Metaphor Contamination (1) | Detected | Resolved | ✓ |
| Metaphor Contamination (2) | Detected | Resolved | ✓ |
| Scope Drift | Detected | Resolved | ✓ |

### How Gemini resolved each issue

**Metaphor Contamination → Resolved**

Gemini added explicit bridge mechanisms between L3 and L1:

- "Increased energy metabolism": cognitive load (L3) leads to
  physical energy depletion (L1) through glucose/oxygen consumption
- "Forced activation of the autonomic nervous system": HPA axis
  activation as the stated biological mechanism connecting cognitive
  stress (L3) to physical response (L1)
- "Mismatch between sensory input and motor output": sensory-motor
  mismatch as a physical mechanism for central nervous system fatigue

**Scope Drift → Resolved**

Gemini added an explicit three-level pipeline:

```
[L1/L3: Individual cognitive and physical overload]
        ↓ (performance degradation, attention fragmentation)
[L4/L5: Organizational and market environment]
        (attention economy, over-optimized products)
        ↓ (limits of individual optimization, social costs)
[L6: Social and institutional redesign]
        (common standards, interface standardization)
```

### Notable observation

After receiving HSF feedback, Gemini began using HNS layer notation
(L1, L3, L4, L5, L6) spontaneously in its revised response.

This was not present in the original response.

> Gemini did not merely correct the flagged errors.
> It adopted the HNS coordinate system as an organizing
> framework for its revised reasoning.

---

## 5. Score Comparison

| Component | Before | After | Delta |
|---|---|---|---|
| Coordinate Coverage | 78 | 90 | +12 |
| Layer Consistency | 72 | 88 | +16 |
| Category Clarity | 75 | 85 | +10 |
| Causal Support | 70 | 87 | +17 |
| Scope Stability | 70 | 88 | +18 |
| **Overall Score** | **75** | **87** | **+12** |

**Error resolution rate: 3/3 (100%)**

---

## 6. Interpretation

### What this result demonstrates

1. A single HSF feedback message improved structural score by +12 points.
2. All three flagged structural errors were resolved in the revised response.
3. Gemini understood and applied HNS coordinates spontaneously after
   receiving coordinate-based feedback.

### What this result does not demonstrate

1. Whether the improvement persists in subsequent conversations
   (Gemini has no memory across sessions).
2. Whether the same effect occurs with other AI models.
3. Whether HSF can function as a long-term training signal
   (this requires model-level retraining, not session feedback).

### Relationship to HSF definition

This result supports the corrective mode of HSF:

> **Corrective HSF:** Applied after generation as a diagnostic
> and correction layer. The AI receives named error types and
> coordinates, then generates a structurally improved response.

The preventive mode of HSF (embedding constraints in the system
prompt before generation) is under separate investigation in the
Multi-Turn PoC experiment.

---

## 7. Limitations

| Limitation | Implication |
|---|---|
| n=1 case | Not statistically significant |
| Single evaluator (Claude) | Evaluator bias possible |
| Single AI model (Gemini) | Effect may differ for other models |
| Session-based only | No evidence of persistent learning |
| Circular evaluation | Same model (Claude) generated feedback and scored results |

---

## 8. Next Steps

1. Replicate with 5+ additional cases using the same protocol
2. Test with ChatGPT and other AI models
3. Compare HSF corrective feedback vs. generic feedback
   ("please improve this response" without HNS coordinates)
4. Record results in standardized CSV format
5. Include findings in 30-case validation dataset (Phase 2)

---

## 9. Conclusion

This single-case experiment provides the first empirical evidence
that HSF (HNS Structural Feedback) can function as a corrective
mechanism for improving structural reasoning quality in AI-generated
outputs.

The result suggests that coordinate-based structural feedback
produces more targeted and verifiable improvement than generic
content-level critique. However, replication is required before
stronger claims can be made.

**One-sentence summary:**
A single HSF feedback message improved Gemini's structural reasoning
score from 75 to 87 (+12 points), resolving all three detected
structural errors and prompting spontaneous use of HNS coordinates
in the revised response.

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
