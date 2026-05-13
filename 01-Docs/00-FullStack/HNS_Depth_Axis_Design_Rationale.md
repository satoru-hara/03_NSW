# HNS Depth Axis Design Rationale  
### Why HNS‑144 and HNS‑864 Use Different Depth Axis Terminology  
Satoru Hara, Natural Structure Works (NSW)  
May 2026

---

## 1. Overview

The Human Natural Structure (HNS) framework defines two independent depth axes:

- **HNS‑144 (Observational Specification)**  
  - Abstract–Concrete Axis  
  - Fine–Coarse Axis  

- **HNS‑864 (Analytical Specification)**  
  - Structural–Dynamic Analysis Axis  
  - Macro–Micro Resolution Axis  

Although these axes are conceptually related, their terminology differs by design.  
This document explains the rationale behind the transformation and provides a non‑normative correspondence table.

---

## 2. Functional Difference Between Observation and Analysis

### 2.1 HNS‑144: Observation Depth Axes  
HNS‑144 defines depth as a property of **how a phenomenon is observed**:

- **Abstract** – conceptual altitude  
- **Concrete** – instance-level detail  
- **Coarse** – broad outline  
- **Fine** – micro-level distinctions  

These axes regulate the observer’s viewpoint to prevent distortions such as:

- Layer Collapse  
- Category Drift  
- Depth Confusion  
- Resolution Mixing  

Observation depth is therefore a **perceptual control mechanism**.

---

### 2.2 HNS‑864: Analysis Depth Axes  
HNS‑864 defines depth as a property of **how a phenomenon is analyzed**:

- **Structural** – stable, principle-based analysis  
- **Dynamic** – temporal or situational variation  
- **Macro** – large-scale patterns  
- **Micro** – fine-grained mechanisms  

These axes regulate analytical treatment, not perceptual stance.

Analysis depth is therefore a **processing control mechanism**.

---

## 3. Why the Terminology Must Differ

### 3.1 Observation ≠ Analysis  
Observation (144) and analysis (864) are different OS layers:

- **Observation precedes analysis.**  
- **Analysis must not rewrite observation.**

If both layers used identical terminology:

- the OS layering would collapse  
- structural independence would be lost  
- ISO/IEC requirements for non-overlapping conceptual domains would fail  

Therefore, terminology must diverge.

---

### 3.2 Avoiding False Equivalence  
A direct 1:1 mapping would incorrectly imply:

- Abstract = Structural  
- Concrete = Dynamic  
- Coarse = Macro  
- Fine = Micro  

This is **not strictly true**.  
The relationship is **derivative**, not identical.

Thus, HNS‑864 explicitly states:

> “This axis is derived from the Abstract–Concrete distinction defined in HNS‑144.”

Derived ≠ identical.  
Derived = transformed for analytical use.

---

### 3.3 Preventing Circular Definitions  
If the same terms were used:

- Observation depth would define analysis depth  
- Analysis depth would redefine observation depth  

This circularity would break the HNS OS architecture.

---

## 4. Non‑Normative Correspondence Table

Although the axes differ intentionally, the following table clarifies the conceptual lineage:

| HNS‑144 (Observation) | HNS‑864 (Analysis) | Relationship |
|------------------------|---------------------|--------------|
| **Abstract** | **Structural** | Structural analysis derives from abstract observation |
| **Concrete** | **Dynamic** | Dynamic analysis derives from concrete observation |
| **Coarse** | **Macro** | Macro analysis generalizes coarse observation |
| **Fine** | **Micro** | Micro analysis refines fine observation |

This table is **non‑normative** and provided only for interpretive clarity.

---

## 5. Why the Correspondence Table Is Not in the Specifications

The correspondence table is intentionally excluded from both HNS‑144 and HNS‑864 because:

1. **Specifications must preserve layer independence.**  
2. **A formal mapping would imply equivalence, not derivation.**  
3. **ISO/IEC standards require conceptual separation between observation and analysis.**  
4. **The mapping is interpretive, not structural.**  
5. **Rationale documents—not specifications—are the correct place for such explanations.**

Thus, the table belongs in a **Rationale** document, not in the normative specifications.

---

## 6. Conclusion

The depth axes of HNS‑144 and HNS‑864 differ because:

- Observation and analysis are distinct OS layers  
- Terminology must reflect functional separation  
- Direct equivalence would cause conceptual collapse  
- ISO/IEC requires non-overlapping normative domains  
- The relationship is derivative, not identical  

This document clarifies the design logic and provides a non‑normative correspondence table for readers who study the specifications together.

---

© 2026 Natural Structure Works (NSW)
