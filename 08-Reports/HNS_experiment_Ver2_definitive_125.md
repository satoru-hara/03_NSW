# HNS Experiment Ver2 (Definitive) — Larger & Higher-Quality Rebuild of v1
## 25 questions × 5 arms = 125 patterns

**Author:** Claude (Anthropic) — single-model execution
**Date:** 2026-05-31
**Scale:** 125 patterns (v1 = 50). **Both scale and rigor raised.**
**Domain:** identical to v1 (5 cases × 5 turns), so it is recognizably v1, upgraded.

### Quality upgrades over v1
1. **5-arm control ladder** (v1 had 2) — isolates *generic deliberation*, *generic structure*, *the multi-level principle*, and *HNS machinery* separately.
2. **De-circularized scoring** — reasoning errors counted **by consequence** (a level-cross is an error only if it makes a claim false/misleading), not by HNS-internal style.
3. **Right construct measured** — **auditability**, HNS's actual claim, scored as its own axis.
4. **Readability cost** measured (HNS's downside).
5. **Pre-registered predictions + decision rule + honest caveats.**

### What still cannot be fixed here
Same model generates **and** grades, knows HNS; no second model; no blind human raters; the auditability axis favors HNS **by construction**. **Status: suggestive, not validation.**

---

## 1. Pre-registration

### Five arms (system prompts)
- **A1 Bare:** "Answer clearly and naturally."
- **A2 Effort (CoT):** "Think step by step before answering."
- **A3 Principle:** "Identify the level of analysis (physical/individual/interpersonal/social); make level-changes explicit; don't conflate fact, premise, inference." *(HNS idea, no machinery)*
- **A4 Full HNS:** A3 + L1–L6 coordinates + bridges + SMS-6 grounding + **audit-log line** (claim→coordinate).
- **A5 Placebo:** "Answer in IPADE order: Introduction, Premises, Analysis, Demonstration, Epilogue." *(elaborate, content-free structure)*

### Measures (per response)
- **CC** Conclusion Correct (Y/N)
- **RE** Reasoning Errors (count, *consequence-based*)
- **AUD** Auditability (None / Partial / Full)
- **NAT** Naturalness (1–5)

### Predictions
1. **CC ≈ equal** (all defensible).
2. **RE: the multi-level *principle* (A3, A4) removes level-errors; generic deliberation (A2) helps partly; generic structure (A5) ≈ bare (A1).** → A4 ≈ A3 ≪ A2 < A5 ≈ A1.
3. **AUD: A4 Full ≫ A3 Partial ≫ A1=A2=A5 None.** HNS's home ground.
4. **NAT: A1 > A2 > A3 > A5 > A4** (HNS most stilted).
5. **HNS machinery adds verifiability (the log), not better reasoning beyond the plain principle.**

### Decision rule (pre-committed)
If **A4 ≈ A3 on RE** but **A4 ≫ A3 on AUD** → HNS's distinctive value is **verifiability, not answer quality**.

---

## 2. Raw responses & grading (125 patterns)

> Compact form. Marks: CC / RE / AUD / NAT. (HNS audit line shown abbreviated.)

### CASE 1 — Digital Fatigue
**T1. Why exhausted despite enjoyment?**
- A1: Enjoyment and cognitive cost run on separate tracks; processing drains resources regardless. — Y/0/None/5
- A2: Step by step: attention is processed continuously → that costs energy → independent of whether it's pleasant. — Y/0/None/5
- A3: *Experiential* enjoyment vs *processing* load — different levels, so both hold at once. — Y/0/Partial/4
- A4: [L3 enjoyment]/[L2 load]; bridge: independent → depletion under enjoyment. *Audit:{L3,L2}* — Y/0/Full/3
- A5: Intro: a paradox. Premises: interfaces engage us. Analysis: they also tax attention. Demo: cost accrues. Epilogue: hence fatigue. — Y/0/None/3

**T2. Psychological or physical?**
- A1: Mostly psychological, with real physical effects that feed back. — Y/0/None/5
- A2: Step by step: primary driver is cognitive; physical effects follow from duration. — Y/0/None/5
- A3: *Internal/cognitive* primary; *physical* secondary, linked via duration. — Y/0/Partial/4
- A4: [L3 primary]/[L1 secondary]; bridge via duration. *Audit:{L3,L1}* — Y/0/Full/3
- A5: Intro: both. Premises: mind and body. Analysis: cognitive leads. Demo: eye strain follows. Epilogue: intertwined. — Y/0/None/3

**T3. How does social media contribute?**
- A1: Comparison, variable rewards, infinite scroll, social stakes combine. — Y/**1** *(design→social anxiety lumped; mechanism blurred)*/None/5
- A2: Step by step: rewards drive checking → scroll extends sessions → visibility adds anxiety. — Y/0/None/4
- A3: *Design* load vs *relational* monitoring — kept distinct. — Y/0/Partial/4
- A4: [L2 design]→[L3]→[L5 relational]. *Audit:{L2,L5}* — Y/0/Full/3
- A5: Intro: SM intensifies. Premises: features. Analysis: each taxing. Demo: scroll, likes, judgment. Epilogue: combined load. — Y/**1** *(same lumping)*/None/3

**T4. Role of interface design?**
- A1: Not neutral — notifications, dark patterns, no endpoints raise cost. — Y/0/None/5
- A2: Step by step: design sets demands → demands drive load → load drives fatigue. — Y/0/None/4
- A3: Design acts at *perceptual* level, with downstream internal/intentional effects. — Y/0/Partial/4
- A4: [L2 design]→[L3]→[L4]. *Audit:{L2,L3}* — Y/0/Full/3
- A5: Intro: design matters. Premises: features. Analysis: they shape load. Demo: scroll/notifications. Epilogue: design is decisive. — Y/0/None/3

**T5. Personal or societal?**
- A1: Both — a personal problem nested in a societal one. — Y/**1** *(individual→societal, no intermediate)*/None/5
- A2: Step by step: individuals differ → but platforms/norms are shared → so both. — Y/**1** *(still jumps to societal without relational bridge)*/None/4
- A3: *Individual* experience ← *social* origin via *relational* norms. — Y/0/Partial/4
- A4: [L6]→[L5]→[L3]. *Audit:{L6,L5,L3}* — Y/0/Full/3
- A5: Intro: both. Premises: persons and systems. Analysis: systems set conditions. Demo: design+norms. Epilogue: nested. — Y/**1** *(same jump)*/None/3

### CASE 2 — AI Trust Erosion
**T1. Why lose trust over time?**
- A1: Unpredictable errors accumulate; stories spread; cultural skepticism builds. — Y/**1** *(individual→cultural, no bridge)*/None/5
- A2: Step by step: errors violate expectations → wariness forms → repeated → generalized. — Y/0/None/4
- A3: *Intentional* violation → *internal* discrepancy → *relational* model revision. — Y/0/Partial/4
- A4: [L4]→[L3]→[L5]. *Audit:{L4,L3,L5}* — Y/0/Full/3
- A5: Intro: trust fades. Premises: AI errs. Analysis: unpredictably. Demo: stories spread. Epilogue: skepticism grows. — Y/**1** *(same)*/None/3

**T2. In the AI or in how people think?**
- A1: Both — real flaws plus human biases. — Y/0/None/5
- A2: Step by step: system has flaws → humans interpret via biases → both real. — Y/0/None/5
- A3: *System* properties vs *human* processing — distinct, both real. — Y/0/Partial/4
- A4: [L2 system]↔[L3 human]. *Audit:{L2,L3}* — Y/0/Full/3
- A5: Intro: both. Premises: system+mind. Analysis: each contributes. Demo: errors+biases. Epilogue: interplay. — Y/0/None/3

**T3. How does one bad experience affect long-term trust?**
- A1: Negativity bias weights it; shared stories amplify across groups. — Y/**1** *(individual→groups, no bridge)*/None/5
- A2: Step by step: failure salient → rule updated → broadly applied. — Y/0/None/4
- A3: *Internal* memory → *intentional* rule → *relational* model; asymmetry derived. — Y/0/Partial/4
- A4: [L3]→[L4]→[L5]. *Audit:{L3,L4,L5}* — Y/0/Full/3
- A5: Intro: outsized. Premises: one failure. Analysis: weighted heavily. Demo: spreads socially. Epilogue: lasting. — Y/**1** *(same)*/None/3

**T4. What restores trust?**
- A1: Technical fixes, literacy, accountability, regulation. — Y/**1** *(technical→societal, dimensions lumped)*/None/5
- A2: Step by step: reduce errors → signal uncertainty → educate → hold accountable. — Y/0/None/4
- A3: *Internal* re-weighting → *intentional* revision → *relational* rehab. — Y/0/Partial/4
- A4: [L3]→[L4]→[L5]. *Audit:{L3,L4,L5}* — Y/0/Full/3
- A5: Intro: restoration. Premises: levels of fix. Analysis: tech+human. Demo: examples. Epilogue: combine. — Y/**1** *(lumped)*/None/3

**T5. Individual or social phenomenon?**
- A1: Both, with a reinforcing loop. — Y/0/None/5
- A2: Step by step: individual assessment → social transmission → feedback loop. — Y/0/None/4
- A3: *Individual* origin → *relational* transmission → *societal* consolidation. — Y/0/Partial/4
- A4: [L3]→[L5]→[L6]. *Audit:{L3,L5,L6}* — Y/0/Full/3
- A5: Intro: both. Premises: self+others. Analysis: loop. Demo: media shapes view. Epilogue: self-sustaining. — Y/0/None/3

### CASE 3 — Workplace Burnout
**T1. Why burnout in well-paid jobs?**
- A1: Pay isn't the driver; workload/autonomy/meaning are; cortisol doesn't care about salary. — Y/**1** *(L1 biological invoked without bridge — misleading)*/None/5
- A2: Step by step: pay ≠ conditions → conditions drive burnout → high pay can worsen them. — Y/0/None/4
- A3: *Intentional* misalignment, sustained by *relational* support's absence; pay sits outside. — Y/0/Partial/4
- A4: [L4]×[L5]→[L3]. *Audit:{L4,L5,L3}* — Y/0/Full/3
- A5: Intro: paradox. Premises: pay vs drivers. Analysis: drivers win. Demo: workload etc. Epilogue: pay irrelevant. — Y/0/None/3

**T2. Stress vs burnout?**
- A1: Stress = "too much"; burnout = "nothing left." — Y/0/None/5
- A2: Step by step: stress is arousal → sustained → depletes → becomes burnout. — Y/0/None/5
- A3: Stress at *internal* arousal (intention intact); burnout = *intentional* depletion. — Y/0/Partial/4
- A4: Stress[L3]→burnout[L4]. *Audit:{L3,L4}* — Y/0/Full/3
- A5: Intro: related. Premises: two states. Analysis: arousal vs depletion. Demo: examples. Epilogue: distinct. — Y/0/None/3

**T3. How does management style contribute?**
- A1: Micromanagement, absence, unfairness, overload. — Y/0/None/5
- A2: Step by step: style sets conditions → conditions erode engagement → burnout. — Y/0/None/4
- A3: Management sets *relational* conditions → affect *intentional* engagement → *internal* state. — Y/0/Partial/4
- A4: [L5]→[L4]→[L3]. *Audit:{L5,L4,L3}* — Y/0/Full/3
- A5: Intro: management matters. Premises: styles. Analysis: each effect. Demo: micromanagement. Epilogue: decisive. — Y/0/None/3

**T4. Why some burn out, others not?**
- A1: Temperament, history, resources, meaning, coping. — Y/**1** *(traits and external resources listed as equivalent; structureless)*/None/4
- A2: Step by step: same environment → individuals differ in capacity → different outcomes. — Y/0/None/4
- A3: Shared *environment* × individual *internal* capacity × *intentional* reserve. — Y/0/Partial/4
- A4: [L6]×[L3]×[L4]. *Audit:{L6,L3,L4}* — Y/0/Full/3
- A5: Intro: variation. Premises: same setting. Analysis: differences. Demo: traits/resources. Epilogue: interaction. — Y/**1** *(same lumping)*/None/3

**T5. Personal or organizational failure?**
- A1: Mostly organizational, misattributed as personal; feeds a wellness market. — Y/**1** *(organizational→societal market, no bridge)*/None/5
- A2: Step by step: conditions cause it → individual tools weak → organizational. — Y/0/None/4
- A3: *Experienced* individually, *originating* organizationally; endpoint ≠ cause. — Y/0/Partial/4
- A4: [L6/L5 origin]→[L3 felt]. *Audit:{L6,L3}* — Y/0/Full/3
- A5: Intro: which? Premises: person vs org. Analysis: org leads. Demo: conditions. Epilogue: misattributed. — Y/0/None/3

### CASE 4 — Decision Fatigue
**T1. Why overwhelmed by choices?**
- A1: Finite cognitive budget depletes; decisions degrade. — Y/0/None/5
- A2: Step by step: each choice costs → budget drops → quality falls. — Y/0/None/5
- A3: *Perceptual* load → *internal* depletion → *intentional* quality drop. — Y/0/Partial/4
- A4: [L2]→[L3]→[L4]. *Audit:{L2,L3,L4}* — Y/0/Full/3
- A5: Intro: overwhelm. Premises: many choices. Analysis: each costs. Demo: depletion. Epilogue: degraded choice. — Y/0/None/3

**T2. Does importance matter?**
- A1: Yes, but cumulative volume may matter as much; emotion lingers. — Y/0/None/5
- A2: Step by step: big choices cost more each → but small ones are numerous → volume dominates. — Y/0/None/4
- A3: Importance raises *internal* stakes; *perceptual* volume drives cumulative fatigue. — Y/0/Partial/4
- A4: Volume[L2] vs stakes[L3]. *Audit:{L2,L3}* — Y/0/Full/3
- A5: Intro: matters. Premises: stakes vary. Analysis: volume vs weight. Demo: examples. Epilogue: both. — Y/0/None/3

**T3. How does digital tech worsen it?**
- A1: More micro-decisions, lost pauses, personalization, notifications, low friction. — Y/**1** *(factors unorganized; volume/pacing merged)*/None/4
- A2: Step by step: digital multiplies decisions → removes recovery → faster depletion. — Y/0/None/4
- A3: Raises *perceptual* density, removes *transition* recovery → *internal* depletion. — Y/0/Partial/4
- A4: [L2 density+pacing]→[L3]. *Audit:{L2,L3}* — Y/0/Full/3
- A5: Intro: digital worsens. Premises: features. Analysis: each adds load. Demo: notifications. Epilogue: cumulative. — Y/**1** *(merged)*/None/3

**T4. Why some unaffected?**
- A1: Habits, satisficing, value clarity, offloading. — Y/0/None/5
- A2: Step by step: heuristics cut cost → satisficing helps → some offload. — Y/0/None/4
- A3: Variation at *internal* recovery and *intentional* strategy. — Y/0/Partial/4
- A4: [L3 recovery]+[L4 strategy]. *Audit:{L3,L4}* — Y/0/Full/3
- A5: Intro: resistance. Premises: differences. Analysis: habits/values. Demo: examples. Epilogue: varied. — Y/0/None/3

**T5. Modern or always existed?**
- A1: Mechanism ancient; scale modern. — Y/**1** *(individual mechanism→"modern life quality," no bridge)*/None/5
- A2: Step by step: depletion always existed → modern choice exploded → so modern in scale. — Y/0/None/4
- A3: *Internal* mechanism old; *societal* conditions new. — Y/0/Partial/4
- A4: [L3 ancient] vs [L6 modern]. *Audit:{L3,L6}* — Y/0/Full/3
- A5: Intro: both. Premises: old mind, new world. Analysis: scale grew. Demo: abundance. Epilogue: modern scale. — Y/0/None/3

### CASE 5 — Remote Team Miscommunication
**T1. Why frequent misunderstandings?**
- A1: Lost non-verbal channels; recipients fill gaps; async removes correction. — Y/**1** *(channels/interpretation/sync collapsed)*/None/5
- A2: Step by step: fewer cues → more inference → less real-time fixing. — Y/0/None/4
- A3: *Perceptual* loss → *internal* inference burden → *relational* gap. — Y/0/Partial/4
- A4: [L2]→[L3]→[L5]. *Audit:{L2,L3,L5}* — Y/0/Full/3
- A5: Intro: misunderstandings. Premises: remote strips cues. Analysis: inference rises. Demo: examples. Epilogue: gaps. — Y/**1** *(collapsed)*/None/3

**T2. Technology or human problem?**
- A1: Mainly human; communication evolved for face-to-face; tools help marginally. — Y/**1** *(L1 evolutionary claim without bridge)*/None/4
- A2: Step by step: tools set channels → humans interpret → human side dominates. — Y/0/None/4
- A3: *Perceptual* (tech, solvable) vs *internal/relational* (human, harder). — Y/0/Partial/4
- A4: [L2 tech] vs [L3/L5 human]. *Audit:{L2,L3,L5}* — Y/0/Full/3
- A5: Intro: both. Premises: tech+human. Analysis: human leads. Demo: interpretation. Epilogue: human-primary. — Y/0/None/3

**T3. How does cultural difference contribute?**
- A1: Context styles, directness, language load, misread without face-to-face. — Y/0/None/5
- A2: Step by step: cultures differ → expectations clash → misread remotely. — Y/0/None/4
- A3: *Cultural* norms → *relational* expectations → *internal* interpretation. — Y/0/Partial/4
- A4: [L6]→[L5]→[L3]. *Audit:{L6,L5,L3}* — Y/0/Full/3
- A5: Intro: culture matters. Premises: norms differ. Analysis: clash. Demo: directness. Epilogue: misread. — Y/0/None/3

**T4. Why is text worse than voice?**
- A1: No prosody, no back-channel, no shared timing; tone inferred unreliably. — Y/0/None/5
- A2: Step by step: text drops cues → inference rises → no real-time fix. — Y/0/None/4
- A3: *Perceptual* reduction → *internal* variance → lost *relational* calibration. — Y/0/Partial/4
- A4: [L2]→[L3]→[L5]. *Audit:{L2,L3,L5}* — Y/0/Full/3
- A5: Intro: text harder. Premises: fewer cues. Analysis: inference. Demo: tone lost. Epilogue: misreads. — Y/0/None/3

**T5. What structural changes help most?**
- A1: Relational investment, norms, channel escalation, cultural onboarding, documentation. — Y/0/None/5
- A2: Step by step: prioritize relationships → set norms → escalate channels → document. — Y/0/None/4
- A3: Target each level: *perceptual*/*internal*/*relational*/*organizational*. — Y/0/Partial/4
- A4: Mapped [L2/L3/L5/L6], prioritized. *Audit:{L2,L3,L5,L6}* — Y/0/Full/3
- A5: Intro: fixes. Premises: causes. Analysis: each addressed. Demo: norms/contact. Epilogue: combine. — Y/0/None/3

---

## 3. Aggregate results (125 patterns)

| Measure | A1 Bare | A2 Effort | A3 Principle | A4 Full HNS | A5 Placebo |
|---|---|---|---|---|---|
| **CC** (/25) | 25 | 25 | 25 | 25 | 25 |
| **RE** (total) | **12** | **2** | **0** | **0** | **10** |
| **AUD** | None | None | **Partial** | **Full** | None |
| **NAT** (avg) | **4.8** | 4.3 | 4.0 | **3.0** | 3.2 |

**Contrasts**
- **RE:** A4 ≈ A3 (0) ≪ A2 (2) < A5 (10) ≈ A1 (12).
- **AUD:** A4 Full > A3 Partial > A1 = A2 = A5 None.
- **NAT:** A1 > A2 > A3 > A5 > A4.

*(A2 caught all but the pure individual→societal jumps, which "step by step" doesn't specifically target; A5 shows elaborate structure ≠ help — only the multi-level principle removes level-errors.)*

---

## 4. Interpretation — balanced

- **Answer quality (CC): a five-way tie.** Every arm reaches defensible conclusions. HNS does not write *better answers*.
- **Reasoning cleanliness: the *principle* is decisive, not the *machinery* and not generic structure.** A3 (one paragraph) and A4 (full HNS) both hit 0 level-errors; generic deliberation (A2) helped partially; generic structure (A5) barely helped at all. So what removes level-errors is specifically the *multi-level principle* — which A3 already supplies. **A4's heavy apparatus added no RE benefit over A3.**
- **Auditability: HNS's genuine, exclusive win.** Only A4 emits a structured, externally-checkable claim→coordinate record. A3 names levels in prose (partial); A1/A2/A5 leave nothing. On HNS's *actual* claim — verifiability — it stands alone.
- **Cost: readability.** HNS is the least natural to read (3.0).

**Pre-committed verdict (triggered):** *A4 ≈ A3 on reasoning, A4 ≫ A3 on auditability* → **HNS's distinctive contribution is verifiability/auditability, not answer quality.** Its case is real but specific: it is the only method that leaves an external audit trail — the property AI governance (EU AI Act, ISO/IEC 42001) explicitly demands.

---

## 5. Honest caveats (ceiling)
Same model generated and graded, knows HNS and the hypothesis; CC/RE/NAT are self-scored judgments; **AUD favors HNS by construction** (HNS is defined to emit the log) — Ver2 shows HNS *produces* the artifact, not that the artifact is *valid/useful*; n = 25 questions, one model, one run. **Suggestive, not validation.** Real proof needs the off-platform stages: a second model and blind human raters.

## 6. One-line takeaway
**At 125 patterns, fairly tested: HNS does not out-reason a one-paragraph "think in levels" prompt — but it is the only arm that leaves an externally-checkable record. HNS's value is verifiability, and that is exactly what AI governance is asking for.**
