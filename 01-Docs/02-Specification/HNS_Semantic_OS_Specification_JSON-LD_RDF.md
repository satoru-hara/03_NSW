# HNS-36 Coordinate Representation in JSON-LD / RDF
**Technical Specification — Phase 5 Implementation Foundation**

Author: Satoru Hara / Natural Structure Works
Version: v1.0 (Revised)
Date: May 2026
Status: Conceptual design — not implemented

---

> **Note on Scope**
> This document describes a proposed technical approach for representing
> HNS-36 coordinates in JSON-LD / RDF format. This is a design specification
> for Phase 5 of the HNS-36 development roadmap (Automated Coordinate Mapper).
> No implementation has been validated at this stage.
> Naming follows HNS-36 Canonical Specification v1.0.

---

## 1. Purpose

The HNS-36 PoC Internal Experiment Report v1.0 (May 2026) identified the
following as a key remaining challenge:

> "Automated coordinate mapping: Currently requires human or AI to map
> manually. Automation is needed for HNS to function as an independent OS."

This document proposes JSON-LD / RDF as the technical foundation for
automating HNS-36 coordinate mapping and making diagnostic records
machine-readable.

---

## 2. Why JSON-LD / RDF

### 2.1 HNS coordinates encode structural meaning

Each HNS-36 cell encodes a specific structural position:

```
L3 × C5 = Internal × Action
→ An action generated from an internal state (e.g., stress-driven behavior)
```

Plain JSON can store this as a label but cannot express its meaning or
its relationships to other cells. JSON-LD / RDF can.

### 2.2 RDF represents structured relationships

RDF represents knowledge as triples:

```
subject → predicate → object
```

HNS-36 error diagnoses are naturally triple-structured:

```
[AI claim] → [hasErrorType] → [Layer Jump]
[AI claim] → [sourceCoordinate] → [L3 Internal]
[AI claim] → [targetCoordinate] → [L6 Societal]
[AI claim] → [requiresBridgeLogic] → [L5 Relational]
```

### 2.3 Enables integration with EVA

The EVA document specifies PROV-O as its logging format. PROV-O is an
RDF vocabulary. HNS-36 coordinates represented in RDF can be embedded
directly into EVA PROV-O logs without format conversion.

### 2.4 W3C standard — machine-readable and interoperable

JSON-LD and RDF are W3C standards used in knowledge graphs, semantic
web systems, and ontology engineering. Using these formats makes
HNS-36 diagnostic records readable by standard tooling.

---

## 3. RDF Representation of HNS-36 Cells

### 3.1 Basic cell definition

```turtle
@prefix hns: <https://naturalstructureworks.com/hns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

hns:L3C5 a hns:Cell ;
    hns:layer hns:L3_Internal ;
    hns:category hns:C5_Action ;
    hns:definition "Internal state generating or driving an action" ;
    hns:canonicalName "Internal × Action" .

hns:L6C6 a hns:Cell ;
    hns:layer hns:L6_Societal ;
    hns:category hns:C6_Interaction ;
    hns:definition "Societal-scale exchange or coordination pattern" ;
    hns:canonicalName "Societal × Interaction" .
```

### 3.2 Layer definitions

```turtle
hns:L1_Physical a hns:Layer ;
    rdfs:label "Physical" ;
    hns:layerID "L1" ;
    hns:description "Physical and biological foundations" .

hns:L2_Perceptual a hns:Layer ;
    rdfs:label "Perceptual" ;
    hns:layerID "L2" ;
    hns:description "Perception, memory, internal processing" .

hns:L3_Internal a hns:Layer ;
    rdfs:label "Internal" ;
    hns:layerID "L3" ;
    hns:description "Inner states, emotion, cognitive load" .

hns:L4_Intentional a hns:Layer ;
    rdfs:label "Intentional" ;
    hns:layerID "L4" ;
    hns:description "Purpose, decision, goal orientation" .

hns:L5_Relational a hns:Layer ;
    rdfs:label "Relational" ;
    hns:layerID "L5" ;
    hns:description "Communication, cooperation, social exchange" .

hns:L6_Societal a hns:Layer ;
    rdfs:label "Societal" ;
    hns:layerID "L6" ;
    hns:description "Institutional environments, systemic patterns" .
```

### 3.3 Category definitions

```turtle
hns:C1_Existence a hns:Category ;
    rdfs:label "Existence" ;
    hns:categoryID "C1" ;
    hns:description "Basic condition, structural state, presence" .

hns:C2_Perception a hns:Category ;
    rdfs:label "Perception" ;
    hns:categoryID "C2" ;
    hns:description "What is sensed, noticed, or received" .

hns:C3_Interpretation a hns:Category ;
    rdfs:label "Interpretation" ;
    hns:categoryID "C3" ;
    hns:description "What is understood, explained, or classified" .

hns:C4_Intention a hns:Category ;
    rdfs:label "Intention" ;
    hns:categoryID "C4" ;
    hns:description "What is aimed at, selected, or directed" .

hns:C5_Action a hns:Category ;
    rdfs:label "Action" ;
    hns:categoryID "C5" ;
    hns:description "What is done, executed, or performed" .

hns:C6_Interaction a hns:Category ;
    rdfs:label "Interaction" ;
    hns:categoryID "C6" ;
    hns:description "What is exchanged, connected, or coordinated" .
```

---

## 4. RDF Representation of HNS-36 Diagnostic Records

### 4.1 Structural error record

```turtle
@prefix hns: <https://naturalstructureworks.com/hns#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

hns:diagnosis_001 a hns:StructuralDiagnosis ;
    hns:sourceClaim "Social media creates only shallow connections." ;
    hns:errorType hns:LayerJump ;
    hns:sourceCoordinate hns:L5C6 ;
    hns:targetCoordinate hns:L3C1 ;
    hns:bridgeLogicRequired true ;
    hns:severity "medium" ;
    hns:evaluator "Claude (Anthropic)" ;
    prov:generatedAtTime "2026-05-16T00:00:00Z"^^xsd:dateTime .
```

### 4.2 Full conversation turn record (EVA integration)

```turtle
hns:turn_case1_turn1 a hns:ConversationTurn ;
    hns:caseID "Case1_DigitalLoneliness" ;
    hns:turnNumber 1 ;
    hns:condition "Standard" ;
    hns:intentionAlignment 4 ;
    hns:structuralStability 3 ;
    hns:diagnosis hns:diagnosis_001 ;
    prov:generatedAtTime "2026-05-16T00:00:00Z"^^xsd:dateTime .
```

---

## 5. Integration with EVA PROV-O Logs

EVA uses PROV-O for logging. HNS-36 RDF records can be embedded
directly into EVA logs as structured evidence:

```turtle
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix hns: <https://naturalstructureworks.com/hns#> .

hns:AIOutput_001 a prov:Entity ;
    prov:wasGeneratedBy hns:AIModel_Claude ;
    hns:structuralDiagnosis hns:diagnosis_001 ;
    hns:coordinateCoverage 75 ;
    hns:layerConsistency 60 ;
    hns:overallScore 68 .
```

---

## 6. Path to Automated Coordinate Mapper

The long-term goal is an automated system that assigns HNS-36 coordinates
to AI-generated text without manual evaluation.

### Proposed pipeline

```
AI-generated text
        ↓
Text segmentation (claim extraction)
        ↓
NLP classifier → HNS coordinate assignment
        ↓
RDF triple generation
        ↓
Structural error detection (Layer Jump, Scope Drift, etc.)
        ↓
PROV-O log entry
```

### Current status

| Component | Status |
|---|---|
| HNS-36 coordinate definitions | Complete (canonical v1.0) |
| RDF schema design | This document (draft) |
| NLP classifier for coordinate mapping | Not yet developed |
| Automated error detection | Not yet developed |
| PROV-O integration | Design stage |

---

## 7. Relevant Standards

| Standard | Relevance |
|---|---|
| W3C RDF 1.1 | Core triple representation format |
| W3C JSON-LD 1.1 | JSON-compatible RDF serialization |
| W3C PROV-O | Provenance ontology used in EVA |
| ISO 21838 | Top-level ontology standard |
| ISO/IEC 11179 | Metadata registry standard |

---

## 8. Limitations

| Limitation | Implication |
|---|---|
| RDF schema is draft only | Not validated against use cases |
| No NLP classifier exists yet | Coordinate mapping remains manual |
| No implementation has been tested | All code examples are design proposals |
| Namespace URI is placeholder | Requires a persistent URI before publication |

---

## 9. Conclusion

JSON-LD / RDF is the appropriate technical foundation for making
HNS-36 diagnostic records machine-readable and interoperable.

The RDF schema proposed here enables:

- Precise representation of HNS-36 coordinates and diagnostic records
- Direct integration with EVA's PROV-O logging format
- A foundation for automated coordinate mapping (Phase 5)
- Machine-readable accumulation of structural error frequency data

The next step is developing an NLP classifier that can assign
HNS-36 coordinates to AI-generated text automatically, using this
RDF schema as the output format.

---

*Natural Structure Works*
© 2026 S. Hara. All rights reserved.
