# EVA × EU AI Act Mapping Report
External Verification Architecture — Technical Mapping to the EU AI Act  
Version 1.1 (Standardization-Ready Edition)  
Author: Satoru Hara (NSW)

------------------------------------------------------------

# 0. Scope

This document provides a technical mapping between the requirements of the EU Artificial Intelligence Act (Regulation (EU) 2024/1689) and the External Verification Architecture (EVA).  
It identifies how EVA’s structural components—Verifiability, Transparency, and Physical Immutability—satisfy the Act’s obligations for logging, transparency, traceability, robustness, and human oversight.

This mapping is intended to support the development of EN standards under CEN/CENELEC JTC 21.

------------------------------------------------------------

# 1. Purpose

The purpose of this document is to:

- Translate EU AI Act obligations into concrete engineering requirements  
- Demonstrate how EVA provides a compliant technical foundation  
- Provide a machine-readable, implementation-ready interpretation of the Act  
- Support harmonized standards development for high-risk AI systems  
- Establish a baseline for conformance testing and certification

------------------------------------------------------------

# 2. Normative References

- Regulation (EU) 2024/1689 — Artificial Intelligence Act  
- ISO/IEC 42001:2023 — AI Management System  
- ISO/IEC 23894:2023 — AI Risk Management  
- ISO/IEC 22989:2022 — AI Concepts and Terminology  
- W3C PROV-O (2013) — The PROV Ontology  
- Hara, S. (2026). External Verification Architecture (EVA)  
- Hara, S. (2026). Human Natural Structure (HNS)

------------------------------------------------------------

# 3. Terms and Definitions

**External Verification Architecture (EVA)**  
A structural framework enabling continuous, machine-readable, tamper-resistant monitoring of AI reasoning through mechanisms independent of the model’s internal parameters.

**HNS (Human Natural Structure)**  
A 36‑cell structural coordinate system used as a reference baseline for classifying AI reasoning steps.

**Sidecar Architecture**  
A parallel process that records reasoning evidence externally without sharing memory with the AI model.

------------------------------------------------------------

# 4. Executive Summary

EVA provides a structural mechanism for recording and validating AI system reasoning in an external, machine-readable, tamper-resistant manner.

EVA directly supports the core requirements of the EU AI Act:

- Verifiability  
- Traceability  
- Transparency  
- Accountability  
- Logging obligations  
- Human oversight  
- Robustness and cybersecurity  

This report presents a 1:1 technical mapping between the EU AI Act and EVA’s architectural components.

------------------------------------------------------------

# 5. EU AI Act → EVA Technical Mapping

## 5.1 Article 9 — Risk Management

**EU Requirement:**  
Documented, traceable, and evidence-based risk management.

**EVA Alignment:**  
- PROV-O based reasoning evidence  
- HNS 36-cell structural classification  
- RDF causal reasoning trace  

**Outcome:**  
Externally verifiable risk-related decisions.

------------------------------------------------------------

## 5.2 Article 10 — Data Governance

**EU Requirement:**  
Data quality, lineage, and bias mitigation.

**EVA Alignment:**  
- `prov:used` lineage for all inputs  
- RDF descriptions of data sources  

**Outcome:**  
Full traceability of data origin and usage.

------------------------------------------------------------

## 5.3 Article 12 — Logging

**EU Requirement:**  
Mandatory logging for high-risk AI systems.

**EVA Alignment:**  
- JSON-LD / PROV-O log schema  
- Sidecar-based external log generation  
- No shared memory with the model  

**Outcome:**  
Logs cannot be altered by the AI system.

------------------------------------------------------------

## 5.4 Article 13 — Transparency

**EU Requirement:**  
Explainability and transparency of system behavior.

**EVA Alignment:**  
- HNS 36-cell reasoning classification  
- RDF reasoning trace showing evidence chains  

**Outcome:**  
Explainability becomes a structural property.

------------------------------------------------------------

## 5.5 Article 14 — Human Oversight

**EU Requirement:**  
Supervisors must understand and intervene.

**EVA Alignment:**  
- Human-readable EVA log views  
- Visualization of reasoning steps  

**Outcome:**  
Supervisors gain actionable insight.

------------------------------------------------------------

## 5.6 Article 15 — Accuracy, Robustness, Cybersecurity

**EU Requirement:**  
Protection against manipulation and tampering.

**EVA Alignment:**  
- Signed logs  
- TPM/FPGA-based attestation  
- Hardware-rooted integrity  

**Outcome:**  
Tamper-resistant evidence of system operation.

------------------------------------------------------------

## 5.7 Annex III — High-Risk AI Use Cases

**EU Requirement:**  
Sector-specific obligations.

**EVA Alignment:**  
- EVA profiles per domain  
- Domain-specific HNS coordinate assignments  

**Outcome:**  
Consistent conformance testing across sectors.

------------------------------------------------------------

# 6. Alignment Between EVA’s Three Conditions and the EU AI Act

| EVA Condition         | EU AI Act Articles | Technical Basis                          |
|-----------------------|--------------------|------------------------------------------|
| Verifiability         | Art.12, Art.15     | JSON-LD / PROV-O / Sidecar               |
| Transparency          | Art.9, Art.13      | HNS classification / RDF reasoning trace |
| Physical Immutability | Art.12, Art.15     | TPM/FPGA signatures / hardware isolation |

------------------------------------------------------------

# 7. Conformance Implications

EVA enables measurable conformance to the EU AI Act:

- **Logging (Art.12):**  
  JSON-LD logs provide machine-verifiable evidence.

- **Transparency (Art.13):**  
  HNS-based reasoning classification ensures explainability.

- **Robustness (Art.15):**  
  Hardware-rooted signatures prevent tampering.

- **Human Oversight (Art.14):**  
  Structured logs support supervisory intervention.

- **Risk Management (Art.9):**  
  PROV-O reasoning chains provide audit-ready evidence.

------------------------------------------------------------

# 8. Applicability to EN Standardization

EVA is suitable for adoption as an EN standard because it provides:

- Machine-readable formats (JSON-LD / RDF)  
- PROV-O compliance  
- Implementable conformance tests  
- Direct mapping to EU AI Act requirements  
- Externality through Sidecar architecture  
- A reference baseline (HNS) for reasoning evaluation  

These characteristics align with CEN/CENELEC expectations for technical standards supporting the EU AI Act.

------------------------------------------------------------

# 9. Conclusion

EVA offers a direct, technically grounded implementation of the EU AI Act’s requirements.  
Its machine-readable logs, structural reasoning model (HNS), and external verification mechanisms make it a strong candidate for CEN/CENELEC EN standardization.

------------------------------------------------------------
