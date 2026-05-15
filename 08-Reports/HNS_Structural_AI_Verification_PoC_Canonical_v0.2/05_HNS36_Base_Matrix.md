# 5. HNS-36 Base Matrix

The HNS-36 matrix is the foundational coordinate system used for structural
verification in this PoC. It is constructed from:

- 6 Human Natural Layers (vertical axis)
- 6 Abstract Cognitive Categories (horizontal axis)

This creates a **6 x 6 = 36-cell** matrix that represents all structurally valid
forms of human reasoning.

Each cell is a coordinate:

    [Layer] x [Category]

The matrix is canonical and normative.  
All PoC logic, mapping rules, and verification steps depend on this structure.

---

# 5.1 Human Natural Layers (Vertical Axis)

+---------+----------------+-----------------------------------------------+
| LayerID | Canonical Name | Summary                                       |
+---------+----------------+-----------------------------------------------+
|   L1    | Physical       | Biological, material, bodily conditions       |
|   L2    | Perceptual     | Sensory intake, attention, signal detection   |
|   L3    | Internal       | Memory, emotion, stress, continuity           |
|   L4    | Intentional    | Purpose, goal orientation, directed meaning   |
|   L5    | Relational     | Communication, coordination, interaction      |
|   L6    | Societal       | Systems, institutions, norms, environment     |
+---------+----------------+-----------------------------------------------+

---

# 5.2 Abstract Cognitive Categories (Horizontal Axis)

+------------+----------------+-----------------------------------------------+
| CategoryID | Canonical Name | Summary                                       |
+------------+----------------+-----------------------------------------------+
|    C1      | Existence      | What exists, structural state                 |
|    C2      | Perception     | What is sensed or noticed                     |
|    C3      | Interpretation | What is understood or explained               |
|    C4      | Intention      | What is aimed or selected                     |
|    C5      | Action         | What is executed or performed                 |
|    C6      | Interaction    | What is exchanged or mutually affected        |
+------------+----------------+-----------------------------------------------+

---

# 5.3 Full HNS-36 Matrix (ASCII Table)

The full 36-cell matrix is shown below.  
Each cell represents a structurally valid coordinate for a claim.

+---------+-------------+-------------+----------------+-------------+-------------+--------------+
| Layer \ | Existence   | Perception  | Interpretation | Intention   | Action      | Interaction  |
| Category| (C1)        | (C2)        | (C3)           | (C4)        | (C5)        | (C6)         |
+---------+-------------+-------------+----------------+-------------+-------------+--------------+
| L1      | L1 x C1     | L1 x C2     | L1 x C3        | L1 x C4     | L1 x C5     | L1 x C6      |
| Physical|             |             |                |             |             |              |
+---------+-------------+-------------+----------------+-------------+-------------+--------------+
| L2      | L2 x C1     | L2 x C2     | L2 x C3        | L2 x C4     | L2 x C5     | L2 x C6      |
| Percept.|             |             |                |             |             |              |
+---------+-------------+-------------+----------------+-------------+-------------+--------------+
| L3      | L3 x C1     | L3 x C2     | L3 x C3        | L3 x C4     | L3 x C5     | L3 x C6      |
| Internal|             |             |                |             |             |              |
+---------+-------------+-------------+----------------+-------------+-------------+--------------+
| L4      | L4 x C1     | L4 x C2     | L4 x C3        | L4 x C4     | L4 x C5     | L4 x C6      |
| Intent. |             |             |                |             |             |              |
+---------+-------------+-------------+----------------+-------------+-------------+--------------+
| L5      | L5 x C1     | L5 x C2     | L5 x C3        | L5 x C4     | L5 x C5     | L5 x C6      |
| Relat.  |             |             |                |             |             |              |
+---------+-------------+-------------+----------------+-------------+-------------+--------------+
| L6      | L6 x C1     | L6 x C2     | L6 x C3        | L6 x C4     | L6 x C5     | L6 x C6      |
| Societ. |             |             |                |             |             |              |
+---------+-------------+-------------+----------------+-------------+-------------+--------------+

---

# 5.4 Why the Matrix Works

The HNS-36 matrix is effective because:

- it is **complete** (covers all human reasoning structures)  
- it is **minimal** (no redundant dimensions)  
- it is **orthogonal** (layers and categories do not overlap)  
- it is **interpretable** (humans can understand each coordinate)  
- it is **model-independent** (works for any AI system)  

This makes HNS-36 suitable for:

- structural verification  
- hallucination detection  
- causal chain analysis  
- governance and auditing  
- cross-model comparison  

---

# 5.5 Example Coordinates

Examples of real claims mapped to HNS-36:

- "Heart rate increases." → **Physical x Existence**  
- "He notices pain." → **Perceptual x Perception**  
- "She believes the task is difficult." → **Internal x Interpretation**  
- "He intends to rest." → **Intentional x Intention**  
- "They coordinate their actions." → **Relational x Interaction**  
- "The system enforces a rule." → **Societal x Action**  

These examples illustrate how the matrix captures the structure of reasoning.
