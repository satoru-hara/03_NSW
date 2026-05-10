# Human Natural Structure as a Human-Meaning Operating System:
# A Structural Gap Analysis Against Prior Art

**Satoru Hara**
Independent Researcher
GitHub: https://github.com/satoru-hara/03_NSW

---

## Abstract

We argue that Human Natural Structure (HNS) occupies a structural position
in the AI architecture stack that has not previously been filled: a
lightweight, model-independent operating system for human meaning, spanning
intent, state, action, contextual compression, social scope, and
civilizational structure.

This paper establishes the argument in five steps. First, we define a
narrow, falsifiable claim composed of six target functions (F1–F6). Second,
we provide structural justification for each function: why Intent–State–Action
constitute the minimal OS kernel, why the 36-cell matrix is the minimal
contextual compression, why AI human-scope definition is an OS-level boundary
condition, and why HNS is model-independent across architectures. Third, we
systematically compare HNS against seven bodies of prior art — cognitive
architectures, foundational ontologies, knowledge graphs, AI alignment
methods, semantic memory OS frameworks, structured intent frameworks, and
Cognitive Alignment Science™ — and identify the precise boundary at which
each falls short. Fourth, we show that four major international standards
bodies (ISO/IEC, IEEE, EU AI Act, NIST) independently corroborate the
structural gap. Fifth, we acknowledge the current limitations of HNS and
define the empirical validation program required before the claim can be
considered established.

**Keywords:** human meaning representation, semantic operating system,
AI alignment, intent structure, human-scope definition, structural AI

---

## 1. Introduction

The rapid deployment of AI systems across high-stakes domains — healthcare,
autonomous vehicles, public administration, education — has exposed a
recurring structural problem: AI systems lack a principled coordinate system
for representing the human meaning space they must navigate. Hallucinations,
context drift, and misaligned outputs are symptoms of this underlying
structural absence.

Several research communities have approached aspects of this problem.
Cognitive architectures model individual human reasoning. Foundational
ontologies formalize concept hierarchies. AI alignment research constrains
AI behavior relative to human preferences. Semantic memory OS frameworks
manage AI memory as a system-level resource. Structured intent frameworks
formalize user intent as a communication protocol.

Despite this activity, we identify a structural gap: no prior framework
provides a unified, lightweight, model-independent OS that simultaneously
defines the intent, state, action, contextual, social, and civilizational
dimensions of the human meaning space that an AI system must represent.

Human Natural Structure (HNS) is a proposal to fill this gap. HNS is
itself positioned as a sub-OS within a broader Layered Coordinate System
(LCS) — a world-structure meta-OS spanning physical, biological, cognitive,
social, institutional, and civilizational layers (Hara, 2026b). HNS occupies
the human-specific subspace of LCS layers L3–L6.

---

## 2. The Falsifiable Claim

We make the following precise claim, which is falsifiable by counterexample:

> **Claim:** No prior framework provides a single, lightweight,
> model-independent structural OS that simultaneously instantiates all of
> the following six functions:
>
> (F1) Human **intent** structure
> (F2) Human **state** structure
> (F3) Human **action** structure
> (F4) **Contextual compression** (36-cell matrix)
> (F5) **Social and civilizational scope**
> (F6) **AI human-scope definition**

A valid counterexample must satisfy **all six** functions simultaneously.

---

## 2.1 Why Intent–State–Action Form an Operating System

HNS interprets human meaning as an operating system defined by three
irreducible axes:

- **Intent** — what the agent is trying to achieve
- **State** — the conditions under which the agent operates
- **Action** — the space of possible interventions

These axes satisfy OS criteria:

- **Minimality:** removing any axis collapses meaning representation.
- **Completeness:** any meaning unit can be located in this space.
- **Model-independence:** applies to LLMs, vision models, speech models,
  symbolic systems, and hybrid architectures.

Thus, Intent–State–Action constitute the minimal OS kernel for human meaning.

---

## 2.2 Why 36 Cells Are the Minimal Contextual Compression

The 36-cell matrix (6 layers × 6 categories) represents a compression
theorem for human context:

- 6 layers = vertical structure of meaning
- 6 categories = horizontal structure of meaning

The Cartesian product yields 36 structurally necessary cells.

This is the smallest matrix that satisfies:

- no semantic collisions
- universality
- reversible expansion to 144
- computational lightness

The claim that 36 is the minimum satisfying all constraints is empirical
and requires validation.

---

## 2.3 Why AI Human-Scope Definition Is an OS Boundary Condition

Different AI systems bear structurally different responsibilities:

- Medical AI → patient, family, medical team
- Autonomous vehicle AI → driver, passengers, pedestrians
- Administrative AI → citizens, institutions, legal frameworks
- Educational AI → learner, teacher, family

Scope determines:

- which intents must be represented
- which states must be tracked
- which actions must be constrained
- which contextual cells are relevant
- which norms apply

Without scope, an AI system operates in an unbounded meaning space —
a structural safety problem.

---

## 2.4 Hierarchical Relationship Between HNS and CAS™

CAS™ provides drift correction: dynamic detection, measurement, and
restoration of alignment over time.

HNS provides the coordinate system within which drift is defined.

Thus:

- **HNS = OS layer** (representation)
- **CAS™ = Application layer** (correction)

CAS™ presupposes a coordinate system; HNS defines it.

---

## 2.5 Model-Independence of HNS

HNS does not depend on:

- transformer architecture
- tokenization
- embedding geometry
- modality

Because HNS defines the **external coordinate system** for human meaning.

Thus, HNS applies to: LLMs, vision-language models, speech models,
multimodal models, symbolic systems, and hybrid neuro-symbolic architectures.

---

## 3. Systematic Prior Art Analysis

### 3.1 Cognitive Architectures (ACT-R, SOAR, CLARION)

Cognitive architectures provide the most rigorous prior formal treatment of
human cognition. ACT-R (Anderson et al., 2004) specifies declarative and
procedural memory with empirically calibrated timing parameters. SOAR
(Laird, 2012) implements a unified cognitive theory through production rules
and working memory. CLARION (Sun, 2006) models explicit and implicit
cognitive processes in a dual-process framework.

**Coverage of HNS functions:**

| Function | ACT-R | SOAR | CLARION |
|---|---|---|---|
| F1 Intent structure | Partial (goal stack) | Partial (goal stack) | Partial |
| F2 State structure | Partial | Partial | Partial |
| F3 Action structure | Yes | Yes | Yes |
| F4 Contextual compression | No | No | No |
| F5 Social/civilizational scope | No | No | No |
| F6 AI human-scope definition | No | No | No |

**Gap:** Cognitive architectures model the individual agent in computational
isolation. They were designed for cognitive simulation, not for providing an
external OS that any AI system can use to navigate human meaning.
F4–F6 were not design targets.

---

### 3.2 Foundational Ontologies (DOLCE, BFO, SUMO)

DOLCE (Gangemi et al., 2002) defines ontological categories with a
descriptive orientation. BFO (Smith et al., 2005) provides a realist upper
ontology widely adopted in biomedicine. SUMO (Niles & Pease, 2001) offers
a comprehensive formal upper ontology.

**Coverage of HNS functions:**

| Function | DOLCE | BFO | SUMO |
|---|---|---|---|
| F1 Intent structure | No | No | Partial |
| F2 State structure | Partial | Partial | Partial |
| F3 Action structure | Partial | No | Partial |
| F4 Contextual compression | No | No | No |
| F5 Social/civilizational scope | No | No | Partial |
| F6 AI human-scope definition | No | No | No |

**Gap:** Foundational ontologies define what exists, not what humans intend
or how meaning coordinates guide AI behavior. They lack intent, action,
and scope layers.

---

### 3.3 Knowledge Graphs (Wikidata, ConceptNet, Google KG)

ConceptNet (Speer et al., 2017) includes commonsense relations. Wikidata
provides structured factual knowledge. Google Knowledge Graph supports
semantic search at scale.

**Coverage of HNS functions:**

| Function | ConceptNet | Wikidata | Google KG |
|---|---|---|---|
| F1 Intent structure | No | No | No |
| F2 State structure | No | No | No |
| F3 Action structure | No | No | No |
| F4 Contextual compression | No | No | No |
| F5 Social/civilizational scope | Partial | Partial | No |
| F6 AI human-scope definition | No | No | No |

**Gap:** Knowledge graphs are descriptive, not prescriptive. They record
what is, not what structural coordinates should guide AI behavior.

---

### 3.4 AI Alignment Research (RLHF, Constitutional AI, Value Learning)

RLHF (Christiano et al., 2017) uses human preference signals to shape AI
policy. Constitutional AI (Bai et al., 2022) defines governing principles
for AI output. Value learning (Russell, 2019) infers human values from
behavior.

**Coverage of HNS functions:**

| Function | RLHF | Constitutional AI | Value Learning |
|---|---|---|---|
| F1 Intent structure | No | No | Partial |
| F2 State structure | No | No | No |
| F3 Action structure | Implicit | Implicit | Partial |
| F4 Contextual compression | No | No | No |
| F5 Social/civilizational scope | No | Partial | No |
| F6 AI human-scope definition | No | No | No |

**Gap:** Alignment research treats human values as an input to capture,
not as a coordinate system to represent.

---

### 3.5 Semantic Memory OS Frameworks (MemOS, MemGPT)

MemOS (Li et al., 2025) introduces a memory operating system for LLMs
managing parametric, activation, and plaintext memory through a unified
MemCube scheduling framework. MemGPT (Packer et al., 2024) implements
OS-inspired hierarchical memory management.

**Coverage of HNS functions:**

| Function | MemOS | MemGPT |
|---|---|---|
| F1 Intent structure | No | No |
| F2 State structure | Partial | Partial |
| F3 Action structure | No | No |
| F4 Contextual compression | No | No |
| F5 Social/civilizational scope | No | No |
| F6 AI human-scope definition | No | No |

**Gap:** These frameworks manage AI memory, not human meaning. MemOS manages
what the AI system remembers; HNS defines the coordinate system for what
the AI must understand. These are complementary layers.

---

### 3.6 Structured Intent Frameworks (PPS/5W3H, SCF)

PPS/5W3H (Peng, 2026) structures user intent using a 5W3H decomposition
and demonstrates cross-model robustness improvements. SCF (arXiv:2604.16339)
introduces a Semantic Intent Graph for multi-agent coordination.

**Coverage of HNS functions:**

| Function | PPS/5W3H | SCF |
|---|---|---|
| F1 Intent structure | Yes | Yes |
| F2 State structure | No | No |
| F3 Action structure | Partial | Yes |
| F4 Contextual compression | No | No |
| F5 Social/civilizational scope | No | No |
| F6 AI human-scope definition | No | No |

**Gap:** These operate at the interaction layer, not the OS layer.
PPS/5W3H's empirical results provide evidence for the value of structured
intent representation, supporting the practical relevance of HNS at the
OS level.

---

### 3.7 Cognitive Alignment Science™ (CAS™)

CAS™ (Pinar, 2025) defines cognitive drift across semantic, normative,
contextual, and temporal dimensions, and proposes a closed-loop correction
architecture with measurement indices (DQI, CII).

**Coverage of HNS functions:**

| Function | CAS™ |
|---|---|
| F1 Intent structure | No |
| F2 State structure | No |
| F3 Action structure | No |
| F4 Contextual compression | No |
| F5 Social/civilizational scope | No |
| F6 AI human-scope definition | No |

**Gap:** CAS™ provides drift correction within an alignment space; HNS
defines what that space is. The two frameworks are architecturally
complementary. CAS™ presupposes a coordinate system; HNS proposes to
define it.

---

## 4. Structural Position of HNS

The analysis in Section 3 supports the following architectural diagram.
HNS is itself positioned within the Layered Coordinate System (LCS),
a world-structure meta-OS that grounds HNS in physical, biological,
and civilizational context (Hara, 2026b).

```
┌──────────────────────────────────────────────────────┐
│          LCS — World-Structure Meta-OS               │
│  L1: Physical  L2: Biological  L3: Cognitive         │
│  L4: Social  L5: Institutional  L6: Civilizational   │
├──────────────────────────────────────────────────────┤
│             HNS — Human Meaning OS                   │
│  (sub-OS within LCS, occupying L3–L6)                │
│  F1: Intent  F2: State  F3: Action                   │
│  F4: Context (6L × 6C = 36 cells)                    │
│  F5: Social / Civilizational Scope                   │
│  F6: AI Human-Scope Definition                       │
├──────────────────┬───────────────────────────────────┤
│  CAS™            │  PPS / SCF                        │
│  (Alignment      │  (Structured intent               │
│   correction)    │   at interaction layer)           │
├──────────────────┴───────────────────────────────────┤
│  MemOS / MemGPT                                       │
│  (AI memory management)                              │
├──────────────────────────────────────────────────────┤
│  DOLCE / BFO / ConceptNet / Knowledge Graphs         │
│  (Encoding substrate / concept hierarchies)          │
├──────────────────────────────────────────────────────┤
│  Cognitive Architectures (ACT-R, SOAR, CLARION)      │
│  (Individual cognitive simulation)                   │
├──────────────────────────────────────────────────────┤
│  AI Models (LLM, Vision, Speech, Multimodal)         │
└──────────────────────────────────────────────────────┘
```

The diagram represents structural relationships, not hierarchies of value.
Each layer addresses a distinct problem. The claim is that the HNS layer
was structurally vacant before HNS, and that HNS itself is grounded within
the broader LCS coordinate system.

---

## 5. Standards Analysis as Independent Corroboration

Major standards bodies require human-meaning representation but do not
define it:

- **ISO/IEC 42001:2023** — requires context documentation but defines
  no structural representation of human intent or context.
- **EU AI Act, Article 14** — requires human oversight but defines no
  formal model of human intent and context.
- **IEEE 7001-2021** — requires explainability but defines no
  human-meaning coordinate system.
- **NIST AI RMF 1.0** — requires mapping affected humans but defines
  no structural model for human scope.

This convergence across four independent frameworks supports the existence
of the structural gap HNS fills.

---

## 6. Current Limitations and Required Validation

**6.1 Metrics undefined.**
HNS lacks quantitative indices comparable to CAS™'s DQI and CII.

**6.2 No temporal dynamics.**
HNS is static; drift over time is unmodeled. Integration with CAS™-style
correction mechanisms is a required next step.

**6.3 36-cell compression unvalidated.**
The claim that 6L × 6C provides sufficient granularity requires empirical
testing against representative human-AI interaction corpora.

**6.4 Peer review pending.**
The GitHub commit history and SSRN preprint establish priority of
conception, but independent peer review has not yet occurred.
Claims remain provisional.

**6.5 No interaction-layer benchmarks.**
PPS/5W3H demonstrates measurable performance improvements from structured
intent representation. HNS requires analogous benchmarks.

---

## 7. Conclusion

We have argued that Human Natural Structure occupies a structural position
— a human-meaning OS providing integrated intent, state, action, contextual,
social, and AI human-scope functions — that is not filled by any prior
framework. HNS is itself grounded within the Layered Coordinate System (LCS),
a world-structure meta-OS that provides physical and biological context for
human meaning.

This argument was established through:

- a falsifiable six-function claim
- structural justification for each function
- systematic comparison with seven bodies of prior art
- architectural positioning within LCS
- standards corroboration from four independent bodies

Two findings are central. First, Intent–State–Action is the minimal OS
kernel for human meaning. Second, HNS and CAS™ are complementary layers,
not competing frameworks: CAS™ corrects drift within a coordinate space
that HNS defines.

The limitations define the empirical validation program that must follow.

**We invite counterexamples as the most productive form of engagement.**

---

## References

Anderson, J. R., Bothell, D., Byrne, M. D., Douglass, S., Lebiere, C., &
  Qin, Y. (2004). An integrated theory of the mind. *Psychological Review*,
  111(4), 1036–1060.

Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., ...
  & Kaplan, J. (2022). Training a helpful and harmless assistant with
  reinforcement learning from human feedback. *arXiv:2204.05862*.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021).
  On the dangers of stochastic parrots: Can language models be too big?
  *Proceedings of FAccT 2021*, 610–623.

Berners-Lee, T., Hendler, J., & Lassila, O. (2001). The semantic web.
  *Scientific American*, 284(5), 34–43.

Christiano, P., Leike, J., Brown, T. B., Martic, M., Legg, S., & Amodei,
  D. (2017). Deep reinforcement learning from human preferences.
  *Advances in Neural Information Processing Systems (NeurIPS 2017)*,
  30, 4299–4307.

EU AI Act (2024). Regulation (EU) 2024/1689 of the European Parliament
  and of the Council. *Official Journal of the European Union*, L 2024/1689.

Gangemi, A., Guarino, N., Masolo, C., Oltramari, A., & Schneider, L.
  (2002). Sweetening ontologies with DOLCE. *Proceedings of EKAW 2002*,
  LNCS 2473, 166–181.

Hara, S. (2026a). Human Natural Structure (HNS): A structural operating
  system for human understanding in AI. *Preprint*, GitHub:
  https://github.com/satoru-hara/03_NSW

Hara, S. (2026b). Layered Coordinate System (LCS): Formal Specification.
  GitHub: https://github.com/satoru-hara/03_NSW/blob/main/
  HNS_Layered_Coordinate_System.md

IEEE (2021). *IEEE 7001-2021: Transparency of Autonomous Systems*. IEEE.

ISO/IEC (2023). *ISO/IEC 42001:2023 — Artificial Intelligence —
  Management System*. International Organization for Standardization.

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., ... & Fung, P.
  (2023). Survey of hallucination in natural language generation.
  *ACM Computing Surveys*, 55(12), 1–38.

Laird, J. E. (2012). *The Soar Cognitive Architecture*. MIT Press.

Li, Z., et al. (2025). MemOS: A Memory OS for AI System.
  *arXiv:2507.03724*.

Niles, I., & Pease, A. (2001). Towards a standard upper ontology.
  *Proceedings of the International Conference on Formal Ontology in
  Information Systems (FOIS 2001)*, 2–9.

NIST (2023). *Artificial Intelligence Risk Management Framework
  (AI RMF 1.0)*. National Institute of Standards and Technology.
  https://doi.org/10.6028/NIST.AI.100-1

Packer, C., Fang, V., Patil, S. G., Lin, K., Wooders, S., & Gonzalez,
  J. E. (2024). MemGPT: Towards LLMs as operating systems.
  *arXiv:2310.08560*.

Peng, G. (2026). Structured intent as a protocol-like communication
  layer: Cross-model robustness, framework comparison, and the weak-model
  compensation effect. *arXiv:2603.29953*.

Pinar, A. (2025). *Cognitive Alignment Science™*. Regen AI Institute.
  https://cognitivealignmentscience.com

Russell, S. (2019). *Human Compatible: Artificial Intelligence and the
  Problem of Control*. Viking.

Smith, B., Ashburner, M., Rosse, C., Bard, J., Bug, W., Ceusters, W.,
  ... & Lewis, S. (2005). The OBO Foundry: Coordinated evolution of
  ontologies to support biomedical data integration. *Nature
  Biotechnology*, 25(11), 1251–1255.

Speer, R., Chin, J., & Havasi, C. (2017). ConceptNet 5.5: An open
  multilingual graph of general knowledge. *Proceedings of AAAI 2017*,
  4444–4451.

Sun, R. (2006). The CLARION cognitive architecture: Extending cognitive
  modeling to social simulation. In R. Sun (Ed.), *Cognition and
  Multi-Agent Interaction*. Cambridge University Press, 79–99.

---

*Version 2.2 (Final) — April 2026.*
*Structural framework by Satoru Hara.*
*This document is submitted for peer review and comment.*

