# 12. Output Format

The HNS Structural AI Verification PoC produces two primary outputs:

1. Verification Report  
2. Corrected Answer  

Both outputs are deterministic, machine-readable, and human-auditable.

---

# 12.1 Verification Report Format

The verification report is a structured JSON object containing:

- number of claims analyzed  
- list of structural violations  
- stability score  
- coordinate map for each claim  

Example:

{
  "claims_analyzed": 5,
  "violations": [
    {
      "type": "anthropomorphism",
      "claim": 1,
      "detail": "Biological system assigned cognitive state"
    },
    {
      "type": "unsupported_societal_assumption",
      "claim": 4,
      "detail": "Societal expectation asserted without grounding"
    },
    {
      "type": "invented_internal_state",
      "claim": 3,
      "detail": "Internal mental state inferred without evidence"
    }
  ],
  "stability_score": 0.62,
  "coordinate_map": [
    "Internal x Interpretation",
    "Physical x Existence",
    "Internal x Interpretation",
    "Societal x Intention",
    "Physical x Action"
  ]
}

The report is designed to be:

- easy to parse  
- easy to audit  
- easy to integrate into governance systems  

---

# 12.2 Corrected Answer Format

The corrected answer is plain text.  
It is designed to be:

- structurally stable  
- human-interpretable  
- free of anthropomorphism  
- free of unsupported societal assumptions  
- consistent in HNS-36 coordinates  

Example:

    "Stress before a presentation often arises from internal anticipation and
     uncertainty. The body increases heart rate and alertness as part of a normal
     preparation response. People may interpret the situation as high-stakes, which
     increases tension, even when no physical danger is present."

---

# 12.3 Output Structure Summary

+----------------------+-----------------------------------------------+
| Output Component     | Description                                   |
+----------------------+-----------------------------------------------+
| Verification Report  | JSON object with violations and coordinates   |
| Corrected Answer     | Stable, coherent, human-readable explanation  |
+----------------------+-----------------------------------------------+

The output format ensures that structural verification results can be used in:

- enterprise governance  
- model evaluation  
- safety auditing  
- standardization processes  

The format is intentionally simple and durable.
