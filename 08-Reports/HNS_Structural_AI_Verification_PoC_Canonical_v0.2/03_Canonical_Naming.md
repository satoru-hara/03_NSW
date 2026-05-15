# 3. Canonical Naming Standard

This PoC follows the **HNS-36 Naming Consolidation & Canonical Specification v1.0**.
The canonical naming set is normative. All PoC implementations, GitHub documents,
EVA / SOHU verification modules, and standardization submissions must use the
canonical terms exclusively.

Historical OS-style names are treated as deprecated aliases and may be referenced
only for backward compatibility.

---

# 3.1 Canonical Human Natural Layers (L1–L6)

The six Human Natural Layers represent the vertical causal axis of HNS-36.

+---------+----------------+
| LayerID | Canonical Name |
+---------+----------------+
|   L1    | Physical       |
|   L2    | Perceptual     |
|   L3    | Internal       |
|   L4    | Intentional    |
|   L5    | Relational     |
|   L6    | Societal       |
+---------+----------------+

Layer meanings (summary):

- Physical: biological and material conditions  
- Perceptual: sensory intake, attention, signal reception  
- Internal: memory, emotion, stress, continuity  
- Intentional: purpose, goal orientation, directed meaning  
- Relational: communication, coordination, interface  
- Societal: institutions, systems, environmental context  

---

# 3.2 Canonical Abstract Cognitive Categories (C1–C6)

The six Abstract Cognitive Categories represent the horizontal explanatory axis of HNS-36.

+------------+----------------+
| CategoryID | Canonical Name |
+------------+----------------+
|    C1      | Existence      |
|    C2      | Perception     |
|    C3      | Interpretation |
|    C4      | Intention      |
|    C5      | Action         |
|    C6      | Interaction    |
+------------+----------------+

Category meanings (summary):

- Existence: what exists, structural state  
- Perception: what is sensed or noticed  
- Interpretation: what is understood or explained  
- Intention: what is aimed or selected  
- Action: what is executed or performed  
- Interaction: what is exchanged or mutually affected  

---

# 3.3 Historical Alias Handling (Deprecated)

Older PoC drafts used OS-style names.  
These are **not** official terms and must not appear in new documents.

+-------------------+-------------------------------+
| Historical Alias  | Canonical Handling            |
+-------------------+-------------------------------+
| PhysicalOS        | Physical                      |
| CognitiveOS       | Perceptual / Internal         |
| InteractionOS     | Relational                    |
| EnvironmentOS     | Societal                      |
| LoadOS            | Internal x Existence (context)|
| PatternOS         | Societal x Interaction        |
+-------------------+-------------------------------+

Aliases may be referenced only to interpret legacy documents.  
All new HNS materials must use canonical naming exclusively.

---

# 3.4 Canonical Coordinate Format

Each claim in an AI-generated answer is mapped to:

HNS Coordinate = [Human Natural Layer] x [Abstract Cognitive Category]

Examples:

- Internal x Existence  
- Relational x Action  
- Societal x Interaction  
- Perceptual x Perception  
- Intentional x Intention  

This coordinate system forms the basis of structural verification in the PoC.
