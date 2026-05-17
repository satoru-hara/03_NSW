# EVA × EU AI Act Mapping Report
**External Verification Architecture — Technical Mapping to the EU AI Act**
Version 1.1 (Revised Edition)
Author: Satoru Hara / Natural Structure Works

---

> **Note on Scope**
> EVA (External Verification Architecture) is currently at conceptual design stage.
> The mappings in this document represent intended structural alignments, not
> implemented or certified compliance. Independent technical validation is required
> before use in formal standardization submissions.
> HNS-36, which EVA references as a reasoning baseline, has preliminary empirical
> support from an internal PoC (5 cases, single evaluator, May 2026).

---

## 0. Scope

This document provides a technical mapping between the requirements of the EU
Artificial Intelligence Act (Regulation (EU) 2024/1689) and the External
Verification Architecture (EVA).

It identifies how EVA's structural components — Verifiability, Transparency, and
Physical Immutability — are designed to address the Act's obligations for logging,
transparency, traceability, robustness, and human oversight.

This mapping is intended to support discussion of EN standards under CEN/CENELEC
JTC 21 and is offered as a conceptual contribution for review.

---

## 1. Purpose

The purpose of this document is to:

- Translate EU AI Act obligations into concrete engineering requirements
- Describe how EVA is designed to provide a compliant technical foundation
- Offer an implementation-oriented interpretation of the Act
- Support harmonized standards discussion for high-risk AI systems
- Establish a baseline for future conformance testing and certification design

---

## 2. Normative References

| Reference | Status |
|---|---|
| Regulation (EU) 2024/1689 — Artificial Intelligence Act | Normative |
| ISO/IEC 42001:2023 — AI Management System | Normative |
| ISO/IEC 23894:2023 — AI Risk Management | Normative |
| ISO/IEC 22989:2022 — AI Concepts and Terminology | Normative |
| W3C PROV-O (2013) — The PROV Ontology | Normative |

### Informative References (unpublished, author's own work)

| Reference | Status |
|---|---|
| Hara, S. (2026). External Verification Architecture (EVA) | Informative — conceptual design, not peer-reviewed |
| Hara, S. (2026). Human Natural Structure (HNS) | Informative — preliminary PoC, not peer-reviewed |

---

## 3. Terms and Definitions

**External Verification Architecture (EVA)**
A proposed structural framework intended to enable continuous, machine-readable,
tamper-resistant monitoring of AI reasoning through mechanisms independent of the
model's internal parameters. Currently at conceptual design stage.

**HNS (Human Natural Structure)**
A 36-cell structural coordinate system used as a reference baseline for classifying
AI reasoning steps. Preliminary empirical validation available (HNS-36 PoC v1.0,
May 2026).

**Sidecar Architecture**
A proposed parallel process that records reasoning evidence externally without
sharing memory with the AI model.

---

## 4. Executive Summary

EVA is designed as a structural mechanism for recording and validating AI system
reasoning in an external, machine-readable, tamper-resistant manner.

If implemented as designed, EVA is intended to support the core requirements of
the EU AI Act:

- Verifiability
- Traceability
- Transparency
- Accountability
- Logging obligations
- Human oversight
- Robustness and cybersecurity

This report presents a conceptual mapping between EU AI Act requirements and
EVA's architectural components. The mappings reflect design intent, not
demonstrated implementation.

---

## 5. EU AI Act → EVA Technical Mapping

### 5.1 Article 9 — Risk Management

**EU Requirement:**
Documented, traceable, and evidence-based risk management.

**EVA Design Alignment:**
- PROV-O based reasoning evidence
- HNS 36-cell structural classification
- RDF causal reasoning trace

**Intended Outcome:**
Externally verifiable risk-related decisions.

---

### 5.2 Article 10 — Data Governance

**EU Requirement:**
Data quality, lineage, and bias mitigation.

**EVA Design Alignment:**
- prov:used lineage for all inputs
- RDF descriptions of data sources

**Intended Outcome:**
Full traceability of data origin and usage.

---

### 5.3 Article 12 — Logging

**EU Requirement:**
Mandatory logging for high-risk AI systems.

**EVA Design Alignment:**
- JSON-LD / PROV-O log schema
- Sidecar-based external log generation
- No shared memory with the model

**Intended Outcome:**
Logs that cannot be altered by the AI system.

---

### 5.4 Article 13 — Transparency

**EU Requirement:**
Explainability and transparency of system behavior.

**EVA Design Alignment:**
- HNS 36-cell reasoning classification
- RDF reasoning trace showing evidence chains

**Intended Outcome:**
Explainability as a structural property of the system.

---

### 5.5 Article 14 — Human Oversight

**EU Requirement:**
Supervisors must understand and intervene.

**EVA Design Alignment:**
- Human-readable EVA log views
- Visualization of reasoning steps

**Intended Outcome:**
Supervisors gain actionable insight into AI reasoning.

---

### 5.6 Article 15 — Accuracy, Robustness, Cybersecurity

**EU Requirement:**
Protection against manipulation and tampering.

**EVA Design Alignment:**
- Signed logs
- TPM/FPGA-based attestation (design stage)
- Hardware-rooted integrity

**Intended Outcome:**
Tamper-resistant evidence of system operation.

---

### 5.7 Annex III — High-Risk AI Use Cases

**EU Requirement:**
Sector-specific obligations.

**EVA Design Alignment:**
- EVA profiles per domain (proposed)
- Domain-specific HNS coordinate assignments

**Intended Outcome:**
Consistent conformance testing framework across sectors.

---

## 6. Alignment Between EVA's Three Conditions and the EU AI Act

| EVA Condition | EU AI Act Articles | Technical Basis |
|---|---|---|
| Verifiability | Art. 12, Art. 15 | JSON-LD / PROV-O / Sidecar |
| Transparency | Art. 9, Art. 13 | HNS classification / RDF reasoning trace |
| Physical Immutability | Art. 12, Art. 15 | TPM/FPGA signatures / hardware isolation |

> **Note:** Physical Immutability (TPM/FPGA) is at design specification stage.
> Hardware implementation has not been validated.

---

## 7. Conformance Implications (Design Intent)

If implemented as designed, EVA is intended to enable measurable conformance
to the following EU AI Act requirements:

| Requirement | EVA Mechanism | Status |
|---|---|---|
| Logging (Art. 12) | JSON-LD logs provide machine-verifiable evidence | Design stage |
| Transparency (Art. 13) | HNS-based reasoning classification | Preliminary PoC |
| Robustness (Art. 15) | Hardware-rooted signatures prevent tampering | Design stage |
| Human Oversight (Art. 14) | Structured logs support supervisory intervention | Design stage |
| Risk Management (Art. 9) | PROV-O reasoning chains provide audit-ready evidence | Design stage |

---

## 8. Applicability to EN Standardization Discussion

EVA may be suitable for consideration in EN standardization because its design
incorporates:

- Machine-readable formats (JSON-LD / RDF)
- PROV-O compliance design
- Implementable conformance test structure
- Direct mapping to EU AI Act requirements
- Externality through Sidecar architecture
- A reference baseline (HNS-36) for reasoning evaluation

> **Important:** This document is a conceptual contribution. It has not been
> reviewed by CEN/CENELEC, ISO, or EU regulatory authorities. Formal
> standardization requires independent technical review and validation.

---

## 9. Limitations

| Limitation | Implication |
|---|---|
| EVA is at design stage | No implementation has been validated |
| HNS-36 has preliminary PoC only | n=5 cases, single evaluator |
| TPM/FPGA component unimplemented | Physical Immutability is design intent only |
| Self-authored references | No independent peer review of EVA or HNS |
| No CEN/CENELEC review | Standardization applicability is author's assessment |

---

## 10. Conclusion

EVA is designed as a structural mechanism that may directly address the EU AI
Act's requirements for logging, transparency, traceability, and human oversight.

Its machine-readable log formats, HNS-based structural reasoning model, and
external verification design make it a candidate for future CEN/CENELEC EN
standardization consideration, subject to independent technical validation.

The next required step is external review of the EVA design specification by
technical experts independent of the author.

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
