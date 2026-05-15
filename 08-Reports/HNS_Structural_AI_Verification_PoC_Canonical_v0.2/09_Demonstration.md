# 9. Demonstration

This section provides a full demonstration of the HNS Structural AI Verification PoC
in action. The demonstration shows:

1. the AI-generated answer  
2. segmentation into claims  
3. mapping to HNS-36 coordinates  
4. detection of structural violations  
5. generation of a verification report  
6. corrected, stable output  

The demonstration uses the same example question as Section 6 for consistency.

---

# 9.1 Input Question

    "Why do people feel stressed before an important presentation?"

The PoC does not influence the model’s answer.  
It evaluates the structure after the answer is generated.

---

# 9.2 AI-Generated Answer (Raw)

Example output from an AI model:

    "People feel stressed because their body thinks something dangerous is happening.
     Their heart rate increases, and they imagine the audience judging them harshly.
     Society expects perfect performance, so the brain prepares for survival."

This answer contains meaningful content but also includes structural issues:

- anthropomorphism  
- invented internal states  
- unsupported societal assumptions  
- mixed-layer causal chain  

The PoC makes these issues visible.

---

# 9.3 Claim Segmentation

The answer is segmented into discrete claims:

1. The body thinks something dangerous is happening.  
2. Heart rate increases.  
3. They imagine the audience judging them harshly.  
4. Society expects perfect performance.  
5. The brain prepares for survival.

Each claim is evaluated independently.

---

# 9.4 Coordinate Mapping

Each claim is mapped to an HNS-36 coordinate:

+-----+---------------------------------------------------------------+---------------------------+
| No. | Claim                                                         | HNS Coordinate            |
+-----+---------------------------------------------------------------+---------------------------+
| 1   | The body thinks something dangerous is happening.             | Internal x Interpretation |
| 2   | Heart rate increases.                                         | Physical x Existence      |
| 3   | They imagine the audience judging them harshly.               | Internal x Interpretation |
| 4   | Society expects perfect performance.                          | Societal x Intention      |
| 5   | The brain prepares for survival.                              | Physical x Action         |
+-----+---------------------------------------------------------------+---------------------------+

The mapping reveals structural inconsistencies.

---

# 9.5 Structural Violations Detected

The PoC identifies the following issues:

### 1. Anthropomorphism
"The body thinks" assigns cognition to a biological system.

### 2. Unsupported societal assumption
"Society expects perfect performance" lacks grounding.

### 3. Invented internal states
"They imagine the audience judging them harshly" is not supported by evidence.

### 4. Layer mixing
Internal → Societal → Physical transitions occur without causal justification.

### 5. Causal ambiguity
The chain does not follow a coherent coordinate progression.

These issues reduce structural stability.

---

# 9.6 Verification Report (Full Example)

The PoC produces a structured verification report:

