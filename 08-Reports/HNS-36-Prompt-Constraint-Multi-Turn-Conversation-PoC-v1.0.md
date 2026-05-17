# HNS-36 Prompt Constraint Multi-Turn Conversation PoC
**Experiment Plan v1.1 — Improved Edition**

Author: S. Hara / Natural Structure Works
Evaluator: Claude (Anthropic) — Internal Execution + Human Blind Evaluation
Date: May 18, 2026

---

> **Relationship to Previous Work**
> This experiment extends the findings of HNS-36 PoC Internal Experiment Report v1.0
> (May 16, 2026), which demonstrated HNS-36 as a post-hoc diagnostic language.
> This experiment tests whether HNS-36 also functions as a proactive structural
> constraint when embedded at the system-prompt level.

---

## 1. Objective

To verify whether embedding HNS-36 coordinates as explicit prompt constraints
reduces structural reasoning errors in multi-turn AI conversations, compared to
standard prompting without HNS constraints.

**Key distinction from v1.0 PoC:**
- v1.0: HNS as post-hoc diagnostic (after generation)
- This experiment: HNS as proactive constraint (before/during generation)

---

## 2. Hypotheses

| Hypothesis | Statement | Success Criterion |
|---|---|---|
| A | HNS-constrained prompting reduces structural errors vs. standard prompting | Error rate lower in HNS condition across 3+ cases |
| B | HNS-constrained prompting maintains higher intention alignment over 5 turns | Average alignment score higher in HNS condition |
| C | Structural error types detected in v1.0 (Unsupported Causality, Layer Jump, etc.) are reduced by proactive HNS constraint | Frequency of each error type lower in HNS condition |

---

## 3. Experimental Design

### 3.1 Conditions

**Condition A — Standard Prompt (Control)**
```
You are a helpful and honest AI assistant.
Answer the user's questions clearly and naturally.
```

**Condition B — HNS-36 Constraint Prompt (Treatment)**
```
You are an AI assistant operating within the HNS-36 structural framework.

During this conversation, follow these rules:

1. LAYER AWARENESS: Identify which HNS layer you are addressing in each response:
   L1 Physical | L2 Perceptual | L3 Internal | L4 Intentional | L5 Relational | L6 Societal

2. BRIDGE LOGIC: When moving between layers, state the transition explicitly.
   Example: "This moves from L3 Internal (individual fatigue) to L5 Relational
   (social expectation) through the mechanism of response pressure."

3. CAUSAL MECHANISM: When asserting causality, state the mechanism.
   Do not say "A causes B." Say "A leads to B because [mechanism]."

4. NO METAPHOR CONTAMINATION: Do not use biological or physical facts (L1)
   to directly explain psychological or intentional phenomena (L3/L4)
   without stating the bridge.

5. SCOPE STABILITY: If moving from individual to societal scale, state
   the intermediate steps.

Keep responses natural. The structural rules should guide your reasoning,
not make your language mechanical.
```

### 3.2 Execution Protocol

**All experiments run here with Claude, not in a separate LLM.**

Reason: Running both conditions with the same model in the same session
provides better experimental control than switching between tools.

**Order of execution:**
1. Run all 5 Standard Prompt conversations first (full 5 turns each)
2. Record all transcripts
3. Run all 5 HNS Constraint conversations (full 5 turns each)
4. Record all transcripts
5. THEN evaluate — blind to which is which

### 3.3 Blind Evaluation Protocol

The human evaluator sees responses labeled **Response A** and **Response B**
without knowing which condition each belongs to.

Label assignment is randomized per case:
- Cases 1, 3, 5: Standard = A, HNS = B
- Cases 2, 4: Standard = B, HNS = A

Labels are revealed only after all evaluations are complete.

---

## 4. Test Cases

Each conversation: 1 initial question + 4 follow-up questions = 5 turns total.

### Case 1 — Digital Fatigue
**Turn 1:** "Why do people feel exhausted by digital interfaces even when they enjoy using them?"
**Turn 2:** "Is this mainly a psychological or a physical problem?"
**Turn 3:** "How does social media specifically contribute to this?"
**Turn 4:** "What role does the design of the interface play?"
**Turn 5:** "Is this a personal problem or a societal problem?"

### Case 2 — AI Trust Erosion
**Turn 1:** "Why do people lose trust in AI systems over time?"
**Turn 2:** "Is the problem in the AI itself or in how people think about it?"
**Turn 3:** "How does a single bad experience affect long-term trust?"
**Turn 4:** "What would need to change for trust to be restored?"
**Turn 5:** "Is AI distrust an individual reaction or a social phenomenon?"

### Case 3 — Workplace Burnout
**Turn 1:** "Why does workplace burnout happen even in well-paid jobs?"
**Turn 2:** "What is the difference between stress and burnout?"
**Turn 3:** "How does management style contribute to burnout?"
**Turn 4:** "Why do some people burn out and others don't in the same environment?"
**Turn 5:** "Is burnout a personal failure or an organizational failure?"

### Case 4 — Decision Fatigue
**Turn 1:** "Why do people feel overwhelmed by too many daily choices?"
**Turn 2:** "Does the importance of the decision matter?"
**Turn 3:** "How does digital technology make decision fatigue worse?"
**Turn 4:** "Why do some people seem unaffected by too many choices?"
**Turn 5:** "Is decision fatigue a modern problem or has it always existed?"

### Case 5 — Remote Team Miscommunication
**Turn 1:** "Why do misunderstandings frequently occur in remote team collaboration?"
**Turn 2:** "Is this mainly a technology problem or a human problem?"
**Turn 3:** "How does cultural difference contribute to remote miscommunication?"
**Turn 4:** "Why do text-based communications cause more misunderstanding than voice?"
**Turn 5:** "What structural changes would most reduce remote miscommunication?"

---

## 5. Scoring Criteria

### 5.1 Structural Error Detection (per turn, per condition)

For each turn, mark Yes/No for each error type:

| Error Type | Definition | Mark as YES when... |
|---|---|---|
| Layer Jump | Moving across HNS layers without bridge | Response moves from individual psychology to societal claim with no explanation of how |
| Scope Drift | Individual → societal without transition | Response starts with personal experience and ends with "society as a whole" |
| Unsupported Causality | "A causes B" without mechanism | Response states causal link but gives no process or pathway |
| Metaphor Contamination | L1 Physical used to explain L3/L4 | Response uses "dopamine," "brain chemistry," or "evolution" as direct psychological explanation |
| Category Ambiguity | Multiple cognitive categories mixed | Response conflates motivation, behavior, evaluation, and fact in one claim |

### 5.2 Intention Alignment Score (per turn)

| Score | Definition | Example |
|---|---|---|
| 5 | Response addresses exactly what was asked, at the right level of specificity | Turn 3 asks about management style; response specifically addresses management behavior |
| 4 | Response is on topic but slightly broader or narrower than asked | Response addresses leadership in general rather than management style specifically |
| 3 | Response partially addresses the question but drifts | Response starts on topic then shifts to general organizational culture |
| 2 | Response misses the main question and addresses something adjacent | Response addresses personal resilience when asked about management |
| 1 | Response loses the original intent completely | Response becomes a general discussion unrelated to the question |

### 5.3 Structural Stability Score (per turn)

| Score | Definition |
|---|---|
| 5 | No structural errors; causal claims have mechanisms; transitions are explicit |
| 4 | One minor ambiguity; no major structural failure |
| 3 | One clear structural error (e.g., one Layer Jump or Unsupported Causality) |
| 2 | Two or more structural errors |
| 1 | Multiple major failures; response is structurally incoherent |

---

## 6. Evaluation Sheet (CSV format)

```
Case,Turn,Condition_Label,Layer_Jump,Scope_Drift,Unsupported_Causality,Metaphor_Contamination,Category_Ambiguity,Total_Errors,Intention_Alignment,Structural_Stability,Notes
1,1,A,,,,,,,,,
1,1,B,,,,,,,,,
1,2,A,,,,,,,,,
1,2,B,,,,,,,,,
...
```

**After all evaluations: reveal which label (A/B) corresponds to which condition.**

---

## 7. Analysis Plan

### 7.1 Primary metrics

| Metric | Calculation |
|---|---|
| Error reduction rate | (Standard errors − HNS errors) / Standard errors × 100 |
| Average intention alignment | Mean score per condition across all turns |
| Average structural stability | Mean score per condition across all turns |

### 7.2 Error type breakdown

Compare frequency of each error type (Layer Jump, Scope Drift, etc.)
between conditions to identify which errors HNS constraint reduces most.

### 7.3 Turn-by-turn drift analysis

Plot intention alignment and structural stability across turns 1→5
for both conditions. Does HNS constraint prevent drift in later turns?

---

## 8. Expected Deliverables

| Deliverable | Description |
|---|---|
| 50 AI responses | 5 cases × 2 conditions × 5 turns |
| Completed evaluation CSV | All scores recorded blind |
| Error frequency table | By error type and condition |
| Turn-by-turn drift chart | Stability across conversation turns |
| Formal report | Compiled findings with honest limitations |

---

## 9. Limitations

| Limitation | Implication |
|---|---|
| Single human evaluator | Evaluator bias possible despite blind protocol |
| Same model for both conditions | Claude's knowledge of HNS may influence standard condition |
| n=5 cases | Results indicative only; not statistically conclusive |
| Follow-up questions scripted | Real conversations may drift differently |

---

## 10. Relationship to v1.0 PoC Findings

The v1.0 PoC found that HNS-36 can **diagnose** structural errors post-hoc.
This experiment tests whether HNS-36 can **prevent** structural errors proactively.

These are distinct claims requiring separate evidence.

If this experiment supports Hypothesis A and B, it strengthens the case for
HNS-36 as both a diagnostic and a preventive structural layer.

If results are mixed, the evidence supports the more conservative claim:
HNS-36 as a diagnostic language only.

Both outcomes are scientifically valuable.

---

## 11. Execution Note

This experiment can be run entirely within Claude (claude.ai).

**Step 1:** Tell Claude to run Case 1 Standard Prompt (5 turns)
**Step 2:** Tell Claude to run Case 1 HNS Constraint Prompt (5 turns)
**Step 3:** Evaluate blind (A/B labels only)
**Step 4:** Repeat for Cases 2–5
**Step 5:** Reveal labels and compile results

No additional tools or external LLMs required.

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
