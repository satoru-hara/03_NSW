# 11. Prototype Logic

This section describes the internal logic used by the HNS Structural AI Verification
PoC. The prototype is intentionally rule-based, deterministic, and interpretable.  
Its purpose is to demonstrate that structural verification can be performed without
access to model internals.

The logic is divided into:

1. Normalization Logic  
2. Segmentation Logic  
3. Mapping Logic  
4. Structural Verification Logic  
5. Stability Scoring Logic  
6. Correction Logic  

Each component is described below.

---

# 11.1 Normalization Logic

The normalization module applies a series of deterministic transformations:

- trim whitespace  
- unify punctuation  
- convert line breaks to a standard format  
- flatten nested clauses  
- normalize pronouns  
- remove formatting artifacts  

Example transformation:

Input:
    "People feel stressed because their body thinks something dangerous is happening..."

Normalized:
- People feel stressed because their body thinks something dangerous is happening.

Normalization ensures consistent segmentation and mapping.

---

# 11.2 Segmentation Logic

Segmentation splits the normalized text into discrete claims.

Rules:

- split at periods, semicolons, and major punctuation  
- split at conjunctions when meaning changes  
- avoid splitting inside dependent clauses  
- remove empty segments  

Example:

1. The body thinks something dangerous is happening.  
2. Heart rate increases.  
3. They imagine the audience judging them harshly.

Each claim is processed independently.

---

# 11.3 Mapping Logic (HNS-36 Assignment)

Each claim is mapped to:

    [Human Natural Layer] x [Cognitive Category]

Mapping uses:

- subject type  
  - body → Physical  
  - person → Internal / Intentional  
  - group → Relational  
  - society → Societal  

- verb class  
  - exist → Existence  
  - sense → Perception  
  - interpret → Interpretation  
  - intend → Intention  
  - act → Action  
  - interact → Interaction  

- semantic cues  
- causal markers  

Example:

"Heart rate increases." → Physical x Existence

The mapping is rule-based and fully interpretable.

---

# 11.4 Structural Verification Logic

The verifier checks each mapped claim for structural violations.

Violation types:

1. **Layer Jump**  
   - abrupt transitions between layers without causal justification  

2. **Category Inconsistency**  
   - mixing Existence and Interpretation in the same claim  

3. **Anthropomorphism**  
   - assigning cognition to biological systems  

4. **Invented Internal States**  
   - inferring mental states without evidence  

5. **Unsupported Societal Assumptions**  
   - asserting societal expectations without grounding  

6. **Causal Ambiguity**  
   - unclear transitions between claims  

Each violation is recorded with:

- claim number  
- violation type  
- description  

---

# 11.5 Stability Scoring Logic

The stability score is computed using:

- number of violations  
- severity of violations  
- consistency of coordinates  
- clarity of causal chain  

Score range:

- 1.00 = fully stable  
- 0.00 = structurally incoherent  

The score measures structural coherence, not truth.

---

# 11.6 Correction Logic

The correction module generates a structurally stable answer.

Correction steps:

1. remove anthropomorphism  
2. remove unsupported societal assumptions  
3. avoid invented internal states  
4. maintain consistent coordinates  
5. preserve original meaning  
6. avoid structural drift  

Example corrected output:

    "Stress before a presentation often arises from internal anticipation and
     uncertainty. The body increases heart rate and alertness as part of a normal
     preparation response. People may interpret the situation as high-stakes, which
     increases tension, even when no physical danger is present."

---

# 11.7 Prototype Logic Summary

+---------------------------+-----------------------------------------------+
| Component                 | Purpose                                       |
+---------------------------+-----------------------------------------------+
| Normalization Logic       | Clean and standardize input                   |
| Segmentation Logic        | Extract discrete claims                       |
| Mapping Logic             | Assign HNS-36 coordinates                     |
| Verification Logic        | Detect structural violations                  |
| Stability Scoring Logic   | Quantify structural coherence                 |
| Correction Logic          | Produce stable, coherent output               |
+---------------------------+-----------------------------------------------+

The prototype logic demonstrates that structural verification is feasible,
interpretable, and model-independent.
