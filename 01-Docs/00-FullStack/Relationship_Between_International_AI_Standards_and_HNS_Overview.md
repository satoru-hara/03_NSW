# Relationship Between International AI Standards and HNS

## Overview

**HNS-PoC-Package v1.0 · Overview Document**
*Satoru Hara — Natural Structure Works (NSW)*
*2026 · github.com/satoru-hara/03_NSW*

---

## Table of Contents

1. [The Core Relationship](#1-the-core-relationship)
2. [What International Standards Define](#2-what-international-standards-define)
3. [What International Standards Leave Undefined](#3-what-international-standards-leave-undefined)
4. [How HNS Fills the Gap](#4-how-hns-fills-the-gap)
5. [Standard-by-Standard Alignment](#5-standard-by-standard-alignment)
6. [The EVA-HNS Full-Stack Specification](#6-the-eva-hns-full-stack-specification)
7. [Standardization Pathway](#7-standardization-pathway)
8. [Summary](#8-summary)

---

## 1. The Core Relationship

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

---

## 2. What International Standards Define

The major international AI standards cover the *regulatory* dimensions of AI safety comprehensively:

### EU AI Act (Regulation 2024/1689)
- Classification of AI systems by risk level
- Mandatory requirements for high-risk AI: logging, transparency, human oversight, conformity assessment
- Post-market monitoring and incident reporting obligations

### ISO/IEC 42001 — AI Management System
- Governance and risk management processes for AI
- Documentation, internal audit, and continuous improvement
- Management review and AI policy frameworks

### ISO/IEC 23894 — AI Risk Management
- Identification, assessment, and treatment of AI-specific risks
- Monitoring of residual risks and societal impact
- Human wellbeing as a risk management objective

### NIST AI RMF 1.0
- Four-function framework: **GOVERN / MAP / MEASURE / MANAGE**
- Risk categorisation and quantitative risk assessment
- Accountability and governance structures

### ISO/IEC 22989 — AI Concepts and Terminology
- Shared vocabulary for AI systems
- Definitions for trustworthiness, transparency, and explainability

### IEEE Ethical AI Standards
- Ethical impact assessment in AI design
- Organisational governance for AI accountability
- Transparency mechanisms for AI decision-making

---

## 3. What International Standards Leave Undefined

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

Standards bodies do not define technical implementations by design — they are technology-neutral and jurisdiction-neutral. This is a feature of standards, not a flaw. But it creates a gap that the market must fill.

**HNS fills this gap.**

---

## 4. How HNS Fills the Gap

HNS provides the structural implementation layer that international AI standards require but do not define. It does so through four interconnected components:

### HNS — Human Natural Structure
A multi-resolution structural model of human cognition, implemented as a three-layer cellular matrix:

| Layer | Structure | Function |
|---|---|---|
| **HNS-36** | 6 layers × 6 categories = 36 cells | Universal structural baseline; coordinate system for all cognitive outputs |
| **HNS-144** | 36 cells × 4 logical dimensions = 144 cells | Category-level verification; concept boundary enforcement |
| **HNS-864** | 144 cells × 6 validity modalities = 864 cells | Proposition-level causal audit; structural risk scoring |

### EVA — External Verification Architecture
An independent structural verification layer that operates alongside — but separately from — the AI system being verified. EVA defines three structural conditions:

- **Verifiability** — every AI output attributed to a specific HNS coordinate; JSON-LD audit records
- **Transparency** — sidecar architecture; independent of the AI system's internal parameters
- **Physical Immutability** — hardware-anchored logic; tamper-evident audit trail

### ECS — External Control System
The executive control layer that implements human oversight requirements:

- **Output control** — blocks or modifies outputs that violate HNS structural conditions
- **Action constraints** — limits the action space of agentic AI systems
- **Risk boundary enforcement** — triggers alerts at defined structural risk thresholds
- **Emergency override** — immediate, hardware-level human intervention capability

### HumanOS — Integration Meta-Architecture
The integration layer that coordinates HNS, EVA, and ECS into a unified system-level architecture, addressing governance and policy requirements across standards.

---

## 5. Standard-by-Standard Alignment

### EU AI Act

| Requirement | Article | HNS / EVA / ECS Response |
|---|---|---|
| Technical documentation | Art. 11 | HNS-36 baseline; JSON-LD cell ontology |
| Logging | Art. 12 | EVA JSON-LD audit records (PROV-O Activity instances) |
| Transparency | Art. 13 | EVA sidecar architecture; structurally independent monitoring |
| Human oversight | Art. 14 | ECS output control and emergency override |
| Conformance testing | Art. 43 | HNS-36 baseline; SPARQL-queryable test suite |

---

### ISO/IEC 42001 — AI Management System

| Requirement | Clause | HNS / EVA / ECS Response |
|---|---|---|
| Risk identification | 6.1 | HNS-864 analytical engine; structural risk categories |
| Continuous improvement | 10.2 | EVA corrective cycle; structural drift detection |
| Human oversight | 8.4 | HNS-144 observational OS; ECS control mechanisms |
| Internal audit | 9.2 | EVA audit logs; machine-readable and SPARQL-queryable |

---

### ISO/IEC 23894 — AI Risk Management

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

### ISO/IEC 22989 — Terminology

| Requirement | HNS / EVA / ECS Response |
|---|---|
| Shared vocabulary | HNS JSON-LD / RDF ontology; all terms globally addressable via IRIs |
| Machine-readable definitions | HNS context file (JSON-LD 1.1); SPARQL-queryable |
| Trustworthiness definition | EVA structural conditions: Verifiability, Transparency, Physical Immutability |

---

## 6. The EVA-HNS Full-Stack Specification

The complete integration of HNS, EVA, ECS, and HumanOS constitutes the **EVA-HNS Full-Stack Specification** — the structural implementation layer that transforms AI safety standards from regulatory requirements into verifiable technical properties.

```
EVA-HNS Full-Stack Specification
│
├── HumanOS          → GOVERN (NIST) / ISO 42001 §5
│
├── HNS-36           → MAP (NIST) / ISO 42001 §6.1 / EU AI Act Art. 11, 43
│
├── HNS-144          → MAP + MEASURE / EU AI Act Art. 12 / ISO 42001 §8.4
│
├── HNS-864          → MEASURE / ISO 23894 / ISO 42001 §9.2
│
├── EVA              → MEASURE / EU AI Act Art. 12, 13 / ISO 42001 §9.2
│
└── ECS              → MANAGE / EU AI Act Art. 14 / NIST MANAGE
```

### What the Full Stack Provides That Standards Cannot

| Standards Provide | EVA-HNS Full Stack Provides |
|---|---|
| Logging *requirements* | Structured JSON-LD logs with HNS coordinate attribution |
| Transparency *requirements* | EVA sidecar architecture; independent structural monitoring |
| Human oversight *requirements* | ECS: structural implementation of "human-aligned" control |
| Risk assessment *requirements* | HNS-864: quantitative, proposition-level structural risk scoring |
| Conformance testing *requirements* | HNS-36: verifiable baseline with SPARQL-queryable test suite |
| Value alignment *requirements* | HNS natural layers: coordinate system mapping AI to human values |

---

## 7. Standardization Pathway

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

## 8. Summary

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

## Related Documents

| Document | Content |
|---|---|
| [The HNS Origin Trilogy](https://github.com/satoru-hara/03_NSW) | Three foundational papers on MAV, HNS implementation, and structural isomorphism |
| [HNS Correspondence Table Report](https://github.com/satoru-hara/03_NSW) | Structural mapping between human brain and HNS-aligned AI |
| [JSON-LD / RDF Overview](https://github.com/satoru-hara/03_NSW) | W3C technical foundation of HNS |
| [AI Standards and HNS: Full Alignment Report](https://github.com/satoru-hara/03_NSW) | Complete standard-by-standard alignment with implementation detail |

---

*HNS-PoC-Package v1.0 · Satoru Hara · Natural Structure Works · 2026*
*github.com/satoru-hara/03_NSW · naturalstructureworks.com*
