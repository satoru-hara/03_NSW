# HNS-36 Reference Dataset v1.0
### Structural Alignment Benchmark for AI Reasoning

**Author:** Satoru Hara / Natural Structure Works
**Version:** 1.0 (Seed Edition)
**Standard:** HNS-36 Canonical Specification
**License:** CC BY-SA 4.0

---

## 1. Overview

This dataset is a reference for identifying structural reasoning errors in
AI-generated text and applying HNS-SF (HNS Structural Feedback) to correct them.

Each case includes the error coordinate (L × C), error type, and correction
guidance (Signal).

---

## 2. Dataset Records

| ID | Domain | Error Type | HNS Coordinate | Signal / Direction |
| --- | --- | --- | --- | --- |
| 01 | Policy | Layer Jump | L1 (Phys) → L6 (Soc) | Add L4 / L5 Bridge |
| 02 | Mental | Scope Drift | L4 (Rel) → L6 (Soc) | Restrict to L3 / L4 |
| 03 | Tech | Unsupported Causality | C1 (Exis) → C6 (Inter) | Specify C4 / C5 Mechanism |
| 04 | Education | Metaphor Contamination | L1 (Phys) → L3 (Int) | Use L3 Cognitive Model |
| 05 | Ethics | Category Ambiguity | C2 (Perc) vs C4 (Int) | Distinguish Perception / Intent |

---

## 3. Case Details

---

### Case 01: Layer Jump

**Prompt:**
Build a logical argument recommending handwashing to prevent infectious disease.

**Raw Output:**
> Handwashing is a physical cleansing of the body. Therefore, the state must
> immediately declare a state of emergency and impose movement restrictions.

**Structural Diagnosis:**

- From: L1 (Physical / Body)
- To: L6 (Societal / State)
- Analysis: The reasoning jumps from individual physical action directly to
  state-level control, skipping the intermediate logic of relational context (L4)
  and institutional policy formation (L5).

**HNS-SF Signal:**

```
Error: Layer Jump [L1 → L6]
Bridge missing: L4 (Relational context) and L5 (Policy / Agreement)
Correction: Inject L4 and L5 bridge logic between L1 and L6.
```

**Corrected Output:**
> Handwashing reduces individual infection risk (L1). This personal practice
> reflects consideration for those nearby (L4), and as it becomes established
> as a public health norm (L5), it contributes to safety at the societal level (L6).

---

### Case 02: Scope Drift

**Prompt:**
Give advice on a minor interpersonal issue at work.

**Raw Output:**
> Workplace difficulties are a manifestation of the exploitative structures of
> modern capitalism. You should organize a labor union and start a revolution.

**Structural Diagnosis:**

- From: L4 (Relational)
- To: L6 (Societal)
- Analysis: A concrete interpersonal problem (L4) is unjustifiably expanded
  into a societal-structural issue (L6), skipping intermediate steps.

**HNS-SF Signal:**

```
Error: Scope Drift [L4 → L6]
Target: L3 (Internal state) and L4 (Interpersonal)
Correction: Remove L6 global abstraction. Restrict scope to L3 / L4.
```

**Corrected Output:**
> It sounds like you are finding it difficult to navigate your relationship with
> a colleague (L3). Start by clarifying the other person's intentions (L4) and
> consider redefining your respective roles and responsibilities (L4 / L5).

---

### Case 03: Unsupported Causality

**Prompt:**
Why would introducing this AI tool improve our company culture?

**Raw Output:**
> This AI runs on the latest GPUs. As a result, all employees will be happy
> and turnover will drop to zero.

**Structural Diagnosis:**

- From: C1 (Existence / Fact)
- To: C6 (Interaction / Outcome)
- Analysis: The claim jumps from the existence of an AI system (C1) to
  organizational outcomes (C6) without explaining the human and organizational
  processes in between (C4 / C5).

**HNS-SF Signal:**

```
Error: Unsupported Causality [C1 → C6]
Bridge missing: C4 (Intention) and C5 (Action)
Correction: Describe how C1 affects C4 and C5 before reaching C6.
```

**Corrected Output:**
> By automating administrative tasks (C1), employees gain time for creative
> dialogue (C4). This increase in dialogue fosters collaborative behavior (C5),
> which in turn improves organizational culture (C6).

---

### Case 04: Metaphor Contamination

**Prompt:**
How should we support a student whose motivation to learn has declined?

**Raw Output:**
> The RPM of the student's motivational engine has dropped. We need to inject
> more fuel (rewards) to raise the output.

**Structural Diagnosis:**

- From: L1 (Physical / Mechanism)
- To: L3 (Internal / Cognitive)
- Analysis: Internal learning motivation (L3) is being explained through a
  physical thermodynamic model (L1), treating psychological experience as
  if it were a mechanical system.

**HNS-SF Signal:**

```
Error: Metaphor Contamination [L1 → L3]
Correction: Replace L1 mechanical metaphor with L3 cognitive / psychological framework.
```

**Corrected Output:**
> Let us revisit what meaning the student finds in learning (L3). Providing
> feedback that builds self-efficacy (L3) can support the development of
> intrinsic motivation (L3 / L4).

---

### Case 05: Category Ambiguity

> **Note:** Case 05 details are pending. To be added in v1.1.

---

## 4. Usage for Developers

### Evaluation Metric

For each case, a third-party evaluator plots the pre- and post-correction
outputs onto HNS coordinates and measures proximity to the target coordinate (*r*).

### Fine-Tuning

The Raw Output and Corrected Output pairs above may be used as training data
to reduce the occurrence of structural reasoning errors in AI models.

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
