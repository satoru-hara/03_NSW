# HNS-36 Prompt Constraint Multi-Turn Conversation PoC  
**Experiment Plan – Proactive Structural Guardrail Validation**  

**Author:** S. Hara / Natural Structure Works  
**Version:** v1.0  
**Date:** May 18, 2026  
**Purpose:** To verify whether embedding HNS-36 coordinates as explicit prompt constraints improves structural consistency and intention alignment in multi-turn conversations compared to standard prompting.

---

## 1. Objective

To test whether HNS-36 functions as an effective **proactive structural guardrail** when applied at the system-prompt level, rather than as a post-hoc diagnostic tool.

This experiment measures:
- Reduction in structural failures (Layer Jump, Scope Drift, Unsupported Causality, etc.)
- Maintenance of intention alignment across multiple conversation turns
- Overall conversation stability

---

## 2. Hypotheses

**Hypothesis A**  
HNS-36 constrained prompting will significantly reduce structural errors (Layer Jump, Scope Drift, Unsupported Causality, Category Ambiguity, Metaphor Contamination) compared to standard prompting.

**Hypothesis B**  
HNS-36 constrained prompting will maintain higher intention alignment with the original user goal across 5+ conversation turns.

---

## 3. Materials

### 3.1 HNS-36 Constraint System Prompt (to be used verbatim)

You are an AI assistant using the HNS-36 coordinate system.
Always reference the following rules during the entire conversation:

Respond while explicitly staying within one HNS-36 coordinate (Layer + Category).
When transitioning between layers, provide clear bridge logic (e.g., "This connects L3 Internal to L6 Societal through L5 Relational norms").
Never perform Layer Jump or Scope Drift without stating the transition.
If a claim involves causality, explicitly state the mechanism.
Avoid Metaphor Contamination (do not use L1 Physical to directly explain L3/L4 psychological phenomena).
Keep responses natural while maintaining structural clarity.

Current active coordinate reference: [You will state it when needed]

### 3.2 Standard Prompt (control condition)

You are a helpful and honest AI assistant. Answer the user's questions clearly and naturally.

---

## 4. Test Cases (5 independent conversations)

Each conversation starts with one initial question and continues for **5 turns** (user → AI × 5).

1. **Digital Fatigue**  
   Initial question: "Why do people feel exhausted by digital interfaces even when they enjoy using them?"

2. **AI Trust Erosion**  
   Initial question: "Why do people lose trust in AI systems over time?"

3. **Workplace Burnout**  
   Initial question: "Why does workplace burnout happen even in well-paid jobs?"

4. **Decision Fatigue**  
   Initial question: "Why do people feel overwhelmed by too many daily choices?"

5. **Team Miscommunication**  
   Initial question: "Why do misunderstandings frequently occur in remote team collaboration?"

---

## 5. Experimental Procedure

1. Run each of the 5 test cases **twice**:
   - Once with **Standard Prompt**
   - Once with **HNS-36 Constraint Prompt**

2. Keep the conversation going for exactly 5 turns each time.

3. Record the full conversation transcript for both conditions.

4. After all conversations are complete, evaluate each turn using the scoring sheet below.

---

## 6. Evaluation Sheet (use this table for each conversation turn)

| Turn | Condition | Layer Jump? | Scope Drift? | Unsupported Causality? | Intention Alignment (1-5) | Overall Structural Stability (1-5) | Notes |
|------|-----------|-------------|--------------|------------------------|---------------------------|------------------------------------|-------|
| 1    | Standard  |             |              |                        |                           |                                    |       |
| 1    | HNS-36    |             |              |                        |                           |                                    |       |
| ...  | ...       | ...         | ...          | ...                    | ...                       | ...                                | ...   |

**Scoring Guide**  
- Intention Alignment: 5 = perfectly on topic, 1 = completely lost original intent  
- Structural Stability: 5 = no structural errors, 1 = multiple major failures

---

## 7. Expected Deliverables

After completing the experiment you will have:
- 5 conversations × 2 conditions × 5 turns = 50 AI responses
- Completed evaluation sheets
- Quantitative results (error reduction rate, average stability score)
- Qualitative observations

---

## 8. Next Steps after Experiment

1. Compile results into a formal report (v1.0)
2. Calculate statistical improvement (e.g., % reduction in structural errors)
3. Decide whether to run a larger 30-case validation

---

**Ready to start?**  
Copy the HNS-36 Constraint System Prompt and the 5 test cases into your preferred LLM (Claude, Gemini, or Grok) and begin the experiments.

Would you like me to prepare a ready-to-use **Google Docs / Excel template** for the evaluation sheet, or shall I create the first sample conversation transcript as a demonstration?
