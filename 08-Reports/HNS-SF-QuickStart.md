# HNS-SF Quick Start Guide
### Try Structural Diagnosis in 5 Minutes

**HNS-SF (HNS Structural Feedback)** is a coordinate-based method for
diagnosing *where* and *why* AI reasoning fails — more precisely than
generic critique. This guide lets you run a diagnosis yourself using
any AI system (Claude, ChatGPT, Gemini, etc.).

---

## Step 1: Copy the Evaluator Prompt

Copy the entire block below and paste it into your AI system of choice.

---

```
You are an HNS-36 structural evaluator.

HNS-36 is a coordinate system for diagnosing structural reasoning errors
in AI-generated text. It uses two axes:

LAYERS (what level of reality the reasoning operates at):
  L1 Physical     — biological, material, bodily
  L2 Operational  — procedures, actions, skills
  L3 Internal     — psychology, cognition, emotion
  L4 Relational   — interpersonal, social interaction
  L5 Organizational — institutional, systemic, group
  L6 Societal     — civilization, policy, cultural norms

CATEGORIES (what cognitive function the reasoning performs):
  C1 Existence      — what is / what exists
  C2 Perception     — what is noticed / observed
  C3 Interpretation — what it means
  C4 Intention      — what is wanted / aimed at
  C5 Action         — what is done
  C6 Interaction    — how things affect each other

A coordinate is written as: L[n] × C[n]
Example: L3 × C3 = Internal layer, Interpretation category

FIVE STRUCTURAL ERROR TYPES:

1. Layer Jump
   Reasoning crosses layer boundaries without explanation.
   Example: jumps from L3 (individual psychology) to L6 (social policy)
   with no intermediate logic.

2. Scope Drift
   An individual-level claim expands to societal scale without steps.
   Example: "This person feels anxious → society is collapsing."

3. Unsupported Causality
   A causal claim (A causes B) is made without stating the mechanism.
   Example: "Social media causes depression" — how? through what process?

4. Metaphor Contamination
   A physical or biological metaphor (L1) is used to explain psychological
   or social phenomena (L3/L4/L5) as if they were the same thing.
   Example: "The brain is wired for addiction" used to explain social behavior.

5. Category Ambiguity
   Two or more cognitive categories (C1–C6) are conflated without distinction.
   Example: mixing what someone wants (C4 Intention) with what they do (C5 Action).

---

DIAGNOSIS TASK:

Read the following AI-generated text and apply HNS-36 structural diagnosis.

For each error found, report:
  - Error type (from the five above)
  - Location: the coordinate where the error occurs (L[n] × C[n])
  - What is missing (bridge logic, mechanism, intermediate step)
  - Severity: Low / Medium / High
  - Correction direction: what would fix it

If no error is found for a type, write "None detected."

End with an Overall Structural Score: 0–100
(100 = no structural errors; deduct points per error by severity:
High = -20, Medium = -10, Low = -5)

---

TEXT TO DIAGNOSE:

"Social media is designed to exploit dopamine responses in the brain.
This is why teenagers become addicted and cannot control their screen time.
As a result, an entire generation is losing the ability to form meaningful
relationships, and society is becoming increasingly isolated and fragmented.
We need new regulations to protect young people from these harms."
```

---

## Step 2: Read the Diagnosis

Your AI system will return a structured diagnosis. A well-formed HNS-SF
output looks like this:

```
Error 1: Metaphor Contamination
  Location: L1 × C1 → L3 × C3
  Missing: Distinction between neurological mechanism (L1) and
           psychological experience (L3)
  Severity: Medium
  Correction: Separate "dopamine response" (L1) from "feeling of
              compulsion" (L3) — they are not the same claim.

Error 2: Unsupported Causality
  Location: L3 × C3 → L4 × C6
  Missing: Mechanism explaining how screen time reduces relational capacity
  Severity: High
  Correction: Require an intermediate step: what specific relational
              skill is impaired, and through what process?

Error 3: Scope Drift
  Location: L3 × C3 → L6 × C1
  Missing: Intermediate logic at L4 (interpersonal) and L5 (institutional)
  Severity: High
  Correction: Insert steps: individual behavior → peer group patterns →
              institutional response → societal-level effect.

Overall Structural Score: 55 / 100
```

---

## Step 3: Compare Results

Run the same prompt in two or more AI systems and compare the diagnoses.

Questions to explore:
- Do different AI systems detect the same errors?
- Do they assign the same coordinates?
- Do they agree on severity?
- Which system produces the most reproducible diagnosis?

This comparison is itself an HNS-SF experiment.

---

## Step 4: Try Your Own Text

Replace the sample text in the prompt with any AI-generated output you
want to evaluate — a news summary, an explanation, a policy argument,
a model response to a question.

The five error types apply across all domains.

---

## Reference: HNS-36 at a Glance

| | C1 Existence | C2 Perception | C3 Interpretation | C4 Intention | C5 Action | C6 Interaction |
| --- | --- | --- | --- | --- | --- | --- |
| **L1 Physical** | L1×C1 | L1×C2 | L1×C3 | L1×C4 | L1×C5 | L1×C6 |
| **L2 Operational** | L2×C1 | L2×C2 | L2×C3 | L2×C4 | L2×C5 | L2×C6 |
| **L3 Internal** | L3×C1 | L3×C2 | L3×C3 | L3×C4 | L3×C5 | L3×C6 |
| **L4 Relational** | L4×C1 | L4×C2 | L4×C3 | L4×C4 | L4×C5 | L4×C6 |
| **L5 Organizational** | L5×C1 | L5×C2 | L5×C3 | L5×C4 | L5×C5 | L5×C6 |
| **L6 Societal** | L6×C1 | L6×C2 | L6×C3 | L6×C4 | L6×C5 | L6×C6 |

36 cells total. Each AI output can be mapped to one or more coordinates.

---

## Further Reading

| Document | Purpose |
| --- | --- |
| HNS-SF-Definition-v1.0.md | Full definition of HNS Structural Feedback |
| HNS-36-Research-Development-Plan-v1.1.md | Research roadmap and validation program |

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
