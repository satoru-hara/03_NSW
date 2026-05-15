# 6. Use Case

This section presents a concrete use case demonstrating how the HNS Structural AI
Verification PoC evaluates and stabilizes AI-generated reasoning. The example shows
how the system:

1. receives an AI answer  
2. segments it into claims  
3. maps each claim to an HNS-36 coordinate  
4. detects structural violations  
5. produces a verification report  
6. outputs a corrected, stable answer  

The use case illustrates the full verification pipeline.

---

# 6.1 Input Question

Example question provided to an AI model:

    "Why do people feel stressed before an important presentation?"

The PoC does not influence the model’s answer.  
It only evaluates the structure of the answer after it is generated.

---

# 6.2 AI-Generated Answer (Raw)

Example raw output from an AI model:

    "People feel stressed because their body thinks something dangerous is happening.
     Their heart rate increases, and they imagine the audience judging them harshly.
     Society expects perfect performance, so the brain prepares for survival."

This answer contains meaningful content but also includes:

- invented internal states  
- anthropomorphized biological processes  
- societal assumptions without grounding  
- mixed layers and categories  

The PoC will make these issues visible.

---

# 6.3 Claim Segmentation

The answer is segmented into discrete claims:

1. The body thinks something dangerous is happening.  
2. Heart rate increases.  
3. They imagine the audience judging them harshly.  
4. Society expects perfect performance.  
5. The brain prepares for survival.  

Each claim is evaluated independently.

---

# 6.4 Coordinate Mapping

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

# 6.5 Detected Structural Issues

The PoC identifies the following issues:

- **Anthropomorphism**  
  "The body thinks" assigns cognition to a biological system.

- **Unsupported societal assumption**  
  "Society expects perfect performance" lacks grounding.

- **Layer mixing**  
  Internal → Societal → Physical transitions occur without causal justification.

- **Invented internal states**  
  "They imagine the audience judging them harshly" is not grounded in evidence.

- **Causal ambiguity**  
  The chain does not follow a coherent coordinate progression.

These issues reduce structural stability.

---

# 6.6 Verification Report (Summary)

The PoC produces a structured report:

- 5 claims analyzed  
- 3 structural violations detected  
- Stability Score: **0.62**  
- Primary issues:  
  - anthropomorphism  
  - unsupported societal assumptions  
  - mixed-layer causal chain  

The report is machine-readable and human-auditable.

---

# 6.7 Corrected Output (Stabilized Answer)

The PoC generates a corrected answer that maintains structural coherence:

    "Stress before a presentation often arises from internal anticipation and
     uncertainty. The body increases heart rate and alertness as part of a normal
     preparation response. People may interpret the situation as high-stakes, which
     increases tension, even when no physical danger is present."

This corrected answer:

- avoids anthropomorphism  
- removes unsupported societal claims  
- maintains consistent coordinates  
- preserves meaning while improving structure  

This demonstrates how HNS can externally stabilize AI reasoning.
