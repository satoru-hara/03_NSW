# 16. Appendix

This appendix provides supplemental material that supports the HNS Structural AI
Verification PoC.  
It includes reference tables, definitions, and extended examples that do not fit
directly into the main sections but are essential for deeper understanding.

The appendix contains:

1. HNS-36 Reference Table  
2. Violation Taxonomy (Extended)  
3. Mapping Rules (Extended)  
4. Example Claim Library  
5. Glossary of Terms  

---

# 16.1 HNS-36 Reference Table (Full)

The canonical HNS-36 matrix is reproduced here for convenience.

+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| Layer       | Existence   | Perception  | Interpretation | Intention   | Action      | Interaction  |
| (Lx)        | (C1)        | (C2)        | (C3)           | (C4)        | (C5)        | (C6)         |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L1 Physical | L1 x C1     | L1 x C2     | L1 x C3        | L1 x C4     | L1 x C5     | L1 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L2 Percept. | L2 x C1     | L2 x C2     | L2 x C3        | L2 x C4     | L2 x C5     | L2 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L3 Internal | L3 x C1     | L3 x C2     | L3 x C3        | L3 x C4     | L3 x C5     | L3 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L4 Intent.  | L4 x C1     | L4 x C2     | L4 x C3        | L4 x C4     | L4 x C5     | L4 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L5 Relat.   | L5 x C1     | L5 x C2     | L5 x C3        | L5 x C4     | L5 x C5     | L5 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L6 Societ.  | L6 x C1     | L6 x C2     | L6 x C3        | L6 x C4     | L6 x C5     | L6 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+

+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| Layer       | Existence   | Perception  | Interpretation | Intention   | Action      | Interaction  |
| (Lx)        | (C1)        | (C2)        | (C3)           | (C4)        | (C5)        | (C6)         |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L1 Physical | L1 x C1     | L1 x C2     | L1 x C3        | L1 x C4     | L1 x C5     | L1 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L2 Percept. | L2 x C1     | L2 x C2     | L2 x C3        | L2 x C4     | L2 x C5     | L2 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L3 Internal | L3 x C1     | L3 x C2     | L3 x C3        | L3 x C4     | L3 x C5     | L3 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L4 Intent.  | L4 x C1     | L4 x C2     | L4 x C3        | L4 x C4     | L4 x C5     | L4 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L5 Relat.   | L5 x C1     | L5 x C2     | L5 x C3        | L5 x C4     | L5 x C5     | L5 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L6 Societ.  | L6 x C1     | L6 x C2     | L6 x C3        | L6 x C4     | L6 x C5     | L6 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+

+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| Layer       | Existence   | Perception  | Interpretation | Intention   | Action      | Interaction  |
| (Lx)        | (C1)        | (C2)        | (C3)           | (C4)        | (C5)        | (C6)         |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L1 Physical | L1 x C1     | L1 x C2     | L1 x C3        | L1 x C4     | L1 x C5     | L1 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L2 Percept. | L2 x C1     | L2 x C2     | L2 x C3        | L2 x C4     | L2 x C5     | L2 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L3 Internal | L3 x C1     | L3 x C2     | L3 x C3        | L3 x C4     | L3 x C5     | L3 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L4 Intent.  | L4 x C1     | L4 x C2     | L4 x C3        | L4 x C4     | L4 x C5     | L4 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L5 Relat.   | L5 x C1     | L5 x C2     | L5 x C3        | L5 x C4     | L5 x C5     | L5 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L6 Societ.  | L6 x C1     | L6 x C2     | L6 x C3        | L6 x C4     | L6 x C5     | L6 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+

===============================================================================
HNS-36 REFERENCE TABLE (FINAL ASCII-STABLE VERSION)
===============================================================================

+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| Layer       | Existence   | Perception  | Interpretation | Intention   | Action      | Interaction  |
| (Lx)        | (C1)        | (C2)        | (C3)           | (C4)        | (C5)        | (C6)         |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L1 Physical | L1 x C1     | L1 x C2     | L1 x C3        | L1 x C4     | L1 x C5     | L1 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L2 Percept. | L2 x C1     | L2 x C2     | L2 x C3        | L2 x C4     | L2 x C5     | L2 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L3 Internal | L3 x C1     | L3 x C2     | L3 x C3        | L3 x C4     | L3 x C5     | L3 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L4 Intent.  | L4 x C1     | L4 x C2     | L4 x C3        | L4 x C4     | L4 x C5     | L4 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L5 Relat.   | L5 x C1     | L5 x C2     | L5 x C3        | L5 x C4     | L5 x C5     | L5 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+
| L6 Societ.  | L6 x C1     | L6 x C2     | L6 x C3        | L6 x C4     | L6 x C5     | L6 x C6      |
+-------------+-------------+-------------+----------------+-------------+-------------+--------------+

===============================================================================
HNS-36 REFERENCE TABLE (FINAL NON-BREAKING ASCII VERSION)
===============================================================================

Layer (Lx)      Existence(C1)   Perception(C2)   Interpretation(C3)   Intention(C4)   Action(C5)     Interaction(C6)
---------------------------------------------------------------------------------------------------------------
L1 Physical     L1 x C1         L1 x C2          L1 x C3              L1 x C4          L1 x C5        L1 x C6
L2 Perceptual   L2 x C1         L2 x C2          L2 x C3              L2 x C4          L2 x C5        L2 x C6
L3 Internal     L3 x C1         L3 x C2          L3 x C3              L3 x C4          L3 x C5        L3 x C6
L4 Intentional  L4 x C1         L4 x C2          L4 x C3              L4 x C4          L4 x C5        L4 x C6
L5 Relational   L5 x C1         L5 x C2          L5 x C3              L5 x C4          L5 x C5        L5 x C6
L6 Societal     L6 x C1         L6 x C2          L6 x C3              L6 x C4          L6 x C5        L6 x C6
---------------------------------------------------------------------------------------------------------------

---

# 16.2 Violation Taxonomy (Extended)

The PoC uses a minimal violation taxonomy.  
This appendix provides extended definitions for future expansion.

### 1. Anthropomorphism  
Assigning cognition, intention, or interpretation to non-cognitive systems.

### 2. Unsupported Societal Assumption  
Claiming societal expectations or norms without grounding.

### 3. Invented Internal State  
Inferring thoughts, emotions, or beliefs without evidence.

### 4. Layer Jump  
Abrupt transition between layers without causal justification.

### 5. Category Inconsistency  
Mixing incompatible cognitive categories in a single claim.

### 6. Causal Ambiguity  
Unclear or missing causal relationships between claims.

### 7. Normative Drift (future)  
Unjustified introduction of moral or normative judgments.

### 8. Multi-agent Confusion (future)  
Blurring boundaries between agents or perspectives.

---

# 16.3 Mapping Rules (Extended)

This section provides additional mapping heuristics.

### Subject-Based Mapping

| Subject Type        | Default Layer |
|---------------------|---------------|
| Body / organ        | Physical      |
| Sensory system      | Perceptual    |
| Individual human    | Internal / Intentional |
| Group / team        | Relational    |
| Society / system    | Societal      |

### Verb-Class Mapping

| Verb Class          | Category      |
|---------------------|---------------|
| exist / change      | Existence     |
| sense / notice      | Perception    |
| believe / interpret | Interpretation|
| want / aim          | Intention     |
| act / respond       | Action        |
| coordinate / exchange| Interaction  |

---

# 16.4 Example Claim Library

A library of example claims and their HNS-36 coordinates.

### Physical Layer Examples
- "Heart rate increases." → L1 x C1  
- "Muscles contract." → L1 x C5  

### Perceptual Layer Examples
- "He notices a loud sound." → L2 x C2  
- "She detects movement." → L2 x C2  

### Internal Layer Examples
- "He remembers the event." → L3 x C3  
- "She feels anxious." → L3 x C1  

### Intentional Layer Examples
- "He intends to rest." → L4 x C4  
- "She chooses a strategy." → L4 x C4  

### Relational Layer Examples
- "They coordinate their actions." → L5 x C6  
- "He explains the plan to her." → L5 x C3  

### Societal Layer Examples
- "The system enforces a rule." → L6 x C5  
- "Society values cooperation." → L6 x C3  

---

# 16.5 Glossary of Terms

### HNS  
Human Natural Structure.  
A canonical model of human reasoning layers.

### HNS-36  
A 6x6 coordinate matrix representing all structurally valid reasoning forms.

### Structural Verification  
Evaluating reasoning based on structure, not truth.

### Stability Score  
A numerical measure of structural coherence.

### EVA  
External Verification Architecture.

### SOHU  
Structural Operating Human Unit.

---

# 16.6 Appendix Summary

+---------------------------+-----------------------------------------------+
| Component                 | Purpose                                       |
+---------------------------+-----------------------------------------------+
| HNS-36 Table              | Reference for mapping                         |
| Violation Taxonomy        | Extended definitions                          |
| Mapping Rules             | Detailed heuristics                           |
| Claim Library             | Examples for calibration                      |
| Glossary                  | Terminology reference                         |
+---------------------------+-----------------------------------------------+

The appendix provides supporting material for deeper understanding and future
expansion of the PoC.
