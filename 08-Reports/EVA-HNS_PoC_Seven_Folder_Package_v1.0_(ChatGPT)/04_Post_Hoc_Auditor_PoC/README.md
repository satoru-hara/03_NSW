# EVA Post-Hoc Auditor PoC v1.0

**Model-Agnostic Audit of Already Emitted AI Output**

Author: **Satoru Hara / Natural Structure Works (NSW)**  
Status: **Demonstration PoC / preliminary author-led verification**  
Version: **v1.0**

---

## Purpose

Demonstrate that EVA can operate in post-hoc mode by auditing already emitted AI output without modifying model weights or accessing logits.

---

## Main Demonstration Claim

> EVA-HNS can function as a vendor-independent post-hoc auditor for AI outputs.

---

## Files in This Folder

| File | Description |
|---|---|
| `report.md` | Full PoC report. |
| `test_set.csv` | Test prompts or checklist items. |
| `results_summary.csv` | Result table with HNS coordinates, SMS-6 grounding, EVA verdicts, and grounding scores. |
| `eva_audit_log.json` | Machine-readable EVA audit-log sample. |

---

## Recommended Use

Use this folder to inspect the PoC method, reproduce the table structure, and prepare future independent validation.

Recommended reading order:

1. `README.md`
2. `report.md`
3. `test_set.csv`
4. `results_summary.csv`
5. `eva_audit_log.json`

---

## What This PoC Demonstrates

EVA-HNS can function as a vendor-independent post-hoc auditor for AI outputs.

---

## What This PoC Does Not Claim

This PoC does not show real-time token attenuation or pre-decode intervention.

This folder should be read as a demonstration package, not as independent certification.

---

## Suggested Citation

```text
Hara, S. (2026). EVA Post-Hoc Auditor PoC v1.0: Model-Agnostic Audit of Already Emitted AI Output. Natural Structure Works.
```

---

## Attribution

Please maintain attribution to:

**Satoru Hara / Natural Structure Works (NSW)**

---

*End of README.md*
