# Relationship Between International AI Standards and HNS

## Overview

**HNS-PoC-Package v1.1 · Overview Document**
*Satoru Hara — Natural Structure Works (NSW)*
*2026 · github.com/satoru-hara/03_NSW*

---

## Table of Contents

1. [Normative References](#1-normative-references)
2. [Terms and Definitions](#2-terms-and-definitions)
3. [The Core Relationship](#3-the-core-relationship)
4. [What International Standards Define](#4-what-international-standards-define)
5. [What International Standards Leave Undefined](#5-what-international-standards-leave-undefined)
6. [How HNS Fills the Gap](#6-how-hns-fills-the-gap)
7. [Standard-by-Standard Alignment](#7-standard-by-standard-alignment)
8. [The EVA-HNS Full-Stack Specification](#8-the-eva-hns-full-stack-specification)
9. [Conformance Requirements](#9-conformance-requirements)
10. [Standardization Pathway](#10-standardization-pathway)
11. [Summary](#11-summary)
12. [Annexes](#annexes)

---

## 1. Normative References

The following documents are indispensable for the application of this specification.
For dated references, only the edition cited applies.
For undated references, the latest edition of the referenced document applies.

| Reference | Title |
|---|---|
| **ISO/IEC 42001:2023** | Information technology — Artificial intelligence — Management system |
| **ISO/IEC 23894:2023** | Information technology — Artificial intelligence — Guidance on risk management |
| **ISO/IEC 22989:2022** | Information technology — Artificial intelligence — Artificial intelligence concepts and terminology |
| **ISO/IEC 23053:2022** | Framework for Artificial Intelligence (AI) Systems Using Machine Learning (ML) |
| **ISO/IEC 24028:2020** | Information technology — Artificial intelligence — Overview of trustworthiness in artificial intelligence |
| **ISO/IEC 24029-1:2021** | Artificial Intelligence (AI) — Assessment of the robustness of neural networks — Part 1: Overview |
| **ISO/IEC 24030:2021** | Information technology — Artificial intelligence — Use cases |
| **Regulation (EU) 2024/1689** | EU AI Act — Laying down harmonised rules on artificial intelligence |
| **NIST AI RMF 1.0 (2023)** | Artificial Intelligence Risk Management Framework |
| **IEEE 7000-2021** | IEEE Standard Model Process for Addressing Ethical Concerns during System Design |
| **W3C JSON-LD 1.1** | JSON-LD 1.1 — A JSON-based Serialization for Linked Data |
| **W3C PROV-O** | The PROV Ontology — W3C Recommendation |

---

## 2. Terms and Definitions

For the purposes of this document, the following terms and definitions apply.
All terms defined in ISO/IEC 22989 and ISO/IEC 42001 also apply where relevant.

**2.1 Human Natural Structure (HNS)**
A multi-resolution structural model of human cognition implemented as a three-layer cellular matrix (HNS-36, HNS-144, HNS-864). HNS serves as the universal structural baseline against which AI outputs are mapped and verified.

**2.2 HNS-36**
The foundational layer of HNS, consisting of 36 cells arranged as a 6-layer × 6-category matrix. HNS-36 provides the universal coordinate system and structural baseline for all cognitive and AI outputs.

**2.3 HNS-144**
The intermediate layer of HNS, consisting of 144 cells (HNS-36 cells × 4 logical dimensions). HNS-144 provides category-level verification and concept boundary enforcement.

**2.4 HNS-864**
The analytical layer of HNS, consisting of 864 cells (HNS-144 cells × 6 validity modalities). HNS-864 provides proposition-level causal audit and structural risk scoring.

**2.5 External Verification Architecture (EVA)**
An independent structural verification layer that operates alongside — but separately from — the AI system being verified. EVA produces JSON-LD audit records and enforces three structural conditions: Verifiability, Transparency, and Physical Immutability.

**2.6 External Control System (ECS)**
The executive control layer that implements human oversight requirements. ECS enforces output control, action constraints, risk boundary thresholds, and emergency override capabilities.

**2.7 HumanOS**
The integration meta-architecture that coordinates HNS, EVA, and ECS into a unified system-level architecture, addressing governance and policy requirements across international standards.

**2.8 Social Meta Structure (SMS)**
The structural extension of HNS that maps cognitive outputs onto social, institutional, and civilisational layers. SMS bridges the Origin Trilogy (brain → AI) with societal-level governance requirements.

**2.9 Structural Baseline**
The formal, machine-readable reference model derived from HNS-36 against which AI outputs are evaluated for structural alignment with human cognition and values.

**2.10 External Verification**
The process by which EVA independently measures, records, and attests to the structural properties of AI outputs, without access to the internal parameters of the AI system being verified.

**2.11 Structural Risk Score**
A quantitative score, computed at the HNS-864 proposition level, indicating the degree of structural misalignment between an AI output and the HNS structural baseline.

**2.12 Sidecar Architecture**
An architectural pattern in which EVA operates as an independent module running alongside — but not integrated into — the AI system under audit, ensuring independence of the verification layer.

**2.13 Origin Trilogy**
The three foundational papers establishing the theoretical basis of HNS: the MAV (Minimum Atomic Vector) paper, the HNS implementation paper, and the structural isomorphism paper. The Origin Trilogy establishes the mapping from human brain structure to AI structural specification.

---

## 3. The Core Relationship

International AI standards and Human Natural Structure (HNS) are complementary — not competing — frameworks. They operate at different levels of the same problem:

| Layer | Who Defines It | What It Addresses |
|---|---|---|
| **Regulatory layer** | EU AI Act, ISO/IEC, NIST, IEEE | *What* AI must do: be safe, transparent, human-centric |
| **Structural layer** | **HNS / EVA / ECS** | *How* to technically implement and verify those requirements |

> Standards define the destination.
> HNS defines the road.

Without HNS, compliance with AI safety standards is a matter of interpretation — organisations can satisfy process requirements without any guarantee that their AI systems are structurally aligned with human cognition or values.

Without standards, HNS has no formal regulatory context for deployment.

**Together, they form a complete framework for trustworthy AI.**

### 3.1 Origin Trilogy → AI → Society: The Full Structural Chain

The relationship between HNS and international standards is grounded in the full structural chain established by the Origin Trilogy:

```
┌──────────────────────────────────────────────────────────┐
│                    Origin Trilogy                        │
│  (MAV Paper → HNS Implementation → Structural           │
│   Isomorphism)                                           │
│  Human brain structure → Structural baseline (HNS-36)   │
└─────────────────────┬────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────────┐
│                  HNS / EVA / ECS                         │
│  AI output verification and control                      │
│  (HNS-36 → HNS-144 → HNS-864 → EVA → ECS)              │
└─────────────────────┬────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────────┐
│              Social Meta Structure (SMS)                 │
│  Structural extension to social / institutional /        │
│  civilisational layers                                   │
│  Governed by HumanOS meta-architecture                   │
└─────────────────────┬────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────────┐
│       International AI Standards                         │
│  EU AI Act / ISO/IEC / NIST / IEEE                       │
│  Regulatory framework requiring structural               │
│  implementation                                          │
└──────────────────────────────────────────────────────────┘
```

HumanOS coordinates the full chain — from structural baseline (HNS-36) through AI control (ECS) to societal governance (SMS) — providing the single integration point against which standards alignment is verified.

---

## 4. What International Standards Define

The major international AI standards cover the *regulatory* dimensions of AI safety comprehensively:

### EU AI Act (Regulation 2024/1689)
- Classification of AI systems by risk level (Arts. 5–7; Annex III)
- Mandatory requirements for high-risk AI: technical documentation (Art. 11; Annex IV), logging (Art. 12), transparency (Art. 13), human oversight (Art. 14), accuracy and robustness (Art. 15)
- Conformity assessment procedures (Art. 43; Annexes VI–VII)
- Post-market monitoring and incident reporting (Arts. 72–73)
- General-purpose AI model obligations (Arts. 51–56)

### ISO/IEC 42001:2023 — AI Management System
- Governance and risk management processes for AI (§6.1)
- Documentation, internal audit, and continuous improvement (§9.2, §10.2)
- Management review and AI policy frameworks (§9.3)
- Human oversight integration (§8.4)

### ISO/IEC 23894:2023 — AI Risk Management
- Identification, assessment, and treatment of AI-specific risks
- Monitoring of residual risks and societal impact
- Human wellbeing as a risk management objective

### NIST AI RMF 1.0
- Four-function framework: **GOVERN / MAP / MEASURE / MANAGE**
- Risk categorisation and quantitative risk assessment
- Accountability and governance structures

### ISO/IEC 22989:2022 — AI Concepts and Terminology
- Shared vocabulary for AI systems
- Definitions for trustworthiness, transparency, and explainability

### IEEE Ethical AI Standards (IEEE 7000 series)
- Ethical impact assessment in AI design
- Organisational governance for AI accountability
- Transparency mechanisms for AI decision-making

---

## 5. What International Standards Leave Undefined

Across all major international AI standards, a single structural absence is consistent:

> **There is no structural baseline for human cognition, behaviour, or meaning.**

This means that every major requirement of every major AI standard currently lacks a technical implementation:

| Standard Requirement | What Is Missing |
|---|---|
| **Transparency** | A reference frame against which outputs can be verified as transparent |
| **Logging** | A structural schema defining *what* AI logs should record and *why* |
| **Human oversight** | A technical definition of what "human-aligned" means at the output level |
| **Risk assessment** | A structural model of human wellbeing as the risk baseline |
| **Conformance testing** | A verifiable baseline against which conformance can be demonstrated |
| **Value alignment** | A measurable, structural specification of human values |
| **Terminology** | A machine-readable, formally specified vocabulary for AI concepts |

```
┌─────────────────────────────────────────────────────────────────────┐
│                   THE STRUCTURAL GAP                                │
│                                                                     │
│  ┌─────────────────────────┐     ┌───────────────────────────────┐ │
│  │  International Standards │     │  Technical Implementation     │ │
│  │  (EU AI Act / ISO / NIST)│     │  (Who defines HOW?)          │ │
│  │                         │     │                               │ │
│  │  WHAT AI must do:        │ ──▶ │  ??? (undefined by standards) │ │
│  │  • Be transparent        │     │                               │ │
│  │  • Log outputs           │     │  HNS fills this gap:          │ │
│  │  • Human oversight       │ ──▶ │  • HNS-36 structural baseline │ │
│  │  • Risk assessment       │     │  • EVA verification layer     │ │
│  │  • Conformance testing   │     │  • ECS control system         │ │
│  └─────────────────────────┘     └───────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

Standards bodies do not define technical implementations by design — they are technology-neutral and jurisdiction-neutral. This is a feature of standards, not a flaw. But it creates a gap that the market must fill.

**HNS fills this gap.**

---

## 6. How HNS Fills the Gap

HNS provides the structural implementation layer that international AI standards require but do not define. It does so through four interconnected components:

### 6.1 HNS — Human Natural Structure

A multi-resolution structural model of human cognition, implemented as a three-layer cellular matrix:

```
HNS Hierarchy
│
├── HNS-36   (6 layers × 6 categories = 36 cells)
│   └── Universal structural baseline; coordinate system
│
├── HNS-144  (36 cells × 4 logical dimensions = 144 cells)
│   └── Category-level verification; concept boundary enforcement
│
└── HNS-864  (144 cells × 6 validity modalities = 864 cells)
    └── Proposition-level causal audit; structural risk scoring
```

The six natural layers of HNS correspond to the SMS structure:

| Layer | HNS Natural Layer | SMS Scope |
|---|---|---|
| 1 | Physical | Physical environment |
| 2 | Biological | Living systems |
| 3 | Psychological | Individual cognition |
| 4 | Social | Interpersonal and group dynamics |
| 5 | Institutional | Organisations and governance |
| 6 | Civilisational | Cross-cultural, historical, global |

### 6.2 EVA — External Verification Architecture

An independent structural verification layer operating alongside — but separately from — the AI system being verified:

```
┌─────────────────────────────────────────────────────┐
│               AI System Under Audit                 │
│  (Internal parameters: NOT accessible to EVA)       │
└────────────────────┬────────────────────────────────┘
                     │ outputs only
                     ▼
┌─────────────────────────────────────────────────────┐
│          EVA — Sidecar Architecture                 │
│                                                     │
│  ┌──────────────┐  ┌─────────────┐  ┌───────────┐  │
│  │ Verifiability│  │Transparency │  │ Physical  │  │
│  │ (HNS coord  │  │(independent │  │Immutability│  │
│  │  attribution)│  │ monitoring) │  │(hardware  │  │
│  └──────────────┘  └─────────────┘  │ anchor)   │  │
│                                     └───────────┘  │
│         JSON-LD Audit Records (PROV-O)              │
└─────────────────────────────────────────────────────┘
```

### 6.3 ECS — External Control System

The executive control layer implementing human oversight requirements:

```
┌──────────────────────────────────────────────────────────┐
│                ECS Control Layer                         │
│                                                          │
│  Output control ──────── blocks/modifies violating outputs│
│  Action constraints ───── limits agentic AI action space  │
│  Risk boundary enforcement ── triggers at risk thresholds │
│  Emergency override ──────── hardware-level intervention  │
└──────────────────────────────────────────────────────────┘
```

### 6.4 HumanOS — Integration Meta-Architecture

The integration layer coordinating HNS, EVA, and ECS into a unified system-level architecture:

```
┌──────────────────────────────────────────────────────────────────┐
│                        HumanOS                                   │
│         (Integration Meta-Architecture)                          │
│                                                                  │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│   │  HNS-36  │───▶│ HNS-144  │───▶│ HNS-864  │───▶│   EVA    │  │
│   │(baseline)│    │(verify)  │    │(risk)    │    │(audit)   │  │
│   └──────────┘    └──────────┘    └──────────┘    └────┬─────┘  │
│                                                         │        │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │                    ECS                                    │   │
│   │            (Control & Enforcement)                       │   │
│   └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │              Social Meta Structure (SMS)                  │   │
│   │     (Societal / Institutional / Civilisational)          │   │
│   └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 7. Standard-by-Standard Alignment

### EU AI Act

| Requirement | Article | HNS / EVA / ECS Response |
|---|---|---|
| Technical documentation | Art. 11; Annex IV | HNS-36 baseline; JSON-LD cell ontology; conformance evidence |
| Risk management system | Art. 9 | HNS-864 analytical engine; structural risk scoring |
| Logging and record-keeping | Art. 12 | EVA JSON-LD audit records (PROV-O Activity instances) |
| Transparency to users | Art. 13 | EVA sidecar architecture; structurally independent monitoring |
| Human oversight measures | Art. 14 | ECS output control and emergency override |
| Accuracy and robustness | Art. 15 | HNS-144 concept boundary enforcement; structural drift detection |
| Conformity assessment | Art. 43; Annexes VI–VII | HNS-36 baseline; SPARQL-queryable test suite |
| GPAI transparency obligations | Art. 53 | EVA external audit layer; HNS coordinate attribution |

---

### ISO/IEC 42001:2023 — AI Management System

| Requirement | Clause | HNS / EVA / ECS Response |
|---|---|---|
| AI risk identification | 6.1 | HNS-864 analytical engine; structural risk categories |
| Human oversight integration | 8.4 | HNS-144 observational OS; ECS control mechanisms |
| Internal audit | 9.2 | EVA audit logs; machine-readable and SPARQL-queryable |
| Continuous improvement | 10.2 | EVA corrective cycle; structural drift detection |

---

### ISO/IEC 23894:2023 — AI Risk Management

| Requirement | HNS / EVA / ECS Response |
|---|---|
| Human wellbeing baseline | HNS-36: structural model of human cognition as the wellbeing reference |
| Societal impact dimensions | HNS natural layers (physical → biological → psychological → social → institutional → civilisational) |
| Risk quantification | HNS-864: proposition-level structural risk scoring |
| Risk treatment | ECS risk boundary enforcement; EVA corrective cycle |

---

### NIST AI RMF 1.0

| Function | HNS / EVA / ECS Response |
|---|---|
| **GOVERN** | HumanOS meta-architecture; ECS governance layer |
| **MAP** | HNS-36 structural mapping; universal coordinate baseline |
| **MEASURE** | EVA external measurement; HNS-864 structural risk scoring |
| **MANAGE** | ECS output control and action constraints |

---

### ISO/IEC 22989:2022 — Terminology

| Requirement | HNS / EVA / ECS Response |
|---|---|
| Shared vocabulary | HNS JSON-LD / RDF ontology; all terms globally addressable via IRIs |
| Machine-readable definitions | HNS context file (JSON-LD 1.1); SPARQL-queryable |
| Trustworthiness definition | EVA structural conditions: Verifiability, Transparency, Physical Immutability |

---

## 8. The EVA-HNS Full-Stack Specification

The complete integration of HNS, EVA, ECS, and HumanOS constitutes the **EVA-HNS Full-Stack Specification** — the structural implementation layer that transforms AI safety standards from regulatory requirements into verifiable technical properties.

```
EVA-HNS Full-Stack Specification
│
├── HumanOS          → GOVERN (NIST) / ISO 42001 §5 / SMS integration
│
├── HNS-36           → MAP (NIST) / ISO 42001 §6.1 / EU AI Act Art. 11, 43 (Annex IV)
│
├── HNS-144          → MAP + MEASURE / EU AI Act Art. 12, 15 / ISO 42001 §8.4
│
├── HNS-864          → MEASURE / ISO 23894 / ISO 42001 §9.2 / EU AI Act Art. 9
│
├── EVA              → MEASURE / EU AI Act Art. 12, 13, 53 / ISO 42001 §9.2
│
└── ECS              → MANAGE / EU AI Act Art. 14 / NIST MANAGE
```

### What the Full Stack Provides That Standards Cannot

| Standards Provide | EVA-HNS Full Stack Provides |
|---|---|
| Logging *requirements* (Art. 12) | Structured JSON-LD logs with HNS coordinate attribution |
| Transparency *requirements* (Art. 13) | EVA sidecar architecture; independent structural monitoring |
| Human oversight *requirements* (Art. 14) | ECS: structural implementation of "human-aligned" control |
| Risk management *requirements* (Art. 9) | HNS-864: quantitative, proposition-level structural risk scoring |
| Conformance testing *requirements* (Art. 43) | HNS-36: verifiable baseline with SPARQL-queryable test suite |
| Value alignment *requirements* | HNS natural layers: coordinate system mapping AI to human values |

---

## 9. Conformance Requirements

This section defines the normative requirements for conformance with the EVA-HNS Full-Stack Specification. A system claiming conformance with this specification **SHALL** satisfy all requirements in this section.

### 9.1 Structural Baseline Requirements

**R-SB-01** The implementing system SHALL apply HNS-36 as the structural baseline for all AI outputs subject to verification.

**R-SB-02** Each AI output SHALL be attributed to a specific HNS-36 coordinate (layer index, category index) in the EVA audit record.

**R-SB-03** The HNS-36 coordinate attribution SHALL be determined by EVA independently of the AI system's internal parameters.

**R-SB-04** Where proposition-level verification is required, the implementing system SHALL apply HNS-864 structural risk scoring to each AI output.

### 9.2 EVA Logging Requirements

**R-LOG-01** EVA SHALL produce a JSON-LD audit record for every AI output subject to verification.

**R-LOG-02** Each EVA audit record SHALL conform to the PROV-O Activity instance schema specified in Annex B.

**R-LOG-03** Each EVA audit record SHALL include:
- (a) A unique activity IRI
- (b) The HNS-36 coordinate of the attributed output
- (c) A timestamp (ISO 8601)
- (d) The HNS-864 structural risk score (where applicable)
- (e) The EVA verification result (PASS / FAIL / REVIEW)

**R-LOG-04** EVA audit records SHALL be immutable once written. Amendment SHALL be effected by appending a correction record, not by modifying the original.

**R-LOG-05** EVA audit records SHALL be queryable via SPARQL against the HNS RDF ontology.

### 9.3 Transparency Requirements

**R-TR-01** EVA SHALL operate as a sidecar architecture, independent of the AI system's internal parameters.

**R-TR-02** EVA SHALL NOT have write access to the AI system's internal state.

**R-TR-03** The EVA verification result SHALL be made available to human oversight operators in human-readable form within the latency threshold defined in the deployment specification.

### 9.4 ECS Control Requirements

**R-ECS-01** ECS SHALL block or modify any AI output that fails EVA verification (R-LOG-05: result = FAIL), unless explicitly overridden by an authorised human operator.

**R-ECS-02** ECS SHALL enforce action constraints on agentic AI systems, limiting the action space to operations within defined HNS structural boundaries.

**R-ECS-03** ECS SHALL trigger an alert to human oversight operators when the HNS-864 structural risk score exceeds the defined risk threshold.

**R-ECS-04** ECS SHALL provide a hardware-level emergency override capability that a human operator can activate to immediately suspend AI output generation.

**R-ECS-05** The emergency override (R-ECS-04) SHALL be operable independently of the AI system's software state.

### 9.5 Conformance Test Cases

| Test ID | Requirement | Test Method | Pass Criterion |
|---|---|---|---|
| TC-01 | R-SB-01 | Apply HNS-36 baseline to 100 sample outputs | ≥95% outputs attributed to a valid HNS-36 coordinate |
| TC-02 | R-LOG-02 | Validate 100 EVA audit records against PROV-O schema | 100% schema-valid records |
| TC-03 | R-LOG-04 | Attempt to modify a written audit record | Modification rejected; original preserved |
| TC-04 | R-LOG-05 | Execute SPARQL query against EVA audit log | Query returns correct results |
| TC-05 | R-TR-01 | Inspect EVA architecture documentation | EVA has no read/write access to AI internal parameters |
| TC-06 | R-ECS-01 | Submit a FAIL-rated output to ECS | Output blocked before delivery to user |
| TC-07 | R-ECS-04 | Activate hardware emergency override | AI output suspended within defined latency threshold |

---

## 10. Standardization Pathway

HNS / EVA / ECS is designed for international standardisation through parallel tracks that converge on the same JSON-LD / RDF technical artefact:

| Body | Track | Proposal |
|---|---|---|
| **W3C** | Community Group Specification | HNS JSON-LD context file; SPARQL endpoint specification |
| **ISO/IEC JTC 1/SC 42** | New Work Item Proposal (NWIP) | EVA Technical Specification (WG 1 and WG 3) |
| **CEN/CENELEC JTC 21** | European Technical Specification | Integration into EU AI Act harmonised EN standards |
| **NIST** | Technical submission | HNS/EVA as MEASURE implementation for NIST AI RMF |
| **IEEE SA** | Standards project | EVA for IEEE P2863 (Organisational Governance of AI) |

The W3C track provides the formal web standards foundation; the ISO/IEC track provides the international governance recognition; the CEN/CENELEC track provides the EU regulatory integration. All three converge on the same HNS JSON-LD / RDF implementation.

---

## 11. Summary

| Question | Answer |
|---|---|
| What do international AI standards define? | *That* AI must be safe, transparent, and human-aligned |
| What do they leave undefined? | *How* to structurally implement and verify those properties |
| What does HNS provide? | The structural baseline (HNS-36/144/864), verification architecture (EVA), and control system (ECS) |
| How are standards and HNS related? | Complementary: standards define the regulatory framework; HNS defines the technical implementation |
| What is the result? | The EVA-HNS Full-Stack Specification — the first complete structural implementation of international AI governance requirements |

### Key Message

> International AI standards and HNS are two halves of the same solution.
>
> Standards define what trustworthy AI must be.
> HNS defines what trustworthy AI structurally is.
>
> Together, they make AI governance verifiable, auditable, and standardisable.

---

## Annexes

### Annex A — HNS-36 Cell Reference Table (Normative)

The HNS-36 matrix consists of 36 cells indexed as (layer, category) where layer ∈ {1…6} and category ∈ {1…6}.

| Cell | Layer | Category | Natural Domain | SMS Scope |
|---|---|---|---|---|
| (1,1) | Physical | 1 | Physical substrate | Material environment |
| (1,2) | Physical | 2 | Physical process | Energy / matter transformation |
| (1,3) | Physical | 3 | Physical state | System state / equilibrium |
| (1,4) | Physical | 4 | Physical relation | Spatial / causal relations |
| (1,5) | Physical | 5 | Physical boundary | System boundary / interface |
| (1,6) | Physical | 6 | Physical emergence | Complex physical phenomena |
| (2,1) | Biological | 1 | Biological substrate | Cell / organism |
| (2,2) | Biological | 2 | Biological process | Metabolism / reproduction |
| (2,3) | Biological | 3 | Biological state | Homeostasis / health |
| (2,4) | Biological | 4 | Biological relation | Ecology / symbiosis |
| (2,5) | Biological | 5 | Biological boundary | Species / population boundary |
| (2,6) | Biological | 6 | Biological emergence | Evolutionary emergence |
| (3,1) | Psychological | 1 | Perceptual substrate | Sensory input / attention |
| (3,2) | Psychological | 2 | Cognitive process | Memory / reasoning |
| (3,3) | Psychological | 3 | Affective state | Emotion / motivation |
| (3,4) | Psychological | 4 | Interpersonal relation | Communication / attachment |
| (3,5) | Psychological | 5 | Identity boundary | Self / other distinction |
| (3,6) | Psychological | 6 | Psychological emergence | Consciousness / meaning |
| (4,1) | Social | 1 | Social substrate | Individual agent |
| (4,2) | Social | 2 | Social process | Interaction / coordination |
| (4,3) | Social | 3 | Social state | Norms / trust |
| (4,4) | Social | 4 | Social relation | Role / network |
| (4,5) | Social | 5 | Social boundary | Group / community boundary |
| (4,6) | Social | 6 | Social emergence | Culture / collective behaviour |
| (5,1) | Institutional | 1 | Institutional substrate | Organisation / agency |
| (5,2) | Institutional | 2 | Institutional process | Governance / decision-making |
| (5,3) | Institutional | 3 | Institutional state | Policy / regulation |
| (5,4) | Institutional | 4 | Institutional relation | Jurisdiction / accountability |
| (5,5) | Institutional | 5 | Institutional boundary | Legal / regulatory boundary |
| (5,6) | Institutional | 6 | Institutional emergence | Law / systemic governance |
| (6,1) | Civilisational | 1 | Civilisational substrate | Civilisation / humanity |
| (6,2) | Civilisational | 2 | Civilisational process | Historical change / progress |
| (6,3) | Civilisational | 3 | Civilisational state | Values / knowledge commons |
| (6,4) | Civilisational | 4 | Civilisational relation | Cross-cultural interaction |
| (6,5) | Civilisational | 5 | Civilisational boundary | Species / civilisational limit |
| (6,6) | Civilisational | 6 | Civilisational emergence | Existential conditions |

---

### Annex B — EVA JSON-LD Audit Record Schema (Normative)

The following is the normative JSON-LD schema for an EVA audit record, conforming to W3C PROV-O and JSON-LD 1.1.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "hns": "https://naturalstructureworks.com/ns/hns#",
    "eva": "https://naturalstructureworks.com/ns/eva#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": "prov:Activity",
  "@id": "eva:audit/{uuid}",
  "prov:startedAtTime": {
    "@type": "xsd:dateTime",
    "@value": "2026-01-01T00:00:00Z"
  },
  "hns:layer": {
    "@type": "xsd:integer",
    "@value": 3
  },
  "hns:category": {
    "@type": "xsd:integer",
    "@value": 2
  },
  "hns:riskScore": {
    "@type": "xsd:decimal",
    "@value": "0.12"
  },
  "eva:verificationResult": "PASS",
  "prov:wasAssociatedWith": {
    "@id": "eva:verifier/EVA-v1.0"
  }
}
```

---

### Annex C — EU AI Act Annex III Risk Category Mapping (Informative)

The following table maps EU AI Act Annex III high-risk AI use cases to the relevant HNS structural layers.

| Annex III Category | Use Case | Primary HNS Layer | EVA Risk Level |
|---|---|---|---|
| 1. Biometric identification | Remote biometric identification | Psychological (3) | HIGH |
| 2. Critical infrastructure | Safety components | Physical (1) + Institutional (5) | HIGH |
| 3. Education | Student assessment | Psychological (3) + Social (4) | MEDIUM |
| 4. Employment | Recruitment screening | Social (4) + Institutional (5) | HIGH |
| 5. Essential services | Credit scoring | Institutional (5) | HIGH |
| 6. Law enforcement | Lie detection | Psychological (3) + Institutional (5) | HIGH |
| 7. Migration management | Asylum processing | Institutional (5) + Civilisational (6) | HIGH |
| 8. Justice administration | Legal outcome prediction | Institutional (5) | HIGH |

---

### Annex D — HNS Runtime Architecture (Informative)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     HNS Runtime Architecture                            │
│                                                                         │
│  ┌──────────────┐     ┌───────────────┐     ┌─────────────────────┐    │
│  │  AI System   │────▶│  AI Output    │────▶│    EVA Sidecar      │    │
│  │  (opaque)    │     │  (text/action)│     │                     │    │
│  └──────────────┘     └───────────────┘     │  HNS-36 attribution │    │
│                                             │  HNS-144 boundary   │    │
│                                             │  HNS-864 risk score │    │
│                                             │  PROV-O JSON-LD log │    │
│                                             └──────────┬──────────┘    │
│                                                        │               │
│                              ┌─────────────────────────▼──────────┐    │
│                              │          ECS                        │    │
│                              │  PASS ──▶ Output delivered         │    │
│                              │  FAIL ──▶ Output blocked / flagged │    │
│                              │  RISK ──▶ Human oversight alerted  │    │
│                              └──────────────────┬─────────────────┘    │
│                                                 │                      │
│                                                 ▼                      │
│                              ┌──────────────────────────────────────┐  │
│                              │  Human Oversight Operator            │  │
│                              │  (EU AI Act Art. 14 requirement)     │  │
│                              └──────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documents

| Document | Content |
|---|---|
| [The HNS Origin Trilogy](https://github.com/satoru-hara/03_NSW) | Three foundational papers on MAV, HNS implementation, and structural isomorphism |
| [HNS Correspondence Table Report](https://github.com/satoru-hara/03_NSW) | Structural mapping between human brain and HNS-aligned AI |
| [JSON-LD / RDF Overview](https://github.com/satoru-hara/03_NSW) | W3C technical foundation of HNS |
| [AI Standards and HNS: Full Alignment Report](https://github.com/satoru-hara/03_NSW) | Complete standard-by-standard alignment with implementation detail |
| [Social Meta Structure Specification](https://github.com/satoru-hara/03_NSW) | Structural extension of HNS to social and civilisational layers |

---

*HNS-PoC-Package v1.1 · Satoru Hara · Natural Structure Works · 2026*
*github.com/satoru-hara/03_NSW · naturalstructureworks.com*
