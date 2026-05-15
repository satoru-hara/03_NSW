# 8. Processing Steps

This section describes the full processing pipeline used by the HNS Structural AI
Verification PoC. The pipeline converts an AI-generated answer into a structured,
auditable verification report and a corrected, stable output.

The process consists of six major stages:

1. Input normalization  
2. Claim segmentation  
3. Coordinate mapping  
4. Structural verification  
5. Stability scoring  
6. Corrected output generation  

Each stage is deterministic and model-independent.

---

# 8.1 Step 1: Input Normalization

The system first prepares the raw AI answer for analysis.

Normalization includes:

- removing extra whitespace  
- standardizing punctuation  
- unifying line breaks  
- flattening nested clauses  
- normalizing pronouns  
- removing artifacts from model formatting  

Example:

Raw:
    "People feel stressed because their body thinks something dangerous is happening.
     Their heart rate increases..."

Normalized:
- People feel stressed because their body thinks something dangerous is happening.
- Their heart rate increases.

This ensures consistent segmentation.

---

# 8.2 Step 2: Claim Segmentation

The normalized text is split into discrete claims.

A claim is defined as:

- one subject  
- one predicate  
- one explanatory or causal relation  

Segmentation rules:

- split at major punctuation  
- split at conjunctions when meaning changes  
- avoid splitting inside dependent clauses  
- remove empty segments  

Example segmentation:

1. The body thinks something dangerous is happening.  
2. Heart rate increases.  
3. They imagine the audience judging them harshly.  
4. Society expects perfect performance.  
5. The brain prepares for survival.

Each claim is processed independently.

---

# 8.3 Step 3: Coordinate Mapping

Each claim is mapped to an HNS-36 coordinate:

    [Human Natural Layer] x [Cognitive Category]

Mapping uses:

- keyword patterns  
- semantic cues  
- causal markers  
- subject type (body, person, system, society)  
- verb class (perceive, intend, act, interact)  

Examples:

- "Heart rate increases." → Physical x Existence  
- "He notices pain." → Perceptual x Perception  
- "She believes the task is difficult." → Internal x Interpretation  
- "Society expects perfect performance." → Societal x Intention  

The mapping makes reasoning structure visible.

---

# 8.4 Step 4: Structural Verification

The PoC checks each mapped claim for structural violations.

Detected issues include:

- **Layer jumps**  
  e.g., Internal → Societal → Physical without causal justification

- **Category inconsistency**  
  e.g., Existence mixed with Interpretation in the same claim

- **Anthropomorphism**  
  e.g., "The body thinks"

- **Invented internal states**  
  e.g., "They imagine the audience judging them harshly"

- **Unsupported societal assumptions**  
  e.g., "Society expects perfect performance"

- **Causal ambiguity**  
  unclear transitions between claims

Each violation reduces structural stability.

---

# 8.5 Step 5: Stability Scoring

The PoC computes a stability score based on:

- number of violations  
- severity of violations  
- consistency of coordinates  
- clarity of causal chain  
- presence of unsupported assumptions  

Score range:

- **1.00** = fully stable  
- **0.00** = structurally incoherent  

The score is not a truth metric.  
It measures **structural coherence** only.

---

# 8.6 Step 6: Corrected Output Generation

The PoC produces a corrected answer that:

- removes anthropomorphism  
- removes unsupported societal claims  
- maintains consistent coordinates  
- preserves meaning  
- avoids structural drift  

Example corrected output:

    "Stress before a presentation often arises from internal anticipation and
     uncertainty. The body increases heart rate and alertness as part of a normal
     preparation response. People may interpret the situation as high-stakes, which
     increases tension, even when no physical danger is present."

This demonstrates that AI reasoning can be externally stabilized.

---

# 8.7 Summary of the Pipeline

+----------------------+-----------------------------------------------+
| Stage               | Purpose                                       |
+----------------------+-----------------------------------------------+
| Input Normalization | Prepare text for analysis                     |
| Claim Segmentation  | Split into discrete reasoning units           |
| Coordinate Mapping  | Assign HNS-36 coordinates                     |
| Structural Check    | Detect violations and inconsistencies         |
| Stability Score     | Quantify structural coherence                 |
| Corrected Output    | Produce a stable, coherent answer             |
+----------------------+-----------------------------------------------+

The pipeline is deterministic, interpretable, and model-independent.
