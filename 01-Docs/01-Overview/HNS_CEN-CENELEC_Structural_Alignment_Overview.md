# HNS and CEN/CENELEC: Structural Alignment Overview

**HNS-PoC-Package v1.0 · Structural Alignment Overview**
*Satoru Hara — Natural Structure Works (NSW)*
*2026 · github.com/satoru-hara/03_NSW*

---

This document provides an overview of the structural alignment between
Human Natural Structure (HNS) and the European standardization bodies
CEN (European Committee for Standardization) and
CENELEC (European Committee for Electrotechnical Standardization).

The purpose of this overview is to clarify how HNS aligns with the
technical, structural, and regulatory requirements emerging from
EU AI Act–related standardization activities, and to identify the
specific pathways through which HNS can contribute to the development
of harmonized European AI standards.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Role of CEN/CENELEC in AI Standardization](#2-role-of-cencenelec-in-ai-standardization)
3. [The Standardization Gap in EU AI Act Implementation](#3-the-standardization-gap-in-eu-ai-act-implementation)
4. [Structural Alignment Between HNS and CEN/CENELEC Requirements](#4-structural-alignment-between-hns-and-cencenelec-requirements)
5. [Why HNS Is Structurally Relevant to CEN/CENELEC](#5-why-hns-is-structurally-relevant-to-cencenelec)
6. [The EVA-HNS Full-Stack Specification and EU Harmonization](#6-the-eva-hns-full-stack-specification-and-eu-harmonization)
7. [Implications for Standardization](#7-implications-for-standardization)
8. [Pathway for HNS Integration into CEN/CENELEC Work](#8-pathway-for-hns-integration-into-cencenelec-work)
9. [Conclusion](#9-conclusion)

---

## 1. Introduction

HNS (Human Natural Structure) is a structural operating system that
defines the cognitive invariants, interpretive coordinates, and
meaning-stability mechanisms underlying human reasoning. It is
implemented natively in JSON-LD / RDF — W3C Linked Data standards —
making it machine-readable, globally interoperable, and directly
compatible with the technical infrastructure of European AI governance.

CEN and CENELEC are responsible for developing harmonized standards
that operationalize the EU AI Act. Through their joint technical
committee **CLC/JTC 21 (Artificial Intelligence)**, they are developing
the EN standards that will define the technical requirements for safety,
transparency, risk management, and external verification of AI systems
deployed in the European Union.

HNS provides the structural foundation required for several of these
standardization domains. Specifically, HNS addresses the gap that
every major EU AI Act technical requirement faces: the absence of a
structural baseline for human cognition, behaviour, and meaning against
which AI system outputs can be formally verified.

This document explains where that alignment exists, why it matters for
CEN/CENELEC standardization work, and how HNS can be integrated into
the ongoing development of harmonized European AI standards.

---

## 2. Role of CEN/CENELEC in AI Standardization

CEN and CENELEC, operating jointly through **CLC/JTC 21**, develop EN
standards that:

- Implement the technical requirements of the EU AI Act
- Define harmonized technical specifications for AI safety, transparency,
  and risk management
- Establish verification and conformity assessment procedures for
  high-risk AI systems
- Provide operational guidance for AI system lifecycle management
- Ensure interoperability across EU member state regulatory frameworks

Once adopted as harmonized standards, EN standards create a presumption
of conformity with the corresponding EU AI Act requirements — meaning
that AI systems compliant with the EN standard are presumed compliant
with the law. This makes CLC/JTC 21 output the primary technical
implementation pathway for EU AI Act requirements.

CLC/JTC 21 operates in close coordination with **ISO/IEC JTC 1/SC 42**
(through the Vienna Agreement between CEN/CENELEC and ISO/IEC), which
means that standards developed in one body are routinely adopted by the
other. HNS contributions to CLC/JTC 21 therefore have direct relevance
to ISO/IEC JTC 1/SC 42, and vice versa.

---

## 3. The Standardization Gap in EU AI Act Implementation

The EU AI Act specifies *that* high-risk AI systems must be safe,
transparent, and human-aligned. CLC/JTC 21 is tasked with specifying
*how* these requirements are technically implemented. But a foundational
gap persists across all current standardization work:

> **There is no structural baseline for human cognition, behaviour, or
> meaning against which AI system outputs can be formally verified.**

Without such a baseline:

| EU AI Act Requirement | Standardization Challenge |
|---|---|
| **Transparency** (Art. 13) | Transparency against what reference? There is no structural definition of what an AI system should be transparent *about* |
| **Logging** (Art. 12) | Logs of what structure? There is no schema defining what logs should measure |
| **Human oversight** (Art. 14) | Oversight toward what baseline? There is no structural definition of "human-aligned" |
| **Conformity assessment** (Art. 43) | Conformity with what? There is no technical baseline for structural alignment |
| **Risk management** (Art. 9) | Risk relative to what human model? There is no structural model of human wellbeing |

HNS provides this missing baseline — a formally specified, machine-readable,
culturally neutral structural reference against which each of these
requirements can be implemented and verified.

---

## 4. Structural Alignment Between HNS and CEN/CENELEC Requirements

### 4.1 Meaning and Interpretive Stability

**CEN/CENELEC require:**
- Stable semantics across AI system outputs
- Consistent interpretation of AI outputs by human operators
- Human-aligned reasoning that does not drift across contexts

**HNS provides:**
- **Cognitive invariants**: the HNS-36 coordinate system defines the
  stable structural categories of human cognition that are universal
  across languages, cultures, and domains
- **Natural interpretive coordinates**: every AI output can be located
  within the 36-cell matrix, giving it a structurally defined meaning
  that is independent of the specific LLM generating it
- **Structural meaning stability**: the HNS-144 logical relation layer
  enforces category boundary conditions that prevent meaning drift
  across multi-turn interactions

### 4.2 External Verification (EVA)

**EU AI Act requires (Art. 12, 13, 43):**
- Independent verification of AI system behaviour
- Traceable reasoning logs
- Structural consistency checks across the AI system lifecycle

**HNS enables EVA by providing:**
- **Human-aligned reference structure**: HNS-36 is the structural baseline
  against which EVA verification is conducted
- **Verification baselines**: the 36/144/864-cell matrix defines
  precisely the structural properties that a verified output must satisfy
- **Semantic and causal invariants**: HNS-864 audits individual causal
  claims against a formally specified causal grammar, producing
  machine-readable audit records in JSON-LD / RDF format

EVA operates as a **sidecar architecture** — independent of the AI
system being verified, requiring no modifications to the AI system's
weights or architecture. This independence is the key property that
makes EVA compatible with CEN/CENELEC requirements for third-party
conformity assessment.

### 4.3 Safety and Control (ECS)

**CEN/CENELEC require:**
- Action constraints for AI systems operating in high-risk contexts
- Safety enforcement mechanisms capable of overriding AI system outputs
- Operational boundaries that prevent AI systems from violating
  defined safety thresholds

**HNS supports ECS by defining:**
- **Human-aligned behavioural expectations**: the HNS-36 coordinate
  system defines the structural boundaries of human-aligned behaviour,
  providing the reference against which ECS constraint conditions are
  defined
- **Structural constraints for safe operation**: ECS enforcement rules
  are expressed as HNS coordinate boundary conditions, making them
  formally specifiable, machine-executable, and auditable

ECS provides the **hardware-anchored** control mechanism that
EU AI Act Article 14 (human oversight) requires: a physical control
layer that cannot be overridden by the AI system itself.

### 4.4 Documentation and Transparency

**CEN/CENELEC require:**
- Technical documentation sufficient to demonstrate conformity
- Explainability: AI system reasoning must be understandable by humans
- Transparency: AI system behaviour must be traceable and auditable

**HNS provides:**
- **A unified cognitive framework**: HNS-36 provides the structural
  vocabulary in which AI system behaviour can be documented — not in
  system-specific terms, but in universal human cognitive coordinates
- **Natural explanation structures**: because HNS coordinates correspond
  to human cognitive categories, explanations expressed in HNS
  coordinates are inherently human-interpretable
- **Human-interpretable reasoning coordinates**: every EVA audit record
  is a JSON-LD document that can be read by both machines (via SPARQL)
  and humans (as structured text), satisfying dual explainability requirements

### 4.5 Interoperability and Cross-Border Compliance

**CEN/CENELEC require:**
- Standards that apply uniformly across all EU member states
- Technical specifications that are vendor-neutral and architecture-neutral
- Mechanisms for cross-border recognition of conformity assessments

**HNS provides:**
- **Vendor neutrality**: HNS operates as an external verification layer
  that does not modify the AI system it verifies; it applies equally
  to AI systems from any vendor
- **Architecture neutrality**: HNS-36/144/864 is defined over the
  abstract structure of cognitive outputs, not over specific model
  architectures or training methods
- **W3C standard foundation**: HNS is implemented in JSON-LD / RDF —
  W3C Recommendations that are adopted across all EU member states
  and referenced in EU data interoperability mandates (DCAT-AP, EuroVoc)

---

## 5. Why HNS Is Structurally Relevant to CEN/CENELEC

HNS is relevant to CEN/CENELEC standardization work for five reasons:

**1. It provides a universal human-aligned structure.**
The HNS-36 matrix is culturally neutral, jurisdiction-neutral, and
vendor-neutral. It is derived from the universal structure of human
cognition — not from any specific cultural, legal, or technical
convention. This makes it suitable as the structural baseline for
harmonized European standards that must apply uniformly across
27 member states with diverse languages, cultures, and legal traditions.

**2. It provides a stable reference for verification.**
Current AI verification approaches (RLHF, Constitutional AI, prompt-based
guardrails) cannot produce externally verifiable conformity evidence
because they encode alignment in opaque model parameters. HNS/EVA
produces explicit, machine-readable audit records expressed in W3C
standards, providing the stable reference that third-party conformity
assessment requires.

**3. It provides a cognitive baseline for safety.**
AI safety cannot be defined without a model of what "safe for humans"
means. HNS-36 provides this model — a formally specified coordinate
system for human cognitive structure that can serve as the safety
baseline for EU AI Act conformity assessment.

**4. It provides a structural foundation for harmonized standards.**
CEN/CENELEC EN standards must be technically precise, implementable,
and testable. HNS provides the structural vocabulary in which these
requirements can be expressed: specific HNS coordinates, specific
EVA verification conditions, specific ECS control thresholds.

**5. It is not a model or dataset; it is a structural OS.**
HNS does not compete with existing AI systems. It is a structural
operating system that can be applied across all AI architectures,
providing a consistent verification layer regardless of the underlying
model. This architecture-neutrality is essential for CEN/CENELEC
standards that must apply to the full diversity of AI systems deployed
in the EU.

---

## 6. The EVA-HNS Full-Stack Specification and EU Harmonization

The EVA-HNS Full-Stack Specification — comprising HNS-36/144/864, EVA,
ECS, and HumanOS — constitutes the complete structural implementation
layer for EU AI Act requirements. Its alignment with CEN/CENELEC
harmonization needs is summarised below:

| CLC/JTC 21 Work Area | EVA-HNS Component | EU AI Act Article |
|---|---|---|
| AI system transparency | EVA sidecar architecture + JSON-LD logs | Art. 13 |
| Technical documentation | HNS-36 structural baseline + JSON-LD ontology | Art. 11 |
| Risk management | HNS-864 analytical OS + EVA corrective cycle | Art. 9 |
| Human oversight | ECS output control + emergency override | Art. 14 |
| Conformity assessment | HNS-36 baseline + SPARQL test suite | Art. 43 |
| Post-market monitoring | EVA continuous logging + longitudinal SPARQL queries | Art. 61 |
| Serious incident reporting | EVA audit records (PROV-O Activity) + timestamp indexing | Art. 62 |

The EVA-HNS Full-Stack Specification is designed to generate **conformance
evidence** that can be submitted directly to a Notified Body for
EU AI Act conformity assessment — without any intermediate translation
or adaptation layer.

---

## 7. Implications for Standardization

HNS enables the following concrete standardization outcomes for
CLC/JTC 21:

**Consistent verification frameworks (EVA)**
EVA defines a vendor-neutral, architecture-neutral verification protocol
that can be specified as a CEN/CENELEC EN standard applicable to all
high-risk AI systems. The protocol is fully defined in W3C standards
(JSON-LD, RDF, SPARQL, PROV-O), making it directly referenceable in
EN standards without additional technical specification work.

**Safe operational control systems (ECS)**
ECS defines a hardware-anchored control architecture that satisfies
EU AI Act Article 14 human oversight requirements. Its specification
in terms of HNS structural coordinates makes it formally testable
and verifiable — properties that CLC/JTC 21 conformity assessment
procedures require.

**Harmonized semantic structures**
HNS-36, expressed in JSON-LD / RDF, provides a harmonized semantic
structure for AI system documentation that is directly compatible
with EU data infrastructure standards (DCAT-AP, EuroVoc, SEMIC).
This enables cross-border recognition of conformity evidence without
semantic translation.

**Cross-model interpretive stability**
Because HNS operates at the structural level of cognitive outputs —
not at the level of model architecture or training methodology — it
provides consistent interpretive stability across different AI systems,
vendors, and deployment contexts. This is the property that harmonized
standards require.

---

## 8. Pathway for HNS Integration into CEN/CENELEC Work

HNS can be integrated into CEN/CENELEC standardization work through
the following pathway:

### Step 1 — Technical Contribution to CLC/JTC 21
Submit the EVA-HNS Full-Stack Specification as a technical contribution
to CLC/JTC 21, documenting its alignment with EU AI Act Articles 9,
11, 12, 13, 14, 43, 61, and 62.

### Step 2 — W3C Community Specification
Publish the HNS JSON-LD context file as a W3C Community Group
Specification. W3C Community Specifications are referenceable in
CEN/CENELEC EN standards, providing the formal web standards
foundation for HNS terminology and data structures.

### Step 3 — New Work Item Proposal
Collaborate with CLC/JTC 21 member bodies to develop a New Work Item
Proposal (NWIP) for an EN standard defining the EVA verification
protocol, using HNS-36 as the structural baseline and JSON-LD as
the data format.

### Step 4 — Pilot Implementation
Conduct pilot implementations of HNS/EVA in high-risk AI deployments
(clinical decision support, legal reasoning, public sector AI) to
generate empirical conformance evidence for submission to CLC/JTC 21.

### Step 5 — Harmonized Standard Publication
Following CLC/JTC 21 review and approval, publish the EVA-HNS
specification as an EN standard, creating a presumption of conformity
with the relevant EU AI Act requirements for AI systems that implement
the standard.

---

## 9. Conclusion

HNS provides the structural basis required for several key
standardization domains under CEN/CENELEC. Its alignment with EU AI Act
requirements makes it a strong candidate for integration into future
harmonized EN standards developed by CLC/JTC 21.

The key points of this alignment are:

| HNS Component | CEN/CENELEC Relevance | EU AI Act Article |
|---|---|---|
| **HNS-36** | Universal structural baseline; conformity assessment reference | Art. 9, 11, 43 |
| **HNS-144** | Category-level semantic stability; transparency baseline | Art. 13 |
| **HNS-864** | Proposition-level causal audit; risk quantification | Art. 9, 12 |
| **EVA** | External verification architecture; independent conformity evidence | Art. 12, 13, 43 |
| **ECS** | Human oversight implementation; operational safety control | Art. 14 |
| **JSON-LD / RDF** | EU-interoperable data format; SPARQL-queryable audit records | Art. 12, 61, 62 |

HNS is positioned not as a competing technology, but as a structural
foundation that supports safe, interpretable, and verifiable AI systems
across the EU. It is the missing implementation layer that CEN/CENELEC
standardization work requires — and it is ready for integration.

> The EU AI Act defines what trustworthy AI must be.
> CEN/CENELEC defines how those requirements are technically specified.
> HNS defines the structural foundation on which those specifications can be built.

---

## Related Documents

| Document | Content |
|---|---|
| [The HNS Origin Trilogy](https://github.com/satoru-hara/03_NSW) | Foundational papers: MAV neuroscience, HNS implementation, structural isomorphism |
| [HNS Correspondence Table](https://github.com/satoru-hara/03_NSW) | Brain–AI structural mapping and EVA foundation |
| [JSON-LD / RDF Overview](https://github.com/satoru-hara/03_NSW) | W3C technical foundation of HNS |
| [AI Standards and HNS: Full Alignment](https://github.com/satoru-hara/03_NSW) | Complete standard-by-standard alignment |
| [AI Standards and HNS: Overview](https://github.com/satoru-hara/03_NSW) | Relationship overview across all major standards |

---

*© 2026 Satoru Hara / Natural Structure Works (NSW)*
*https://github.com/satoru-hara/03_NSW*
*https://www.naturalstructureworks.com/*
