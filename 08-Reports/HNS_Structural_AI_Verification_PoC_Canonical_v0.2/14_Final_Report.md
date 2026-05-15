# 13. Limitations

The HNS Structural AI Verification PoC is a prototype designed to demonstrate the
feasibility of external, model-independent reasoning verification.  
As such, it has several limitations that must be acknowledged.

These limitations fall into four categories:

1. Conceptual limitations  
2. Technical limitations  
3. Scope limitations  
4. Future-dependency limitations  

---

# 13.1 Conceptual Limitations

### 1. Not a truth detector  
HNS-36 evaluates **structure**, not **truth**.  
A structurally coherent answer may still contain factual errors.

### 2. Not a psychological model  
The PoC does not infer real human mental states.  
It only checks whether the AI’s claims about such states are structurally valid.

### 3. Not a full causal model  
The system checks for causal coherence but does not build a full causal graph.

### 4. Not a replacement for domain expertise  
HNS-36 ensures structural stability, but domain experts must still validate content.

---

# 13.2 Technical Limitations

### 1. Rule-based mapping  
The prototype uses deterministic rules, which may oversimplify ambiguous cases.

### 2. Limited semantic depth  
The system does not perform deep semantic parsing or world modeling.

### 3. No probabilistic reasoning  
The PoC does not estimate likelihoods or confidence levels.

### 4. No multimodal support  
Only text is supported.  
Images, audio, and video must be manually converted to text.

### 5. No cross-claim contradiction detection  
The system checks structure, not logical contradiction between claims.

---

# 13.3 Scope Limitations

### 1. Not designed for long documents  
The PoC is optimized for short to medium-length AI answers.

### 2. Not designed for creative writing  
Fictional content may intentionally violate structural norms.

### 3. Not designed for legal or medical decisions  
The PoC is not a compliance or diagnostic tool.

### 4. Not designed for multi-agent reasoning  
It evaluates a single answer, not interactions between multiple AI systems.

---

# 13.4 Future-Dependency Limitations

### 1. Dependent on Naming Spec v1.0  
Future versions of HNS-36 or EVA may refine naming or mapping rules.

### 2. Dependent on improved segmentation  
More advanced segmentation algorithms may increase accuracy.

### 3. Dependent on expanded violation taxonomy  
The current violation set is minimal and may expand in future versions.

### 4. Dependent on standardization progress  
Full utility depends on adoption by governance bodies and industry standards.

---

# 13.5 Summary of Limitations

+---------------------------+-----------------------------------------------+
| Category                  | Limitation Summary                            |
+---------------------------+-----------------------------------------------+
| Conceptual                | Structure-only, not truth or psychology       |
| Technical                 | Rule-based, text-only, no deep semantics      |
| Scope                     | Not for long docs, creative writing, or law   |
| Future Dependency         | Evolves with HNS/EVA standardization          |
+---------------------------+-----------------------------------------------+

The PoC demonstrates feasibility, but it is not a complete verification system.
