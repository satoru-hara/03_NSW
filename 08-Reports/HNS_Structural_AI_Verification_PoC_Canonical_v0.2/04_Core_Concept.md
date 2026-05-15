# 4. Core Concept

The core concept of the HNS Structural AI Verification PoC is that AI-generated
reasoning can be evaluated through a **fixed, human-interpretable coordinate system**.
This coordinate system is the canonical **HNS-36** matrix:

- 6 Human Natural Layers (vertical axis)
- 6 Abstract Cognitive Categories (horizontal axis)

Every claim in an AI answer can be expressed as:

    [Layer] x [Category]

This creates a stable structural representation of reasoning that is independent of:

- model architecture  
- training data  
- vendor implementation  
- parameter count  

The PoC demonstrates that **reasoning structure is observable**, even when the internal
model is a black box.

---

# 4.1 Why Structure Matters

AI hallucination and reasoning drift often occur because:

- claims mix incompatible layers  
- causal chains jump across categories  
- internal states are invented  
- societal-level assumptions appear without grounding  
- intentions are assigned without evidence  

These failures are **structural**, not semantic.

HNS-36 provides a way to detect these structural failures by checking whether each
claim stays within a coherent coordinate.

---

# 4.2 Claim Segmentation

The PoC begins by splitting an AI answer into discrete claims.  
A claim is defined as:

- a single unit of meaning  
- containing one subject  
- one predicate  
- one explanatory or causal relation  

Example:

"Stress increases heart rate because the body prepares for action."

This becomes:

1. Stress increases heart rate.  
2. The body prepares for action.  

Each claim is then independently mapped to an HNS coordinate.

---

# 4.3 Coordinate Mapping

Each claim is mapped to:

- a Human Natural Layer (L1–L6)  
- a Cognitive Category (C1–C6)  

Examples:

- "Heart rate increases" → Physical x Existence  
- "The person notices pain" → Perceptual x Perception  
- "He believes the task is difficult" → Internal x Interpretation  
- "She intends to rest" → Intentional x Intention  
- "They coordinate their actions" → Relational x Interaction  
- "The system enforces a rule" → Societal x Action  

This mapping makes reasoning **visible**.

---

# 4.4 Structural Verification

Once mapped, the PoC checks for:

- layer jumps  
- category inconsistency  
- unsupported causal transitions  
- invented internal states  
- societal assumptions without grounding  
- ambiguous or mixed coordinates  

These structural violations indicate that the reasoning is unstable.

---

# 4.5 Stability Score

The PoC computes a stability score based on:

- number of violations  
- severity of violations  
- consistency of coordinates  
- clarity of causal chain  

The score is not a judgment of truth.  
It is a measure of **structural coherence**.

---

# 4.6 Corrected Output

Finally, the PoC produces:

- a verification report  
- a corrected, structurally stable answer  

The corrected answer stays within coherent coordinates and avoids structural drift.

This demonstrates that **AI reasoning can be externally stabilized** without modifying
the underlying model.
