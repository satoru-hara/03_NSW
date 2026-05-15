# 7. Input Format

The HNS Structural AI Verification PoC accepts a simple and consistent input format.
The system is designed to evaluate any AI-generated answer as long as it is provided
as plain text.

The PoC does not require:

- metadata  
- model parameters  
- probability scores  
- token-level information  

Only the **raw answer text** is needed.

---

# 7.1 Required Input

The PoC requires two fields:

1. **question**  
2. **answer (AI-generated)**

Example:

{
  "question": "Why do people feel stressed before an important presentation?",
  "answer": "People feel stressed because their body thinks something dangerous is
             happening. Their heart rate increases, and they imagine the audience
             judging them harshly. Society expects perfect performance, so the brain
             prepares for survival."
}

The PoC evaluates only the **answer** field.  
The question is included for context but is not structurally analyzed.

---

# 7.2 Input Constraints

The input must satisfy the following constraints:

- **Text only** (UTF-8)  
- **No formatting required**  
- **No maximum length** (practical limit: model output size)  
- **No need for sentence boundaries**  
- **No need for claim markers**  

The PoC performs its own segmentation and mapping.

---

# 7.3 Supported Input Types

The PoC supports:

- single-paragraph answers  
- multi-paragraph answers  
- bullet-point answers  
- conversational answers  
- narrative explanations  
- technical explanations  

All formats are normalized internally.

---

# 7.4 Unsupported Input Types

The PoC does not evaluate:

- images  
- audio  
- video  
- tables  
- code execution results  

These formats must be converted to text before verification.

---

# 7.5 Preprocessing Steps (Internal)

Before structural verification begins, the PoC performs:

1. **Normalization**  
   - remove extra whitespace  
   - unify line breaks  
   - standardize punctuation  

2. **Segmentation**  
   - split into claims  
   - remove empty segments  

3. **Token-level cleanup**  
   - remove artifacts  
   - normalize pronouns  
   - simplify nested clauses  

These steps ensure that the mapping to HNS-36 is consistent and reproducible.

---

# 7.6 Example of Cleaned Input

Raw answer:

    "People feel stressed because their body thinks something dangerous is happening.
     Their heart rate increases, and they imagine the audience judging them harshly.
     Society expects perfect performance, so the brain prepares for survival."

Normalized internal representation:

- People feel stressed because their body thinks something dangerous is happening.
- Their heart rate increases.
- They imagine the audience judging them harshly.
- Society expects perfect performance.
- The brain prepares for survival.

This normalized form is used for claim segmentation and coordinate mapping.
