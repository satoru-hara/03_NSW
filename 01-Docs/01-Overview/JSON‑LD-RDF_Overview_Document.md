# JSON-LD / RDF Overview (Short)

## 1. What are RDF and JSON-LD?

- **RDF (Resource Description Framework)**  
  - W3C standard (since 1999)  
  - Represents meaning as **triples**: `Subject - Predicate - Object`  
  - Basis of Semantic Web and Knowledge Graphs  

- **JSON-LD (JSON for Linked Data)**  
  - W3C Recommendation (2013, updated to 1.1 in 2020)  
  - Expresses RDF in **JSON**  
  - Web-native, API-friendly, AI-readable  

---

## 2. Why they matter for AI

- Provide a **global standard** for machine-readable meaning  
- Used for:
  - Knowledge Graphs  
  - Search and ranking  
  - Structured data on the Web  
  - AI semantic grounding and interoperability  

---

## 3. Global adoption

- **Google**: Search, Knowledge Graph, Schema.org  
- **Microsoft**: Bing, Copilot, Linked Data  
- **Meta**: Knowledge Graph  
- **EU**: EU Knowledge Graph, Open Data  

---

## 4. Relation to HNS

- HNS is written **natively in JSON-LD / RDF**  
- This ensures:
  - Compatibility with Google / Microsoft / EU ecosystems  
  - Machine-readable human structure (36-cell model)  
  - Readiness for standardization (ISO / CEN-CENELEC)  

---

## 5. One HNS cell example (JSON-LD)

```json
{
  "@context": {
    "@vocab": "https://nsw.example.org/hns#",
    "label": "rdfs:label",
    "description": "rdfs:comment"
  },
  "@id": "https://nsw.example.org/hns/cell/L3C3",
  "@type": "HNSCell",
  "label": "L3C3 - Causal / Mechanism",
  "description": "Mechanistic explanation of causal relations."
}
