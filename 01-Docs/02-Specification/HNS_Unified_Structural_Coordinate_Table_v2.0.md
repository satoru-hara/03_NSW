# HNS Unified Structural Coordinate Table

*The unified canonical reference of HNS structural primitives — Natural Layers, Abstract Categories, Onto-Modal Quadrants, Inference & Control Operators, and Social Meta Layers — together with their theoretical lineage.*

---

| Field | Value |
|---|---|
| **Author** | Satoru Hara / Natural Structure Works (NSW) |
| **Version** | v2.0 |
| **Revision** | Adds Section 5, Social Meta Layers (HNS-SMS-6), as the Axis-3 grounding axis. It is listed as a parallel axis and is **orthogonal** to the 36/144/864 coordinate nesting (it grounds/regulates output; it is not a multiplicative factor). Subtitle and Composition updated accordingly. Sections 1–4 unchanged from v1.0. |
| **Status** | Authoritative Reference (author's own framework; not reviewed by ISO, IEC, SC42, IEEE, NIST, or any other standards body) |
| **Placement** | Normative appendix to *HNS-36 / HNS-144: The Structural & Observational OS* (Book 2); Section 5 also serves *HNS-SMS-6* (Book 4). Referenced by all HNS publications. |
| **Purpose** | Define, in one place, the canonical names of every HNS structural primitive and its theoretical lineage, so that all HNS specifications, implementations, and publications use a single stable terminology. |

> **Note on lineage.** The *Lineage* / *Proposer* columns indicate **conceptual inspiration, not strict derivation from a single ontology**. HNS synthesizes across multiple traditions; no claim of full fidelity to any one framework is implied.

---

## 1. Natural Layers (HNS-36)

The six natural layers of human structure (causal structure), forming one axis of the 36-cell base matrix.

| ID | Name | Lineage (inspiration) | Spec reference | Rationale / cross-reference |
|---|---|---|---|---|
| L1 | Physical / Substrate | Physics / BFO Material Entity | L1: Physical / Substrate | Universal lowest layer. |
| L2 | Cellular / Informational | Computational neuroscience | L2: Cellular / Informational | Neural-representation layer. |
| L3 | Cognitive / System 1 | Kahneman Type 1 | L3: Cognitive / System 1 | Maps to MAV Axis 1. |
| L4 | Operational / System 2 | Kahneman Type 2 | L4: Operational / System 2 | Verification function; MAV Axis 2/3. |
| L5 | Micro-Social / Interaction | Habermas | L5: Micro-Social / Interaction | Basis of SMS-2/3. |
| L6 | Macro-Social / Institutional | Institutional theory / BFO Social Object | L6: Macro-Social / Institutional | Maps to SMS-5/6. |

> **Note (L3–L4).** Kahneman's System 1 / System 2 are parallel dual processes, not an intrinsic vertical hierarchy. HNS re-positions them as processing-depth layers; this is a deliberate re-framing, not a claim about Kahneman's original model.

---

## 2. Abstract Categories (HNS-36)

The six abstract (non-causal, explanatory) categories, forming the second axis of the 36-cell base matrix.

| ID | Name | Lineage (inspiration) | Spec reference | Rationale / cross-reference |
|---|---|---|---|---|
| C1 | Continuant / Entity | Aristotle / BFO | C1: Continuant / Entity | Universal. |
| C2 | Occurrent / Process | Aristotle / BFO | C2: Occurrent / Process | Formally well-defined. |
| C3 | Relational / Boundary | Aristotle / Kant | C3: Relational / Boundary | Aligns with the HNS "orthogonality" concept. |
| C4 | Quality / State | Kant | C4: Quality / State | State-space definition. |
| C5 | Transformation / Operation | Pearl (do-operator) | C5: Transformation / Operation | Core of causal transition. |
| C6 | Meta-Level / Schema | Kant (category of categories) | C6: Meta-Level / Schema | Aligns with HNS Runtime / EVA. |

> **Note (BFO consistency).** Under strict BFO, *Continuant* (C1) and *Occurrent* (C2) are the top-level dichotomy, *Quality* (C4) is a dependent continuant (a sub-type of C1), and *Process* (a sub-type of C2) overlaps with C5. The six categories above are therefore a **synthetic** category set inspired by Aristotle/BFO/Kant, not a flat partition derived from any single ontology — see the lineage note above.

---

## 3. Onto-Modal Quadrants (HNS-144)

Two binary dimensions whose Cartesian product yields four quadrants, extending the 36-cell matrix to 144.

| Dimension | Binary values | Lineage (inspiration) | Rationale / cross-reference |
|---|---|---|---|
| ① Ontological Domain | Subjective / Objective | Kant / Habermas | Suppresses Category Ambiguity. |
| ② Modal Invariants | Necessary / Contingent | Kant (modality) | Distinguishes AI "rule vs. context." |

**Quadrants (① × ②):**

| Quadrant | Definition |
|---|---|
| Q1 | Subjective × Contingent |
| Q2 | Subjective × Necessary |
| Q3 | Objective × Contingent |
| Q4 | Objective × Necessary |

---

## 4. Inference & Control Operators (HNS-864)

Six operators acting on the coordinate system, extending 144 to 864. O1–O3 are inference operators (Pearl's hierarchy: association → intervention → counterfactual); O4–O6 are control-loop operators (Powers' Perceptual Control Theory, plus an HNS-defined output regulator).

| ID | Name | Proposer | Mathematical meaning |
|---|---|---|---|
| O1 | Conditioning | Statistics / Pearl | P(Y ∣ X) — association (Pearl Rung 1) |
| O2 | Intervention / do-operator | Pearl | P(Y ∣ do(X)) — intervention (Rung 2) |
| O3 | Counterfactual | Pearl | P(Y_x ∣ X′, Y′) — counterfactual retrospect (Rung 3) |
| O4 | Reference Signal | Powers (PCT) | Reference invariant |
| O5 | Comparator / Error Detection | Powers (PCT) | Control Error = Reference − Perception |
| O6 | Output Attenuation | HNS Engineering | output = g(s) · raw_output, where s is the structural grounding score and g(0) = 0, g monotone increasing, g(s) ∈ [0, 1] ("Zero-Incidence Attenuation") |

> **Note (O5).** Friston's prediction error (sensory − prediction) is a structural analogue of the comparator operator and may be used as an alternative formalization in active-inference implementations. It is not identical: PCT minimizes control error to keep perception at a reference, whereas predictive coding minimizes free energy / surprise.

---

## 5. Social Meta Layers (HNS-SMS-6)

Six grounding layers spanning the embodied (somatic) base, through social scales, to the universal. They constitute **Axis 3 (Grounded / Executive)** — the real-time grounding stack — and are **orthogonal** to the 36/144/864 coordinate: they ground and regulate output, they do not subdivide the coordinate.

Naming: **Social Meta Layers** is the axis (the six layers); **Social Meta Structure (HNS-SMS-6)** is the specification (Book 4). "Social Meta" is the umbrella term for the whole stack; it does **not** assert that every layer — notably the somatic base — is itself social.

| ID | Domain | Lineage (inspiration) | Grounds / suppresses |
|---|---|---|---|
| SMS-1 | Somatic | Barsalou / Harnad (embodied cognition; symbol grounding) | Bodily / ergonomic coherence with the environment; suppresses Metaphor Contamination. |
| SMS-2 | Protocol | Habermas (communicative action) | Communicative alignment and intelligibility; suppresses Scope Drift. Anchors with L5. |
| SMS-3 | Organizational | HNS Extension | Organizational / collaborative scope; suppresses Scope Drift. Anchors with L5. |
| SMS-4 | Economic | HNS Extension | Resource / information / value equivalence; suppresses Unsupported Causality. |
| SMS-5 | Governance | Institutional theory | Conformance with external norms; suppresses Category Ambiguity. Anchors with L6 and Book 6. |
| SMS-6 | Universal | Ashby / General Systems Theory | Global optimality; no systemic violation; suppresses Layer Jump. Anchors with L6. |

> **Note (grounding function & lineage).** The six layers realize the grounding function G(x): an output is grounded (G = 1) only if compatible with all six. The stack extends grounding from body to civilization, building on the free-energy principle (Friston), predictive coding (Rao & Ballard), perceptual control theory (Powers), and cybernetics (Wiener, Ashby). SMS-3 and SMS-4 are HNS extensions with no single external proponent. The failure-suppression mapping is not one-to-one: Scope Drift is suppressed jointly by SMS-2 and SMS-3. As elsewhere, the lineage column indicates conceptual inspiration, not strict derivation.

---

## 6. Composition

The three coordinate specifications are nested scalings of the same system (**Axis 2**). The Social Meta Layers (**Axis 3**) are a **parallel grounding axis, orthogonal** to this nesting — not a multiplicative factor.

| Spec | Composition | Cells |
|---|---|---|
| HNS-36 | Natural Layers (6) × Abstract Categories (6) | 36 |
| HNS-144 | HNS-36 × Onto-Modal Quadrants (4) | 144 |
| HNS-864 | HNS-144 × Inference & Control Operators (6) | 864 |
| HNS-SMS-6 | Social Meta Layers (6) — parallel grounding axis (Axis 3) | orthogonal (not multiplied into the nesting) |

---

*End of HNS Unified Structural Coordinate Table v2.0.*
