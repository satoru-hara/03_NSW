# Human Natural Structure Standards Specification
## A Structural Implementation Framework for International AI Governance

**HNS-PoC-Package v2.0 · Overview Document**
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
9. [Legal Basis for Referenced Standards](#9-legal-basis-for-referenced-standards)
10. [JSON-LD, RDF, and the HNS Ontology](#10-json-ld-rdf-and-the-hns-ontology)
11. [Conformance Requirements](#11-conformance-requirements)
12. [Standardization Pathway](#12-standardization-pathway)
13. [Summary](#13-summary)
14. [Annexes](#14-annexes)

---

## 1. Normative References

The following documents are indispensable for the application of this specification.
For dated references, only the edition cited applies.
For undated references, the latest edition applies.

### 1.1 ISO/IEC JTC 1/SC 42 — Artificial Intelligence

| Standard No. | Title |
|---|---|
| **ISO/IEC 42001:2023** | Information technology — Artificial intelligence — Management system |
| **ISO/IEC 42005:2025** | Information technology — Artificial intelligence — AI system impact assessment |
| **ISO/IEC 23894:2023** | Information technology — Artificial intelligence — Guidance on risk management |
| **ISO/IEC 22989:2022** | Information technology — Artificial intelligence — Concepts and terminology |
| **ISO/IEC 23053:2022** | Framework for Artificial Intelligence (AI) Systems Using Machine Learning |
| **ISO/IEC 24028:2020** | Overview of trustworthiness in artificial intelligence |
| **ISO/IEC 24027:2021** | Bias in AI systems and AI-aided decision making |
| **ISO/IEC 24029-1:2021** | Assessment of the robustness of neural networks — Part 1: Overview |
| **ISO/IEC 24030:2021** | Information technology — Artificial intelligence — Use cases |
| **ISO/IEC 24368:2022** | Overview of ethical and societal concerns |
| **ISO/IEC 5338:2023** | Information technology — Artificial intelligence — AI system life cycle processes |
| **ISO/IEC 5259-1:2024** | Data quality for analytics and ML — Part 1: Overview, terminology and examples |
| **ISO/IEC TR 24372:2021** | Overview of computational approaches for AI systems |
| **ISO/IEC 42006 (WD)** | Requirements for AI management system certification bodies [in development] |
| **ISO/IEC 42105 (WD)** | Guidance for human oversight of AI systems [in development] |

### 1.2 ISO/IEC — Governance, Security, Privacy, Quality, Safety, and Testing

| Standard No. | Title |
|---|---|
| **ISO/IEC 38507:2022** | Information technology — Governance of IT — Governance implications of the use of artificial intelligence by organisations |
| **ISO/IEC 27001:2022** | Information technology — Information security management systems — Requirements |
| **ISO/IEC 27002:2022** | Information technology — Information security controls (implementation guidance for ISO/IEC 27001 Annex A) |
| **ISO/IEC 27701:2019** | Security techniques — Extension to ISO/IEC 27001 for privacy information management (PIMS) |
| **ISO/IEC 27017:2015** | Code of practice for information security controls for cloud services |
| **ISO/IEC 29100:2011** | Information technology — Security techniques — Privacy framework |
| **ISO/IEC 29184:2020** | Information technology — Online privacy notices and consent |
| **ISO/IEC 29119-1:2022** | Software and systems engineering — Software testing — Part 1: General concepts |
| **ISO/IEC 29119-2:2021** | Software and systems engineering — Software testing — Part 2: Test processes |
| **ISO/IEC 15288:2023** | Systems and software engineering — System life cycle processes |
| **ISO/IEC 24748-1:2018** | Systems and software engineering — Life cycle management — Part 1: Guidelines |
| **ISO/IEC 20000-1:2018** | Information technology — Service management — Part 1: Service management system requirements |
| **ISO 31000:2018** | Risk management — Guidelines (parent framework for AI risk) |
| **ISO 9001:2015** | Quality management systems — Requirements |
| **ISO/IEC 25010:2023** | Systems and software quality models |
| **ISO/IEC 15408-1:2022** | Common Criteria — Evaluation criteria for IT security — Part 1 |
| **IEC 61508-1:2010** | Functional safety of E/E/PE safety-related systems — Part 1: General requirements |
| **IEC 62304:2006+A1:2015** | Medical device software — Software life cycle processes |
| **IEC 62443-2-1:2010** | Industrial cybersecurity — Security management system requirements |

### 1.3 European Union Regulatory Framework

| Instrument | Title / Description |
|---|---|
| **EU Charter of Fundamental Rights — Art. 1, 7, 8, 21, 47** | Dignity, Privacy, Data Protection, Non-discrimination, Effective remedy — Primary law basis for EU AI Act |
| **Regulation (EU) 2024/1689 — EU AI Act** | Laying down harmonised rules on artificial intelligence |
| **Regulation (EU) 2016/679 — GDPR** | General Data Protection Regulation |
| **Directive (EU) 2022/2555 — NIS2** | Measures for a high common level of cybersecurity across the Union |
| **Regulation (EU) 2019/881 — Cybersecurity Act** | ENISA mandate and ICT security certification framework |
| **Regulation (EU) 2022/2065 — Digital Services Act** | Obligations for providers of intermediary services |
| **Regulation (EU) 2023/2854 — Data Act** | Rules on fair access to and use of data |
| **Regulation (EU) 2023/1230 — Machinery Regulation** | Regulation on machinery (replacing Directive 2006/42/EC) |
| **Regulation (EU) 2017/745 — MDR** | Medical Device Regulation |
| **Regulation (EU) 2017/746 — IVDR** | In Vitro Diagnostic Medical Device Regulation |
| **Council Directive 85/374/EEC (amended)** | Product Liability Directive |
| **COM/2022/496 — AI Liability Directive (proposed)** | Rules on liability for AI-related damages [legislative proposal] |

### 1.4 W3C Technical Standards

| Specification | Title / Version |
|---|---|
| **JSON-LD 1.1 (W3C Rec. 2020)** | A JSON-based Serialization for Linked Data |
| **RDF 1.1 (W3C Rec. 2014)** | RDF 1.1 Concepts and Abstract Syntax |
| **PROV-O (W3C Rec. 2013)** | The PROV Ontology |
| **OWL 2 (W3C Rec. 2012)** | OWL 2 Web Ontology Language |
| **SPARQL 1.1 (W3C Rec. 2013)** | SPARQL 1.1 Query Language for RDF |
| **SKOS (W3C Rec. 2009)** | Simple Knowledge Organization System |
| **Linked Data Platform 1.0 (W3C Rec. 2015)** | LDP — HTTP-based architecture for Linked Data |

### 1.5 IEEE Standards Association

| Standard | Title |
|---|---|
| **IEEE 7000-2021** | Model Process for Addressing Ethical Concerns during System Design |
| **IEEE 7001-2021** | Transparency of Autonomous Systems |
| **IEEE 7002-2022** | Data Privacy Process |
| **IEEE 7010-2020** | Recommended Practice — Assessing the Impact of Autonomous and Intelligent Systems on Human Well-Being |
| **IEEE 7012 (draft)** | Machine Readable Personal Privacy Terms |
| **IEEE P2863** | Organizational Governance of Artificial Intelligence [in development] |

### 1.6 NIST and United States Federal Instruments

| Document | Title / Authority |
|---|---|
| **NIST AI RMF 1.0 (2023)** | Artificial Intelligence Risk Management Framework — National AI Initiative Act 2020 (15 U.S.C. §9401) |
| **NIST SP 800-218 (2022)** | Secure Software Development Framework (SSDF) |
| **NIST SP 800-53 Rev.5 (2020)** | Security and Privacy Controls for Information Systems — FISMA mandate |
| **Executive Order 14110 (2023)** | Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence |

### 1.7 ITU-T Recommendations

| Recommendation | Title |
|---|---|
| **ITU-T Y.3172 (06/2019)** | Architectural framework for machine learning in future networks including IMT-2020 |
| **ITU-T Y.3173 (02/2020)** | Framework for evaluating intelligence levels of future networks including IMT-2020 |
| **ITU-T Y.3174 (09/2019)** | Framework for data handling to enable machine learning in future networks |
| **UN GA Resolution A/78/L.49 (2024)** | Seizing the opportunities of safe, secure and trustworthy AI systems for sustainable development |

### 1.8 CEN/CENELEC, Council of Europe, and International Governance

| Instrument | Description / Status |
|---|---|
| **CEN/CENELEC JTC 21** | Artificial Intelligence — European harmonised standards under EU AI Act |
| **CoE CETS 225 (2024)** | Framework Convention on AI and Human Rights, Democracy and the Rule of Law — open to non-member states including US, UK, Japan |
| **OECD AI Principles (2019, rev. 2024)** | Recommendation of the Council on Artificial Intelligence |
| **G7 Hiroshima AI Process (2023)** | International Guiding Principles and Code of Conduct for Advanced AI Systems |
| **UNESCO AI Ethics Recommendation (2021)** | Recommendation on the Ethics of Artificial Intelligence |
| **Canada — AIDA (proposed)** | Artificial Intelligence and Data Act — Bill C-27 [legislative proposal] |
| **China — GB/T 42118:2023** | Information technology — AI governance — Technical principles [national standard] |

> **Total: 80 normative references** across ISO/IEC, EU, W3C, IEEE, NIST, ITU-T, and international governance instruments.

---

## 2. Terms and Definitions

For the purposes of this document, the following terms and definitions apply.
All terms defined in ISO/IEC 22989:2022 and ISO/IEC 42001:2023 also apply where relevant.

**2.1 Human Natural Structure (HNS)**
A multi-resolution structural model of human cognition implemented as a three-layer cellular matrix (HNS-36, HNS-144, HNS-864). HNS serves as the universal structural baseline against which AI outputs are mapped and verified.

**2.2 HNS-36**
The foundational layer of HNS: a 6-layer × 6-category matrix of 36 cells constituting the universal coordinate system for cognitive and AI outputs.

**2.3 HNS-144**
The observational layer of HNS: 144 cells (HNS-36 × 4 logical dimensions). Provides category-level verification, concept boundary enforcement, and meaning stability monitoring.

**2.4 HNS-864**
The analytical layer of HNS: 864 cells (HNS-144 × 6 validity modalities). Provides proposition-level causal audit and structural risk scoring.

**2.5 External Verification Architecture (EVA)**
An independent structural verification layer operating alongside — but separately from — the AI system being verified. EVA produces JSON-LD audit records conforming to W3C PROV-O and enforces Verifiability, Transparency, and Physical Immutability.

**2.6 External Control System (ECS)**
The executive control layer implementing human oversight requirements. Enforces output control, action constraints, risk boundary thresholds, and hardware-level emergency override.

**2.7 HumanOS**
The integration meta-architecture that coordinates HNS-36, HNS-144, HNS-864, EVA, and ECS into a unified system-level governance architecture. Implements ISO/IEC 38507:2022 governance implications at the AI system level.

**2.8 Social Meta Structure (SMS)**
The structural extension of HNS mapping cognitive outputs onto social (layer 4), institutional (layer 5), and civilisational (layer 6) layers.

**2.9 Structural Baseline**
The formal, machine-readable reference model derived from HNS-36 against which AI outputs are evaluated for structural alignment with human cognition and values.

**2.10 Structural Hallucination**
A class of AI output failure characterised by violations of structural invariants. Five types: Layer Jump, Category Ambiguity, Scope Drift, Metaphor Contamination, Unsupported Causality.

**2.11 Structural Risk Score**
A quantitative score R ∈ [0.00, 1.00] computed at the HNS-864 proposition level, expressing the degree of structural misalignment between an AI output and the HNS structural baseline.

**2.12 Meaning Stability**
The property of an AI output maintaining consistent structural attribution across layers and categories over successive inference cycles. Monitored by HNS-144 with default threshold T_s = 0.15.

**2.13 HNS Structural Feedback (HSF)**
A corrective feedback mechanism through which HNS-36 verification results are returned to the AI inference pipeline to guide structural alignment without modifying model weights.

**2.14 Sidecar Architecture**
An architectural pattern in which EVA operates as an independent module alongside — but not integrated into — the AI system under audit.

**2.15 Physical Immutability**
The EVA condition requiring that audit records, once written, cannot be modified or deleted by any software process (see ISO/IEC 27001:2022 A.8.3; ISO/IEC 27002:2022).

**2.16 Multi-Axis Verification (MAV)**
The foundational cognitive architecture (Hara, 2026) in which three orthogonal cognitive axes — Stochastic/Generative, Structural/Causal, and Grounded/Executive — intersect to produce structurally valid cognitive outputs.

**2.17 Origin Trilogy**
The three foundational papers (Hara, 2026) establishing the theoretical basis of HNS: the MAV paper, the HNS implementation paper, and the structural isomorphism paper.

---

## 3. The Core Relationship

International AI standards and Human Natural Structure (HNS) are complementary — not competing — frameworks:

| Layer | Who Defines It | What It Addresses |
|---|---|---|
| **Regulatory layer** | EU AI Act, ISO/IEC, NIST, IEEE | *What* AI must do: be safe, transparent, human-centric |
| **Structural layer** | **HNS / EVA / ECS** | *How* to technically implement and verify those requirements |

> Standards define the destination.
> HNS defines the road.

**Together, they form a complete framework for trustworthy AI.**

### 3.1 Origin Trilogy → AI → Society: The Full Structural Chain

```
┌──────────────────────────────────────────────────────────┐
│                    Origin Trilogy                        │
│  Human brain structure → Structural baseline (HNS-36)    │
└─────────────────────┬────────────────────────────────────┘
                      ▼
┌──────────────────────────────────────────────────────────┐
│                  HNS / EVA / ECS                         │
│  HNS-36 → HNS-144 → HNS-864 → EVA → ECS                 │
└─────────────────────┬────────────────────────────────────┘
                      ▼
┌──────────────────────────────────────────────────────────┐
│              Social Meta Structure (SMS)                 │
│  Social / Institutional / Civilisational layers          │
│  Governed by HumanOS (ISO/IEC 38507:2022)                │
└─────────────────────┬────────────────────────────────────┘
                      ▼
┌──────────────────────────────────────────────────────────┐
│       International AI Standards (80 references)         │
│  EU AI Act / ISO/IEC / NIST / IEEE / ITU-T / CoE         │
└──────────────────────────────────────────────────────────┘
```

---

## 4. What International Standards Define

### EU AI Act (Regulation 2024/1689)
- Classification by risk level (Arts. 5–7; Annex III)
- High-risk AI requirements: documentation (Art. 11; Annex IV), logging (Art. 12), transparency (Art. 13), human oversight (Art. 14), accuracy (Art. 15)
- Conformity assessment (Art. 43; Annexes VI–VII)
- Post-market monitoring (Arts. 72–73)
- General-purpose AI obligations (Arts. 51–56)

### ISO/IEC 42001:2023 — AI Management System
- Governance and risk management (§6.1); audit (§9.2); improvement (§10.2); human oversight (§8.4)

### ISO/IEC 38507:2022 — Governance Implications of AI
- Governance framework for AI use at organisational level
- Accountability, oversight, and transparency obligations for AI deployers

### ISO/IEC 23894:2023 — AI Risk Management
- Risk identification, assessment, treatment; human wellbeing as risk baseline

### NIST AI RMF 1.0
- Four-function framework: **GOVERN / MAP / MEASURE / MANAGE**

### CoE CETS 225 (2024) — Framework Convention on AI
- First legally binding international AI treaty
- Human rights, democracy, and rule of law safeguards
- Applies to US, UK, Japan, and other non-EU signatories

---

## 5. What International Standards Leave Undefined

> **There is no structural baseline for human cognition, behaviour, or meaning.**

| Standard Requirement | What Is Missing |
|---|---|
| **Transparency** | A reference frame against which outputs can be verified as transparent |
| **Logging** | A structural schema defining *what* AI logs should record and *why* |
| **Human oversight** | A technical definition of what "human-aligned" means at the output level |
| **Risk assessment** | A structural model of human wellbeing as the risk baseline |
| **Conformance testing** | A verifiable baseline against which conformance can be demonstrated |
| **Value alignment** | A measurable, structural specification of human values |
| **Governance** | A technical implementation of AI governance obligations (ISO/IEC 38507) |

```
┌─────────────────────────────────────────────────────────────────────┐
│                   THE STRUCTURAL GAP                                │
│                                                                     │
│  ┌──────────────────────────┐     ┌───────────────────────────────┐ │
│  │  International Standards │     │  Technical Implementation     │ │
│  │  (EU AI Act / ISO / NIST)│     │  (Who defines HOW?)           │ │
│  │  WHAT AI must do:        │ ──▶ │  ??? (undefined by standards) │ │
│  │  • Be transparent        │     │                               │ │
│  │  • Log outputs           │     │  HNS fills this gap:          │ │
│  │  • Human oversight       │ ──▶ │  • HNS-36 structural baseline │ │
│  │  • Risk assessment       │     │  • EVA verification layer     │ │
│  │  • Governance (38507)    │     │  • ECS control system         │ │
│  └──────────────────────────┘     └───────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

**HNS fills this gap.**

---

## 6. How HNS Fills the Gap

### 6.1 HNS — Human Natural Structure

```
HNS Hierarchy
│
├── HNS-36   (6 layers × 6 categories = 36 cells)
│   └── Universal structural baseline; coordinate system
│
├── HNS-144  (36 cells × 4 logical dimensions = 144 cells)
│   └── Category-level verification; meaning stability monitoring
│
└── HNS-864  (144 cells × 6 validity modalities = 864 cells)
    └── Proposition-level causal audit; structural risk scoring
```

| Layer | HNS Natural Layer | SMS Scope |
|---|---|---|
| 1 | Physical | Physical environment |
| 2 | Biological | Living systems |
| 3 | Psychological | Individual cognition |
| 4 | Social | Interpersonal and group dynamics |
| 5 | Institutional | Organisations and governance |
| 6 | Civilisational | Cross-cultural, historical, global |

### 6.2 EVA — External Verification Architecture

```
┌─────────────────────────────────────────────────────┐
│               AI System Under Audit                 │
│  (Internal parameters: NOT accessible to EVA)       │
└────────────────────┬────────────────────────────────┘
                     │ outputs only
                     ▼
┌─────────────────────────────────────────────────────┐
│          EVA — Sidecar Architecture                 │
│  Verifiability · Transparency · Physical Immutability│
│  JSON-LD Audit Records (PROV-O) — ISO/IEC 27002     │
└─────────────────────────────────────────────────────┘
```

### 6.3 ECS — External Control System

| Action | Trigger | Description |
|---|---|---|
| DELIVER | R < T_low | Output delivered to user |
| DELIVER_WITH_FLAG | T_low ≤ R < T_moderate | Output delivered with structural flag |
| HOLD_FOR_REVIEW | T_moderate ≤ R < T_high | Human oversight operator notified |
| BLOCK | R ≥ T_high | Output blocked; user informed |

### 6.4 HumanOS — Integration Meta-Architecture

HumanOS coordinates HNS, EVA, and ECS and implements:
- **ISO/IEC 38507:2022** — Governance implications of AI use
- **ISO/IEC 42001:2023 §5** — Leadership and governance
- **ISO/IEC 20000-1:2018** — IT service management
- **ISO/IEC 15288:2023** — System lifecycle processes
- **NIST AI RMF GOVERN** — Governance function
- **CoE CETS 225 Art. 16** — Human oversight obligations

---

## 7. Standard-by-Standard Alignment

### EU AI Act

| Requirement | Article | HNS / EVA / ECS Response |
|---|---|---|
| Technical documentation | Art. 11; Annex IV | HNS-36 baseline; JSON-LD cell ontology |
| Risk management system | Art. 9 | HNS-864 analytical engine; structural risk scoring |
| Logging and record-keeping | Art. 12 | EVA JSON-LD audit records (PROV-O) — ISO/IEC 27002 A.8.15 |
| Transparency to users | Art. 13; ISO/IEC 29184 | EVA sidecar architecture; structurally independent monitoring |
| Human oversight measures | Art. 14 | ECS output control and emergency override |
| Accuracy and robustness | Art. 15 | HNS-144 meaning stability; ISO/IEC 27001 A.8.3 |
| Provider obligations | Art. 26 | HumanOS — ISO/IEC 38507:2022 governance layer |
| Conformity assessment | Art. 43; Annex VII | HNS-36 baseline; ISO/IEC 29119 test processes |
| GPAI transparency | Art. 53 | EVA external audit layer |
| Post-market monitoring | Art. 72 | EVA continuous audit stream |

### ISO/IEC 42001:2023 — AI Management System

| Requirement | Clause | HNS / EVA / ECS Response |
|---|---|---|
| AI risk identification | 6.1 | HNS-864 analytical engine; structural risk categories |
| Human oversight integration | 8.4 | HNS-144 observational OS; ECS control mechanisms |
| Internal audit | 9.2 | EVA audit logs; SPARQL-queryable |
| Continuous improvement | 10.2 | EVA corrective cycle; structural drift detection |

### ISO/IEC 38507:2022 — Governance Implications of AI

| Requirement | HNS / EVA / ECS Response |
|---|---|
| Governance framework for AI | HumanOS meta-architecture |
| Accountability for AI outputs | EVA immutable audit trail |
| Oversight mechanisms | ECS emergency override; human operator notification |
| Transparency obligations | EVA sidecar; ISO/IEC 29184 online transparency |

### NIST AI RMF 1.0

| Function | HNS / EVA / ECS Response |
|---|---|
| **GOVERN** | HumanOS meta-architecture; ISO/IEC 38507:2022 |
| **MAP** | HNS-36 structural mapping; universal coordinate baseline |
| **MEASURE** | EVA external measurement; HNS-864 structural risk scoring |
| **MANAGE** | ECS output control and action constraints |

### CoE CETS 225 (2024)

| Article | HNS / EVA / ECS Response |
|---|---|
| Art. 14 — Transparency | EVA sidecar; ISO/IEC 29184 transparency notices |
| Art. 15 — Explainability | HNS-36 coordinate attribution; JSON-LD audit records |
| Art. 16 — Human oversight | ECS emergency override; operator notification |

---

## 8. The EVA-HNS Full-Stack Specification

```
EVA-HNS Full-Stack Specification
│
├── HumanOS    → GOVERN (NIST) / ISO 42001 §5 / ISO 38507 / ISO 20000-1
│
├── HNS-36     → MAP (NIST) / ISO 42001 §6.1 / EU AI Act Art. 11, 43
│
├── HNS-144    → MAP + MEASURE / EU AI Act Art. 12, 15 / ISO 42001 §8.4
│
├── HNS-864    → MEASURE / ISO 23894 / ISO 42001 §9.2 / EU AI Act Art. 9
│
├── EVA        → MEASURE / EU AI Act Art. 12, 13 / ISO 27001 / ISO 27002
│
└── ECS        → MANAGE / EU AI Act Art. 14 / IEC 61508 / CoE CETS 225 Art. 16
```

| Standards Provide | EVA-HNS Full Stack Provides |
|---|---|
| Logging *requirements* (Art. 12) | Structured JSON-LD logs with HNS coordinate attribution (ISO/IEC 27002 A.8.15) |
| Transparency *requirements* (Art. 13) | EVA sidecar; ISO/IEC 29184 online transparency notices |
| Human oversight *requirements* (Art. 14) | ECS: structural implementation of "human-aligned" control |
| Risk management *requirements* (Art. 9) | HNS-864: quantitative, proposition-level structural risk scoring |
| Conformance testing *requirements* (Art. 43) | HNS-36: verifiable baseline with ISO/IEC 29119 test processes |
| Governance *requirements* (ISO/IEC 38507) | HumanOS: AI governance integration layer |
| Privacy *requirements* (ISO/IEC 29100) | EVA log PII handling; GDPR Art. 5 compliance |

---

## 9. Legal Basis for Referenced Standards

### 9.1 Legal Hierarchy

1. **Primary law** — Constitutional/treaty-level (TFEU; EU Charter; Council of Europe Conventions)
2. **Secondary legislation** — Regulations and directives (EU AI Act under TFEU Art. 114)
3. **Harmonised standards** — Referenced by legislation (ISO/IEC 42001 as harmonised EN under EU AI Act Art. 40)
4. **Voluntary frameworks** — De facto authority (NIST AI RMF; OECD AI Principles)

### 9.2 EU Legal Basis

| Instrument | Treaty Basis | Type | Binding Force |
|---|---|---|---|
| EU Charter — Art. 1,7,8,21,47 | Treaty of Lisbon (2009) | Charter | Binding on EU institutions and Member States |
| EU AI Act 2024/1689 | TFEU Art. 114 | Regulation | Directly binding in all EU Member States |
| GDPR 2016/679 | TFEU Art. 16 | Regulation | Directly binding |
| NIS2 2022/2555 | TFEU Art. 114 | Directive | Binding; implemented via national law |
| MDR 2017/745 | TFEU Art. 114 | Regulation | Directly binding |

### 9.3 ISO/IEC Standards Legal Basis

| Standard | EU AI Act Connection | Legal Weight |
|---|---|---|
| ISO/IEC 42001:2023 | Art. 40 harmonised EN candidate | Quasi-mandatory for high-risk AI providers |
| ISO/IEC 38507:2022 | Art. 26 Provider obligations | Technical reference standard |
| ISO/IEC 27001:2022 | Art. 15; NIS2 Art. 21 | Technical reference standard |
| ISO/IEC 27002:2022 | NIS2 Art. 21; EVA A.8.3/A.8.15 | Implements ISO/IEC 27001 Annex A |
| ISO/IEC 29100:2011 | GDPR Art. 5(1)(b)–(e) | Privacy framework; referenced by ISO/IEC 27701 |
| ISO/IEC 29184:2020 | Art. 13 Transparency notices | Technical reference standard |
| ISO/IEC 29119:2021-22 | Art. 43; Annex VII | Conformity assessment test processes |
| ISO/IEC 20000-1:2018 | Art. 26 Provider obligations | IT service management |
| IEC 61508:2010 | Art. 9(9) safety-critical AI | Domain-mandatory for industrial AI |
| IEC 62304:2006 | EU MDR Art. 25; IVDR Art. 20 | Domain-mandatory for medical AI |

### 9.4 International Treaty Basis

| Instrument | Legal Basis | Scope |
|---|---|---|
| CoE CETS 225 (2024) | Council of Europe Statute (1949) | Legally binding international treaty; US, UK, Japan signatories |
| UN GA Res. A/78/L.49 (2024) | UN Charter Art. 10 | Non-binding; 123 co-sponsors |
| OECD AI Principles | OECD Convention (1960) | Non-binding; 46 adherent countries |
| ITU-T Y.3172/3/4 | ITU Constitution (1992) | Voluntary; 193 member states |

---

## 10. JSON-LD, RDF, and the HNS Ontology

### 10.1 The Linked Data Stack

| Layer | Standard | Function in HNS |
|---|---|---|
| Identity | IRI (RFC 3987) | Globally unique identifiers for every HNS cell, term, and audit record |
| Data model | RDF 1.1 | Triple-based representation of HNS structural relationships |
| Serialisation | JSON-LD 1.1 | JSON encoding of RDF for audit logs and API responses |
| Vocabulary | OWL 2 / SKOS | Formal ontology defining HNS classes and properties |
| Query | SPARQL 1.1 | Querying EVA audit logs against the HNS ontology |
| Provenance | PROV-O | Audit record schema for EVA verification activities |

### 10.2 The HNS Namespace

```
https://naturalstructureworks.com/ns/hns#
https://naturalstructureworks.com/ns/eva#
```

Each HNS-36 cell is globally addressable as:
```
https://naturalstructureworks.com/ns/hns#cell-{layer}-{category}
```

### 10.3 EVA Audit Record in JSON-LD / PROV-O

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "hns":  "https://naturalstructureworks.com/ns/hns#",
    "eva":  "https://naturalstructureworks.com/ns/eva#",
    "xsd":  "http://www.w3.org/2001/XMLSchema#"
  },
  "@type":  "prov:Activity",
  "@id":    "eva:audit/{uuid}",
  "prov:startedAtTime":     "2026-01-01T00:00:00Z",
  "hns:layerIndex":         3,
  "hns:categoryIndex":      2,
  "hns:dimensionIndex":     "D2",
  "hns:riskScore":          "0.08",
  "eva:verificationResult": "PASS",
  "eva:hallucination":      false,
  "prov:wasAssociatedWith": { "@id": "eva:verifier/EVA-v1.0" },
  "prov:used":              { "@id": "hns:cell-3-2" }
}
```

### 10.4 SPARQL Query Examples

**Query 1 — All FAIL records:**
```sparql
PREFIX eva:  <https://naturalstructureworks.com/ns/eva#>
PREFIX hns:  <https://naturalstructureworks.com/ns/hns#>
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?activity ?time ?layer ?cat ?score
WHERE {
  ?activity a prov:Activity ;
            prov:startedAtTime  ?time ;
            hns:layerIndex      ?layer ;
            hns:categoryIndex   ?cat ;
            hns:riskScore       ?score ;
            eva:verificationResult "FAIL" .
} ORDER BY DESC(?time)
```

**Query 2 — Session risk profile by layer:**
```sparql
SELECT ?layer (AVG(?score) AS ?avgRisk) (COUNT(*) AS ?count)
WHERE { ?a a prov:Activity ; hns:layerIndex ?layer ; hns:riskScore ?score . }
GROUP BY ?layer ORDER BY DESC(?avgRisk)
```

---

## 11. Conformance Requirements

A system claiming structural conformance **SHALL** satisfy all requirements in this section.
Test processes SHALL follow ISO/IEC 29119-2:2021. Test documentation SHALL follow ISO/IEC 29119-1:2022.

### 11.1 HNS-36 Baseline

- **R-HNS-01** SHALL apply HNS-36 as the structural baseline for all AI outputs subject to verification.
- **R-HNS-02** Each output SHALL be attributed to exactly one primary HNS-36 cell (l, c).
- **R-HNS-03** Attribution SHALL be performed by EVA independently of the AI system's internal parameters.
- **R-HNS-04** The HNS-36 cell ontology SHALL be expressed as JSON-LD 1.1 / RDF.
- **R-HNS-05** SHALL apply HNS-864 risk scoring for all outputs classified as high-risk under EU AI Act Annex III.

### 11.2 EVA Logging

- **R-LOG-01** EVA SHALL produce a JSON-LD audit record for every AI output subject to verification.
- **R-LOG-02** Each record SHALL conform to the PROV-O Activity instance schema (Annex B).
- **R-LOG-03** Records SHALL include all mandatory fields (Section 8).
- **R-LOG-04** Records SHALL be immutable once written (ISO/IEC 27001 A.8.3; ISO/IEC 27002).
- **R-LOG-05** Records SHALL be queryable via SPARQL against the HNS RDF ontology.
- **R-LOG-06** Records SHALL be retained per the deployment specification (EU AI Act Art. 12).

### 11.3 ECS Safety Boundaries

- **R-ECS-01** ECS SHALL block any output where R ≥ T_high unless overridden with documented justification.
- **R-ECS-02** ECS SHALL enforce action constraints on agentic AI systems.
- **R-ECS-03** ECS SHALL trigger an alert when R ≥ T_moderate.
- **R-ECS-04** ECS SHALL provide a hardware-level emergency override (EU AI Act Art. 14(4)(e)).
- **R-ECS-05** The emergency override SHALL operate independently of the AI system's software state (IEC 61508).
- **R-ECS-06** Every override activation SHALL generate a mandatory incident record within 60 seconds (NIS2 Art. 23).

### 11.4 Conformance Test Suite (ISO/IEC 29119)

| Test ID | Requirement | Pass Criterion |
|---|---|---|
| TC-01 | R-HNS-01, R-HNS-02 | ≥95% of 100 sample outputs attributed to valid HNS-36 cell |
| TC-02 | R-HNS-03 | EVA attribution log contains no internal model parameter references |
| TC-03 | R-LOG-02 | 100% of 100 audit records validate against PROV-O schema |
| TC-04 | R-LOG-04 | Modification attempt on written record rejected; original preserved |
| TC-05 | R-LOG-05 | SPARQL query returns correct attribution results |
| TC-06 | R-ECS-01 | FAIL-rated output (R ≥ T_high) blocked before delivery |
| TC-07 | R-ECS-04 | Emergency override activates within specified latency threshold |
| TC-08 | R-ECS-06 | Incident record written within 60 seconds of override activation |
| TC-09 | R-HNS-05 | HNS-864 risk score computed for all Annex III high-risk outputs |
| TC-10 | R-LOG-06 | Audit log export accessible on demand in human-readable form |

---

## 12. Standardization Pathway

| Body | Track | Proposal |
|---|---|---|
| **W3C** | Community Group Specification | HNS JSON-LD context file; SPARQL endpoint specification |
| **ISO/IEC JTC 1/SC 42** | New Work Item Proposal (NWIP) | EVA Technical Specification (WG 1 and WG 3) |
| **CEN/CENELEC JTC 21** | European Technical Specification | Integration into EU AI Act harmonised EN standards |
| **NIST** | Technical submission | HNS/EVA as MEASURE implementation for NIST AI RMF |
| **IEEE SA** | Standards project | EVA for IEEE P2863 (Organisational Governance of AI) |
| **Council of Europe** | Technical guidance | HNS/ECS as Art. 14–16 CETS 225 implementation |

---

## 13. Summary

| Question | Answer |
|---|---|
| What do international AI standards define? | *That* AI must be safe, transparent, and human-aligned |
| What do they leave undefined? | *How* to structurally implement and verify those properties |
| What does HNS provide? | Structural baseline (HNS-36/144/864), verification (EVA), control (ECS), governance (HumanOS) |
| How are standards and HNS related? | Complementary: standards define the regulatory framework; HNS defines the technical implementation |
| What is the result? | The EVA-HNS Full-Stack Specification — 80 normative references, fully implemented |

> International AI standards and HNS are two halves of the same solution.
>
> Standards define what trustworthy AI must be.
> HNS defines what trustworthy AI structurally is.
>
> Together, they make AI governance verifiable, auditable, and standardisable.

---

## 14. Annexes

### Annex A — HNS-36 Cell Reference Table (Normative)

| Cell ID | Layer | Category | Natural Domain | SMS Scope |
|---|---|---|---|---|
| HNS-1-1 | Physical | Substrate | Physical substrate | Material environment |
| HNS-1-2 | Physical | Process | Physical process | Energy/matter transformation |
| HNS-1-3 | Physical | State | Physical state | System equilibrium |
| HNS-1-4 | Physical | Relation | Physical relation | Spatial/causal relations |
| HNS-1-5 | Physical | Boundary | Physical boundary | System interface |
| HNS-1-6 | Physical | Emergence | Physical emergence | Complex physical phenomena |
| HNS-2-1 | Biological | Substrate | Biological substrate | Cell/organism |
| HNS-2-2 | Biological | Process | Biological process | Metabolism/reproduction |
| HNS-2-3 | Biological | State | Biological state | Homeostasis/health |
| HNS-2-4 | Biological | Relation | Biological relation | Ecology/symbiosis |
| HNS-2-5 | Biological | Boundary | Biological boundary | Species/population boundary |
| HNS-2-6 | Biological | Emergence | Biological emergence | Evolutionary emergence |
| HNS-3-1 | Psychological | Substrate | Perceptual substrate | Sensory input/attention |
| HNS-3-2 | Psychological | Process | Cognitive process | Memory/reasoning |
| HNS-3-3 | Psychological | State | Affective state | Emotion/motivation |
| HNS-3-4 | Psychological | Relation | Interpersonal relation | Communication/attachment |
| HNS-3-5 | Psychological | Boundary | Identity boundary | Self/other distinction |
| HNS-3-6 | Psychological | Emergence | Psychological emergence | Consciousness/meaning |
| HNS-4-1 | Social | Substrate | Social substrate | Individual agent |
| HNS-4-2 | Social | Process | Social process | Interaction/coordination |
| HNS-4-3 | Social | State | Social state | Norms/trust |
| HNS-4-4 | Social | Relation | Social relation | Role/network |
| HNS-4-5 | Social | Boundary | Social boundary | Group/community boundary |
| HNS-4-6 | Social | Emergence | Social emergence | Culture/collective behaviour |
| HNS-5-1 | Institutional | Substrate | Institutional substrate | Organisation/agency |
| HNS-5-2 | Institutional | Process | Institutional process | Governance/decision-making |
| HNS-5-3 | Institutional | State | Institutional state | Policy/regulation |
| HNS-5-4 | Institutional | Relation | Institutional relation | Jurisdiction/accountability |
| HNS-5-5 | Institutional | Boundary | Institutional boundary | Legal/regulatory boundary |
| HNS-5-6 | Institutional | Emergence | Institutional emergence | Law/systemic governance |
| HNS-6-1 | Civilisational | Substrate | Civilisational substrate | Civilisation/humanity |
| HNS-6-2 | Civilisational | Process | Civilisational process | Historical change/progress |
| HNS-6-3 | Civilisational | State | Civilisational state | Values/knowledge commons |
| HNS-6-4 | Civilisational | Relation | Civilisational relation | Cross-cultural interaction |
| HNS-6-5 | Civilisational | Boundary | Civilisational boundary | Species/civilisational limit |
| HNS-6-6 | Civilisational | Emergence | Civilisational emergence | Existential conditions |

---

### Annex B — EVA JSON-LD Audit Record Schema (Normative)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "hns":  "https://naturalstructureworks.com/ns/hns#",
    "eva":  "https://naturalstructureworks.com/ns/eva#",
    "xsd":  "http://www.w3.org/2001/XMLSchema#"
  },
  "@type":  "prov:Activity",
  "@id":    "eva:audit/{uuid}",
  "prov:startedAtTime":     { "@type": "xsd:dateTime", "@value": "2026-01-01T00:00:00Z" },
  "hns:layerIndex":         { "@type": "xsd:integer",  "@value": 3 },
  "hns:categoryIndex":      { "@type": "xsd:integer",  "@value": 2 },
  "hns:dimensionIndex":     { "@type": "xsd:string",   "@value": "D2" },
  "hns:riskScore":          { "@type": "xsd:decimal",  "@value": "0.12" },
  "eva:verificationResult": "PASS",
  "eva:hallucination":      { "@type": "xsd:boolean",  "@value": false },
  "prov:wasAssociatedWith": { "@id": "eva:verifier/EVA-v1.0" },
  "prov:used":              { "@id": "hns:cell-3-2" }
}
```

---

### Annex C — EU AI Act Annex III Risk Category Mapping (Normative)

| Annex III Category | Use Case Example | Primary HNS Layer | EVA Risk |
|---|---|---|---|
| 1. Biometric identification | Remote biometric identification | Psychological (3) | HIGH |
| 2. Critical infrastructure | AI safety components in electricity grids | Physical (1) + Institutional (5) | HIGH |
| 3. Education | AI student assessment and grading | Psychological (3) + Social (4) | MEDIUM |
| 4. Employment | Recruitment and HR screening AI | Social (4) + Institutional (5) | HIGH |
| 5. Essential services | AI credit scoring systems | Institutional (5) | HIGH |
| 6. Law enforcement | Lie detection and risk assessment AI | Psychological (3) + Institutional (5) | HIGH |
| 7. Migration | Asylum processing AI | Institutional (5) + Civilisational (6) | HIGH |
| 8. Justice | Legal outcome prediction AI | Institutional (5) | HIGH |

---

### Annex D — HNS Runtime Architecture (Informative)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     HNS Runtime Architecture                            │
│                                                                         │
│  ┌──────────────┐     ┌───────────────┐     ┌─────────────────────┐    │
│  │  AI System   │────▶│  AI Output    │────▶│    EVA Sidecar      │    │
│  │  (opaque)    │     │  (text/action)│     │  HNS-36 attribution │    │
│  └──────────────┘     └───────────────┘     │  HNS-864 risk score │    │
│                                             │  PROV-O JSON-LD log │    │
│                                             └──────────┬──────────┘    │
│                                                        │               │
│                              ┌─────────────────────────▼──────────┐    │
│                              │          ECS                        │    │
│                              │  PASS ──▶ DELIVER                  │    │
│                              │  FLAG ──▶ DELIVER_WITH_FLAG         │    │
│                              │  HOLD ──▶ HOLD_FOR_REVIEW           │    │
│                              │  FAIL ──▶ BLOCK                    │    │
│                              └──────────────────┬─────────────────┘    │
│                                                 ▼                      │
│                              ┌──────────────────────────────────────┐  │
│                              │  Human Oversight Operator            │  │
│                              │  (EU AI Act Art. 14; CoE CETS 225    │  │
│                              │   Art. 16; ISO/IEC 38507:2022)       │  │
│                              └──────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Annex E — 80-Standard × HNS Component Alignment Matrix (Normative)

✓ = primary implementation · ○ = supporting role · — = not applicable

| Standard / Instrument | Body | HNS-36 | EVA | ECS | HumanOS |
|---|---|---|---|---|---|
| ISO/IEC 42001:2023 | ISO/IEC | ✓ §6.1 | ✓ §9.2 | ○ | ✓ §5 |
| ISO/IEC 42005:2025 | ISO/IEC | ✓ impact | ✓ log | ○ | ✓ |
| ISO/IEC 23894:2023 | ISO/IEC | ✓ wellbeing | Risk log | ○ | Policy |
| ISO/IEC 22989:2022 | ISO/IEC | Terminology | IRI vocab | — | Defs |
| ISO/IEC 23053:2022 | ISO/IEC | ML map | ✓ | ○ | ✓ |
| ISO/IEC 24028:2020 | ISO/IEC | Trust | ✓ | ○ | ✓ |
| ISO/IEC 24027:2021 | ISO/IEC | Bias (144) | ✓ | ✓ | ✓ |
| ISO/IEC 24029-1:2021 | ISO/IEC | Robust. | ✓ | ✓ | ✓ |
| ISO/IEC 24030:2021 | ISO/IEC | Use cases | ✓ | ○ | ✓ |
| ISO/IEC 24368:2022 | ISO/IEC | V4 value | ✓ | ✓ | ✓ |
| ISO/IEC 5338:2023 | ISO/IEC | Lifecycle | ✓ | ✓ | ✓ |
| ISO/IEC 5259-1:2024 | ISO/IEC | Data qual. | ✓ | ○ | ○ |
| ISO/IEC TR 24372:2021 | ISO/IEC | Approach | ✓ | ○ | ○ |
| ISO/IEC 42006 (WD) | ISO/IEC | Cert. | ✓ | ✓ | ✓ |
| ISO/IEC 42105 (WD) | ISO/IEC | — | ○ | Art.14 | ✓ |
| ISO/IEC 38507:2022 | ISO/IEC | ○ | ○ | ○ | Governance |
| ISO/IEC 27001:2022 | ISO/IEC | ○ | A.8.15 | Physical Imm. | ✓ |
| ISO/IEC 27002:2022 | ISO/IEC | ○ | A.8.3,A.8.15 | Physical Imm. | ✓ |
| ISO/IEC 27701:2019 | ISO/IEC | Layer 3 | Privacy | ○ | Data gov |
| ISO/IEC 27017:2015 | ISO/IEC | ○ | Cloud log | ○ | ✓ |
| ISO/IEC 29100:2011 | ISO/IEC | Layer 3 | PII log | ○ | Privacy fw |
| ISO/IEC 29184:2020 | ISO/IEC | ○ | Transp. | ○ | ✓ |
| ISO/IEC 29119-1:2022 | ISO/IEC | ○ | Test doc | ✓ | Test proc. |
| ISO/IEC 29119-2:2021 | ISO/IEC | ○ | Test proc | ✓ | Test proc. |
| ISO/IEC 15288:2023 | ISO/IEC | Lifecycle | ✓ | ✓ | Lifecycle |
| ISO/IEC 24748-1:2018 | ISO/IEC | LCM | ○ | ○ | LCM |
| ISO/IEC 20000-1:2018 | ISO/IEC | ○ | ○ | ○ | Service mgmt |
| ISO 31000:2018 | ISO | ○ | Risk base | ○ | Policy |
| ISO 9001:2015 | ISO | ○ | ○ | ○ | Quality |
| ISO/IEC 25010:2023 | ISO/IEC | Quality | ✓ | ✓ | ○ |
| ISO/IEC 15408-1:2022 | ISO/IEC | ○ | Eval. | ✓ | ✓ |
| IEC 61508-1:2010 | IEC | ○ | ○ | Func. safety | ✓ |
| IEC 62304:2006 | IEC | ○ | ○ | Med. SW | ✓ |
| IEC 62443-2-1:2010 | IEC | ○ | ✓ | Industrial | ✓ |
| EU Charter Art.1,7,8,21,47 | EU | Found. | Found. | Found. | Found. |
| EU AI Act 2024/1689 | EU | Art.9,11 | ✓ Art.12,13 | Art.14 | Art.26 |
| GDPR 2016/679 | EU | Layer 3 | Lawful log | ○ | Data gov |
| NIS2 2022/2555 | EU | ○ | Art.23 | Art.21 BCP | ✓ |
| Cybersecurity Act | EU | ○ | Cert. | ✓ | ✓ |
| Digital Services Act | EU | Layer 4–5 | Transp. | ○ | ✓ |
| Data Act 2023 | EU | Layer 5 | Access | ○ | ✓ |
| MDR 2017/745 | EU | ○ | ✓ | Med. ctrl | ✓ |
| IVDR 2017/746 | EU | ○ | ✓ | Diag. ctrl | ✓ |
| Machinery Reg. | EU | ○ | ○ | Safety ctrl | ✓ |
| Product Liability Dir. | EU | ○ | Evidence | ○ | ✓ |
| AI Liability Dir. (prop.) | EU | ○ | Audit evid. | ○ | ✓ |
| JSON-LD 1.1 | W3C | Cell IRI | Schema | — | Vocab |
| RDF 1.1 | W3C | Ontology | Triple | — | Vocab |
| PROV-O | W3C | — | Audit rec. | — | — |
| OWL 2 | W3C | Classes | Props | — | Ontology |
| SPARQL 1.1 | W3C | ○ | Query | — | Audit |
| SKOS | W3C | Terms | Terms | — | Glossary |
| LDP 1.0 | W3C | ○ | Endpoint | — | ✓ |
| IEEE 7000-2021 | IEEE | V4 ethics | Ethics log | ✓ | ✓ |
| IEEE 7001-2021 | IEEE | ○ | Transp. | ○ | ✓ |
| IEEE 7002-2022 | IEEE | Layer 3 | Privacy | ○ | Data gov |
| IEEE 7010-2020 | IEEE | Wellbeing | Log | ✓ | ✓ |
| IEEE 7012 (draft) | IEEE | Layer 3 | Privacy | ○ | ✓ |
| IEEE P2863 | IEEE | ○ | ○ | ✓ | Org gov |
| NIST AI RMF GOVERN | NIST | ○ | ○ | ○ | Full impl |
| NIST AI RMF MAP | NIST | Full impl | ✓ | ○ | ✓ |
| NIST AI RMF MEASURE | NIST | 864 score | Full impl | ○ | ✓ |
| NIST AI RMF MANAGE | NIST | ○ | ○ | Full impl | ✓ |
| NIST SP 800-218 | NIST | ○ | ✓ | SDLC | ✓ |
| NIST SP 800-53 R5 | NIST | ○ | A.8 log | Access ctrl | ✓ |
| EO 14110 | US Govt | ○ | ○ | ○ | Federal gov |
| ITU-T Y.3172 | ITU-T | ○ | ✓ | Network | ✓ |
| ITU-T Y.3173 | ITU-T | Intelligence | ✓ | ○ | ✓ |
| ITU-T Y.3174 | ITU-T | ○ | Data hand. | ○ | ✓ |
| UN GA A/78/L.49 | UN | Layer 6 | ○ | ○ | SMS |
| CoE CETS 225 | CoE | Art.14-16 | Transp. | Art.16 over. | Governance |
| CEN/CENELEC JTC 21 | EU | EN harm. | ✓ | ✓ | ✓ |
| OECD AI Principles | OECD | P1.1-1.5 | ✓ | ✓ | ✓ |
| G7 Hiroshima | G7 | Layer 4-6 | Audit | ✓ | ✓ |
| UNESCO AI Rec. | UNESCO | Layer 4-6 | Ethics | ✓ | ✓ |
| Canada AIDA | Canada | ○ | ○ | ○ | Policy ref |
| China GB/T 42118 | China | ○ | ○ | ○ | Policy ref |

---

## Related Documents

### Primary Publications

| Publication | Author | Date | Type | Description |
|---|---|---|---|---|
| **The HNS Origin Trilogy: Brain Architecture as the Foundation of Trustworthy AI** | Hara, S. | May 2026 | Book (Amazon) | Foundational trilogy presenting MAV framework, HNS-36/144/864, SMS-6, structural isomorphism |
| **Human Natural Structure: Implementing the Brain's Multi-Axis Verification Process for Advanced AI Alignment** | Hara, S. | May 26, 2026 | Preprint | Operationalisation of MAV; 50-turn empirical evaluation; 100% auditability; <1% latency overhead |
| **The Multi-Axis Verification Process of the Human Brain** | Hara, S. | May 26, 2026 | Preprint | MAV formal specification; information-geometry proof; cognitive failure mode taxonomy |
| **EVA-HNS: A Structural Full-Stack Operating System for AI Alignment** | Hara, S. | May 24, 2026 | Working Paper | EVA-HNS architecture; 50-turn PoC; HNS Structural Stability Benchmark roadmap |
| **Structural OS for Human Understanding (SOHU)** | Hara, S. | May 22, 2026 | Preprint | SOHU five-layer stack; EVA integration; ISO/IEC 42001, EU AI Act, IEEE P7001 alignment |
| **External Verification Architecture (EVA)** | Hara, S. | May 8, 2026 | Publication | Hardware-anchored safety framework; EU AI Act, ISO/IEC 42001, CEN-CENELEC JTC 21 compatibility |
| **Human Natural Structure (HNS): Full Manuscript** | Hara, S. | April 2026 | Publication | HNS-36 matrix; conversational AI, alignment, safety, education, healthcare applications |

### Repository

All specifications, JSON-LD context files, and supporting materials are publicly available at:
**github.com/satoru-hara/03_NSW** · **naturalstructureworks.com**

---

*HNS-PoC-Package v2.0 · Satoru Hara · Natural Structure Works · 2026*
*github.com/satoru-hara/03_NSW · naturalstructureworks.com*
