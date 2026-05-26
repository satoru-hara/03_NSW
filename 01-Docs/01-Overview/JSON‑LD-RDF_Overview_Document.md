# JSON-LD / RDF Overview

**HNS-PoC-Package v1.0 · Technical Overview**
*Satoru Hara — Natural Structure Works (NSW)*
*2026 · github.com/satoru-hara/03_NSW*

---

## Table of Contents

1. [What are RDF and JSON-LD?](#1-what-are-rdf-and-json-ld)
2. [Why They Matter for AI](#2-why-they-matter-for-ai)
3. [Global Adoption](#3-global-adoption)
4. [Relation to HNS](#4-relation-to-hns)
5. [HNS Implementation Examples](#5-hns-implementation-examples)
6. [Alignment with International Standards](#6-alignment-with-international-standards)
7. [Summary](#7-summary)

---

## 1. What are RDF and JSON-LD?

### 1.1 RDF — Resource Description Framework

**RDF (Resource Description Framework)** is a W3C standard (first published 1999; current version RDF 1.1, 2014) for representing information as machine-readable, globally-identifiable statements.

The central innovation of RDF is the **triple**: every statement takes the form:

```
Subject — Predicate — Object
```

Each element is identified by a globally unique **IRI** (Internationalised Resource Identifier), making every RDF statement independently interpretable by any machine, anywhere, without loss of meaning.

**Example:**
```
Subject:   <https://nsw.example.org/hns/cell/L3C3>
Predicate: <https://nsw.example.org/hns#axis>
Object:    2
```
> *"Cell L3C3 belongs to Axis 2."*

RDF triples are composable across distributed systems, queryable via **SPARQL** (the W3C standard RDF query language), and the foundational data model of the Semantic Web and all major Knowledge Graph architectures.

---

### 1.2 JSON-LD — JSON for Linked Data

**JSON-LD (JSON for Linked Data)** is a W3C Recommendation (2013; updated to version 1.1 in 2020) that expresses RDF in JSON — the ubiquitous data format of modern web APIs.

JSON-LD adds a `@context` object to a standard JSON document that maps local keys to global IRIs from published vocabularies, transforming an ordinary JSON document into a fully-specified RDF graph.

A JSON-LD document is simultaneously:

| Property | Status |
|---|---|
| Valid JSON | ✅ Readable by any JSON parser |
| RDF graph | ✅ Full semantic precision |
| Schema.org-compatible | ✅ Indexable by Google / Bing |
| Machine-readable | ✅ Interpretable by AI systems |
| W3C Recommendation | ✅ Internationally standardised |
| API-friendly | ✅ Native to modern web stacks |

---

### 1.3 The RDF Triple Model

```
# Three triples describing HNS cell L3C3:

hns:L3C3  hns:axis      2 .
hns:L3C3  hns:layer     "L3 — Functional / Biological" .
hns:L3C3  hns:category  "C3 — Relation" .
```

Every element is globally identified. The predicate `hns:axis` is a published property whose semantics are formally specified in the HNS ontology. The entire graph is queryable via SPARQL.

---

### 1.4 Related W3C Standards

HNS builds on a family of complementary W3C standards:

| Standard | Version | Role in HNS |
|---|---|---|
| **RDF 1.1** | 2014 | Core data model for all HNS cells and records |
| **JSON-LD 1.1** | 2020 | Native serialisation format for HNS |
| **SPARQL 1.1** | 2013 | Query language for HNS data |
| **OWL 2** | 2012 | Ontology language for HNS class definitions |
| **SHACL** | 2017 | Validation of HNS JSON-LD documents |
| **PROV-O** | 2013 | Provenance tracking for EVA audit records |
| **W3C Verifiable Credentials** | 2022 | Tamper-evident HNS verification certificates |

---

## 2. Why They Matter for AI

### 2.1 The Semantic Gap in AI

Current large language models generate statistically fluent text, but their outputs are **semantically opaque**: there is no machine-readable representation of what was said, why it was generated, or how it relates to a formal knowledge structure.

**JSON-LD / RDF closes this gap** by providing a global standard for machine-readable meaning. When AI outputs are grounded in a JSON-LD / RDF structure — as HNS outputs are — every output is:

- Traceable to a **formal semantic coordinate**
- Logged in a **machine-readable audit record**
- Queryable by any system that speaks **SPARQL**

### 2.2 Key Applications in AI

| Application | Role of JSON-LD / RDF |
|---|---|
| **Knowledge Graphs** | Native data model (Google KG, Microsoft KG, EU KG) |
| **Search and ranking** | Schema.org structured data; rich snippets |
| **AI semantic grounding** | Formal meaning attached to AI outputs |
| **Audit and governance** | Machine-readable, legally admissible records |
| **Interoperability** | Cross-system data exchange without loss of meaning |
| **Standardisation** | W3C Recommendations referenced by ISO, IEC, CEN |

### 2.3 Why JSON-LD Over Plain JSON or XML

| Property | Plain JSON | XML / OWL | **JSON-LD** |
|---|---|---|---|
| Global identifiers (IRIs) | ✗ | ✓ (verbose) | **✓ (compact)** |
| API / Web friendly | ✓ | ✗ | **✓** |
| Machine-readable meaning | ✗ | ✓ | **✓** |
| SPARQL queryable | ✗ | ✓ | **✓** |
| Human readable | ✓ | Limited | **✓** |
| Schema.org compatible | ✗ | Limited | **✓** |
| W3C Recommendation | ✗ | ✓ | **✓** |
| LLM / AI API friendly | ✓ | ✗ | **✓** |

> JSON-LD is the only format that satisfies all requirements simultaneously.

---

## 3. Global Adoption

JSON-LD / RDF is not a niche standard. It is the infrastructure of the global knowledge web.

### 3.1 Technology Platforms

| Organisation | Platform / Product | JSON-LD / RDF Use |
|---|---|---|
| **Google** | Search, Knowledge Graph, Schema.org | Structured data; entity disambiguation; SERP features |
| **Microsoft** | Bing, Copilot, Azure AI | Linked Data; knowledge-augmented LLM grounding |
| **Meta** | Meta AI, Social Knowledge Graph | Open Graph Protocol (RDF-based); entity graphs |
| **Apple** | Siri, Spotlight | Schema.org markup for entity understanding |
| **Amazon** | Alexa, AWS | Knowledge Graph; product ontologies |

### 3.2 Government and Public Sector

| Organisation | Use |
|---|---|
| **European Union** | EU Knowledge Graph, Open Data Portal, DCAT-AP, EuroVoc (RDF/SKOS) |
| **UK Government** | data.gov.uk (RDF/Linked Data) |
| **US Government** | Data.gov, schema.org adoption across federal agencies |
| **UN / WHO** | ICD-11 (RDF/OWL), SNOMED CT clinical ontologies |

### 3.3 Scale

- **10M+** websites use Schema.org JSON-LD (Google recommendation)
- **100M+** RDF statements in Wikidata (open knowledge graph)
- **Pan-EU** mandate for DCAT-AP RDF in public sector data
- **Global** adoption in healthcare (HL7 FHIR supports JSON-LD)

---

## 4. Relation to HNS

### 4.1 HNS is Written Natively in JSON-LD / RDF

HNS is authored **natively** in JSON-LD and RDF. This is not a convenience choice; it is a structural commitment with four consequences:

1. **Semantic precision** — Every HNS cell has a globally unique IRI and formally specified properties
2. **Interoperability** — HNS is immediately readable by Google, Microsoft, EU, and W3C infrastructure
3. **Auditability** — EVA audit logs are machine-readable, SPARQL-queryable, and legally admissible
4. **Standardisation readiness** — HNS is expressed in the language that ISO, IEC, and CEN/CENELEC reference

### 4.2 HNS Ontology: Primary Classes

| HNS Component | RDF Class | Key Properties | Linked Standard |
|---|---|---|---|
| HNS-36 Cell | `hns:HNSCell` | `hns:layer`, `hns:category`, `hns:axis` | Schema.org/Thing |
| HNS-144 Cell | `hns:HNS144Cell` | `hns:subjectiveObjective`, `hns:staticDynamic`, `hns:localGlobal`, `hns:necessaryContingent` | OWL:Class |
| HNS-864 Cell | `hns:HNS864Cell` | `hns:modalityIndex`, `hns:validityCondition` | OWL:NamedIndividual |
| SMS-6 Layer | `hns:SMSLayer` | `hns:domain`, `hns:groundingFunction`, `hns:failureMode` | SKOS:Concept |
| EVA Audit Record | `hns:AuditRecord` | `hns:cell`, `hns:smsLayer`, `hns:verdict`, `hns:token` | W3C PROV-O Activity |

### 4.3 What This Ensures

```
HNS (JSON-LD / RDF)
         │
         ├── Google Search / Knowledge Graph    → Schema.org compatible
         ├── Microsoft Copilot / Azure          → JSON-LD context readable
         ├── EU Knowledge Graph                 → RDF interoperable
         ├── ISO / IEC standardisation          → W3C Rec. referenced
         ├── CEN/CENELEC JTC 21                 → European TS submittable
         └── SPARQL endpoint                    → Machine-queryable audit
```

---

## 5. HNS Implementation Examples

### 5.1 HNS-36 Cell (JSON-LD)

```json
{
  "@context": {
    "@vocab":     "https://nsw.example.org/hns#",
    "rdfs":       "http://www.w3.org/2000/01/rdf-schema#",
    "schema":     "https://schema.org/",
    "label":      "rdfs:label",
    "comment":    "rdfs:comment",
    "axis":       "hns:axis",
    "layer":      "hns:causalLayer",
    "category":   "hns:cognitiveCategory",
    "sameAs":     "schema:sameAs"
  },
  "@id":      "https://nsw.example.org/hns/cell/L3C3",
  "@type":    "HNSCell",
  "label":    "L3C3 — Causal / Mechanism",
  "comment":  "Mechanistic explanation of causal relations.",
  "axis":     2,
  "layer":    "L3 — Functional / Biological",
  "category": "C3 — Relation",
  "sameAs":   "https://schema.org/MedicalCause"
}
```

> **Cell L3C3** sits at the intersection of the Functional/Biological causal layer (row 3) and the Relation cognitive category (column 3) in the HNS-36 base matrix.

---

### 5.2 HNS-144 Cell (JSON-LD)

```json
{
  "@context": "https://nsw.example.org/hns/context.jsonld",
  "@id":    "https://nsw.example.org/hns/cell/L3C3-OD",
  "@type":  "HNS144Cell",
  "parent": "hns:L3C3",
  "label":  "L3C3-OD — Causal/Mechanism [Objective, Dynamic]",
  "subjectiveObjective": "Objective",
  "staticDynamic":       "Dynamic",
  "localGlobal":         "Local",
  "necessaryContingent": "Necessary"
}
```

> HNS-144 expands each of the 36 base cells along **4 logical relation dimensions**, yielding 144 cells for Category Ambiguity suppression.

---

### 5.3 SMS-6 Layer (JSON-LD)

```json
{
  "@context": "https://nsw.example.org/hns/context.jsonld",
  "@id":    "https://nsw.example.org/hns/sms/SMS-4",
  "@type":  "SMSLayer",
  "label":  "SMS-4 — Economic Layer",
  "domain": "Resource and information equivalence",
  "groundingFunction":
    "Tests output value-relevance to the declared task",
  "failureModeAddressed": "hns:UnsupportedCausality",
  "brainAnalogue":
    "Orbitofrontal cortex value evaluation system"
}
```

---

### 5.4 EVA Audit Record (JSON-LD + W3C PROV-O)

```json
{
  "@context": {
    "hns":  "https://nsw.example.org/hns#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd":  "http://www.w3.org/2001/XMLSchema#"
  },
  "@id":      "https://nsw.example.org/hns/audit/AR-20260527-001",
  "@type":    ["hns:AuditRecord", "prov:Activity"],
  "hns:cell":     { "@id": "hns:L3C3" },
  "hns:smsLayer": { "@id": "hns:SMS-4" },
  "hns:verdict":  "PASS",
  "hns:token":    "therefore",
  "hns:axis":     2,
  "prov:startedAtTime": {
    "@type":  "xsd:dateTime",
    "@value": "2026-05-27T09:14:33Z"
  },
  "prov:wasAssociatedWith": {
    "@id": "https://nsw.example.org/hns/agent/hns36-runtime"
  }
}
```

> Every EVA audit record is:
> - An `hns:AuditRecord` — queryable via HNS SPARQL
> - A `prov:Activity` — queryable via PROV-O SPARQL
> - A JSON-LD document — readable by any JSON parser
> - Machine-readable and legally admissible

---

### 5.5 HNS Ontology (Turtle Syntax)

```turtle
@prefix hns:    <https://nsw.example.org/hns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .

# Class hierarchy
hns:HNSCell     a owl:Class ; rdfs:label "HNS Cell" .
hns:HNS144Cell  a owl:Class ; rdfs:subClassOf hns:HNSCell .
hns:HNS864Cell  a owl:Class ; rdfs:subClassOf hns:HNS144Cell .
hns:SMSLayer    a owl:Class ; rdfs:label "SMS Grounding Layer" .
hns:AuditRecord a owl:Class ; rdfs:label "EVA Audit Record" .

# Property definitions
hns:axis     a owl:DatatypeProperty ; rdfs:domain hns:HNSCell .
hns:verdict  a owl:DatatypeProperty ; rdfs:domain hns:AuditRecord .
hns:cell     a owl:ObjectProperty   ;
             rdfs:domain hns:AuditRecord ;
             rdfs:range  hns:HNSCell .
```

---

### 5.6 SPARQL Queries

```sparql
# Query 1: Retrieve all Axis 2 cells
PREFIX hns:  <https://nsw.example.org/hns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?cell ?label ?layer ?category WHERE {
  ?cell a              hns:HNSCell ;
        hns:axis       2 ;
        rdfs:label     ?label ;
        hns:causalLayer ?layer ;
        hns:cognitiveCategory ?category .
}
ORDER BY ?layer ?category

# Query 2: Retrieve all FAIL verdicts in the last 24 hours
SELECT ?record ?token ?cell ?smsLayer WHERE {
  ?record a            hns:AuditRecord ;
          hns:verdict  "FAIL" ;
          hns:token    ?token ;
          hns:cell     ?cell ;
          hns:smsLayer ?smsLayer ;
          prov:startedAtTime ?t .
  FILTER(?t > "2026-05-26T00:00:00Z"^^xsd:dateTime)
}
```

> HNS data is queryable by any organisation using standard SPARQL — no proprietary tooling required.

---

## 6. Alignment with International Standards

### 6.1 Standards Alignment Table

| Standard | Requirement | HNS JSON-LD Response | Status |
|---|---|---|---|
| **W3C JSON-LD 1.1** (2020) | Web-native Linked Data | HNS context file in JSON-LD 1.1; all cells globally addressable | ✅ Native |
| **W3C RDF 1.1** (2014) | Triple-based semantics | All HNS cells representable as RDF triples; SPARQL-queryable | ✅ Native |
| **W3C PROV-O** (2013) | Provenance tracking | EVA audit records as PROV-O Activity instances | ✅ Compatible |
| **ISO/IEC 42001:2023** | AI output quality documentation | AuditRecord JSON-LD instances constitute the required QA log | ✅ Satisfies |
| **ISO/IEC 23894:2023** | AI risk classification | Five-type HNS taxonomy as OWL classes; machine-classifiable | ✅ Compatible |
| **ISO/IEC TR 24028:2020** | AI explainability | Geometric verification certificates as JSON-LD | ✅ Compatible |
| **EU AI Act** (2024) | Transparency; conformity assessment | EVA logs as W3C Verifiable Credentials; EU KG-compatible RDF | ✅ Interoperable |
| **CEN/CENELEC JTC 21** | European AI standardisation | HNS JSON-LD context submittable as European Technical Specification | ✅ Pathway open |
| **NIST AI RMF 1.0** | Decision explanations | HNS coordinate triples as SPARQL-queryable decision records | ✅ Compatible |

### 6.2 Standardisation Pathways

```
HNS JSON-LD / RDF
         │
         ├── W3C Community Group Specification
         │     → Published HNS JSON-LD context file
         │     → SPARQL endpoint specification
         │
         ├── ISO/IEC JTC 1 / SC 42
         │     → NP proposal: HNS as AI verification vocabulary
         │     → Input document: this report + HNS-PoC-Package
         │
         └── CEN/CENELEC JTC 21
               → European Technical Specification
               → EU AI Act conformity assessment tool
```

---

## 7. Summary

| Point | Detail |
|---|---|
| **HNS native format** | JSON-LD 1.1 + RDF 1.1 (W3C Recommendations) |
| **Cell representation** | Each of 864 cells: globally unique IRI, type, properties |
| **Audit log format** | JSON-LD + W3C PROV-O; SPARQL-queryable |
| **Global compatibility** | Google, Microsoft, Meta, EU Knowledge Graph — all native |
| **Query interface** | SPARQL endpoint; no proprietary tooling required |
| **Standards compliance** | ISO/IEC 42001, 23894, TR 24028; EU AI Act; NIST AI RMF |
| **Standardisation path** | W3C Community Spec → ISO/IEC SC 42 → CEN/CENELEC JTC 21 |

### Key Message

> HNS does not need to be translated into the global AI and standards ecosystem.
> **It is already written in its native language.**
>
> JSON-LD / RDF makes HNS globally interoperable.
> HNS makes the brain's verification principle engineerable.

---

## References

- W3C. (2014). *RDF 1.1 Concepts and Abstract Syntax*. https://www.w3.org/TR/rdf11-concepts/
- W3C. (2020). *JSON-LD 1.1*. https://www.w3.org/TR/json-ld11/
- W3C. (2013). *SPARQL 1.1 Query Language*. https://www.w3.org/TR/sparql11-query/
- W3C. (2012). *OWL 2 Web Ontology Language*. https://www.w3.org/TR/owl2-overview/
- W3C. (2017). *Shapes Constraint Language (SHACL)*. https://www.w3.org/TR/shacl/
- W3C. (2013). *PROV-O: The PROV Ontology*. https://www.w3.org/TR/prov-o/
- W3C. (2022). *Verifiable Credentials Data Model v1.1*. https://www.w3.org/TR/vc-data-model/
- ISO/IEC 42001:2023. *Artificial Intelligence — Management System*. ISO.
- ISO/IEC 23894:2023. *AI — Guidance on Risk Management*. ISO.
- European Commission. (2024). *EU Artificial Intelligence Act*. Official Journal of the EU.
- Hara, S. (2026). *The HNS Origin Trilogy: Brain Architecture as the Foundation of Trustworthy AI*. Natural Structure Works.
- Hara, S. (2026). *HNS-PoC-Package v1.0*. github.com/satoru-hara/03_NSW

---

*HNS-PoC-Package v1.0 · Satoru Hara · Natural Structure Works · 2026*
*github.com/satoru-hara/03_NSW*
