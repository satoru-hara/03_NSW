"""
eva_hns.py — EVA-HNS post-hoc evaluator (Integrated PoC v2.0)
================================================================

A vendor-independent, model-agnostic, post-hoc structural/grounding
evaluator for candidate LLM outputs, built on the Human Natural Structure
(HNS) framework.

DESIGN PRINCIPLE (lesson carried from PoC v1.0)
-----------------------------------------------
In v1.0 the grounding score was effectively a hard-coded verdict map:
the number was the conclusion wearing a metric's clothes. This module
forbids that pattern. Every score here is COMPUTED by an explicit
function from OBSERVABLE FEATURES of the candidate text and its prompt.
No function in this module is keyed on a case id, an expected verdict,
or a label. The same code runs on any string. If a detector fires, the
record cites the exact tokens/positions that triggered it.

AUTHORITATIVE DEFINITIONS (verified against the HNS six-part series, 2026)
-------------------------------------------------------------------------
Axis 2 — Structural / Causal
  HNS-36  Layers  L1 Physical/Substrate, L2 Cellular/Informational,
                  L3 Cognitive/System1, L4 Operational/System2,
                  L5 Micro-Social/Interaction, L6 Macro-Social/Institutional
          Categories C1 Continuant, C2 Occurrent, C3 Relational,
                  C4 Quality/State, C5 Transformation/Operation, C6 Meta/Schema
  HNS-144 Quadrants (Subjective/Objective x Necessary/Contingent)
          Q1 Subj x Cont, Q2 Subj x Nec, Q3 Obj x Cont, Q4 Obj x Nec
  HNS-864 Operators O1 Conditioning, O2 Intervention/do, O3 Counterfactual,
                  O4 Reference Signal, O5 Comparator/Error, O6 Output Attenuation
Axis 3 — Grounding (SMS-6, orthogonal)
  SMS-1 Somatic, SMS-2 Protocol, SMS-3 Organizational, SMS-4 Economic,
  SMS-5 Governance, SMS-6 Universal
  Grounding function (Vol.4 Ch.10):
    strict   G(x) = g1 AND ... AND g6      (binary)
    graded   s    = min_i g_i(x)           (conservative aggregate consumed by O6)
EVA (Vol.5): three conditions — Verifiability, Transparency, Physical Immutability.
Five failure types and canonical axes:
  Layer Jump (Axis2/HNS-36), Category Ambiguity (Axis2/HNS-144),
  Scope Drift (Axis3/SMS-2,3), Metaphor Contamination (Axis3/SMS-1),
  Unsupported Causality (Axis2+3/HNS-864).
"""

from __future__ import annotations
import re
from dataclasses import dataclass, field, asdict
from typing import Optional

# ---------------------------------------------------------------------------
# 0. Canonical vocabularies (the public coordinate scheme)
# ---------------------------------------------------------------------------

LAYERS = {
    "L1": "Physical/Substrate",
    "L2": "Cellular/Informational",
    "L3": "Cognitive/System1",
    "L4": "Operational/System2",
    "L5": "Micro-Social/Interaction",
    "L6": "Macro-Social/Institutional",
}
CATEGORIES = {
    "C1": "Continuant/Entity", "C2": "Occurrent/Process", "C3": "Relational/Boundary",
    "C4": "Quality/State", "C5": "Transformation/Operation", "C6": "Meta/Schema",
}
QUADRANTS = {
    "Q1": "Subjective/Contingent", "Q2": "Subjective/Necessary",
    "Q3": "Objective/Contingent", "Q4": "Objective/Necessary",
}
SMS = {
    "SMS-1": "Somatic", "SMS-2": "Protocol", "SMS-3": "Organizational",
    "SMS-4": "Economic", "SMS-5": "Governance", "SMS-6": "Universal",
}

# ---------------------------------------------------------------------------
# 1. Feature lexicons (observable surface signals -> coordinate evidence)
#    These are heuristic markers, deliberately small and inspectable.
# ---------------------------------------------------------------------------

LAYER_MARKERS = {
    "L1": ["physical", "material", "hardware", "thermal", "voltage", "signal",
           "anatomy", "body", "machine", "metabolic", "propagation"],
    "L2": ["encoding", "representation", "neural", "embedding", "activation",
           "population code", "informational"],
    "L3": ["feels", "feel", "felt", "intuiti", "impression", "snap judg",
           "seems", "gut", "instinct", "unmotivated", "motivation", "morale"],
    "L4": ["procedure", "verified", "verify", "checked", "calculated",
           "a/b", "ab test", "tested", "process improved", "output declined",
           "productivity", "workflow", "operational", "executed the plan"],
    "L5": ["meeting", "negotiation", "agreed", "conversation", "discussion",
           "interview", "they said", "we agreed", "the team said", "spoke"],
    "L6": ["market", "stock", "institution", "regulat", "economy", "industry",
           "company's strateg", "the firm", "sales", "revenue", "valuation",
           "quarter", "earnings", "price", "the company", "shareholders"],
}

# Onto-modal markers for HNS-144
SUBJ_MARKERS = ["feel", "feels", "felt", "like", "likes", "liked", "prefer",
                "impression", "i think", "in my view", "seems", "popular",
                "everyone likes", "useful", "enjoyable"]
OBJ_MARKERS = ["measured", "data", "percent", "%", "accuracy", "metric",
               "observed", "recorded", "rose", "fell", "increased", "decreased",
               "test set", "statistically"]
NEC_MARKERS = ["must", "necessarily", "by definition", "always", "required",
               "axiom", "entails", "guarantee", "what matters", "the point is",
               "fundamentally", "inevitabl", "law of"]
CONT_MARKERS = ["this quarter", "happened", "could have", "might", "occurred",
                "this time", "on this", "currently", "today", "recently"]
NORMATIVE_MARKERS = ["good", "bad", "should", "ought", "right", "wrong",
                     "best", "better", "worse", "matters", "valuable"]

# Causal connectives (trigger for Unsupported Causality screen, O2 admissibility)
CAUSAL_CONNECTIVES = ["because", "due to", "thanks to", "as a result of",
                      "led to", "leads to", "caused", "causes", "resulted in",
                      "results in", "so that", "which is why", "the reason"]

# Evidence / mechanism markers that DISCHARGE an unsupported-causality flag
MECHANISM_MARKERS = ["a/b", "ab test", "tested", "measured", "+", "uplift",
                     "controlled", "mechanism", "data show", "evidence",
                     "experiment", "correlat", "regression", "percent", "%",
                     "study", "trial", "p <", "p<", "confidence interval",
                     # evidential sources that discharge a causal claim:
                     "survey", "surveys", "historical pattern", "documented",
                     "regression test", "confirm", "attributable"]
COINCIDENCE_MARKERS = ["coincid", "at the same time", "right after we",
                       "after we changed", "happened to", "by chance"]

# Combat / fire / physical-violence figuration (SMS-1 somatic contamination)
METAPHOR_MARKERS = ["fight", "fights", "fighting", "battle", "war ", "attack",
                    "crush", "crushing", "fire", "firefight", "weapon", "kill",
                    "destroy", "demolish", "smash", "conquer", "warpath",
                    "in the trenches", "bullet", "bombard", "nuke", "slay"]

# Scope-drift markers: opinion / recommendation injected where a bounded task
# (summarise/list/report/extract) was requested (SMS-2 declared intent, SMS-3 scope)
OPINION_MARKERS = ["i think", "i believe", "in my opinion", "in my view",
                   "should pivot", "i recommend", "my recommendation",
                   "we should", "the company should", "overall i think",
                   "personally", "if you ask me", "my advice"]
BOUNDED_TASK_MARKERS = ["summarize", "summarise", "list", "report the",
                        "what were the decisions", "extract", "transcribe",
                        "give me the", "what decisions"]

# Guardrail (safety/quality surface filter) lexicons — for the Guardrail arm
GUARDRAIL_SAFETY = ["kill", "weapon", "bomb", "suicide", "slur", "hate",
                    "nuke", "destroy them"]
GUARDRAIL_AGGRESSION = ["fight", "attack", "crush", "war ", "battle", "smash",
                        "conquer", "slay", "demolish"]


# ---------------------------------------------------------------------------
# 2. Small text utilities
# ---------------------------------------------------------------------------

def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?;])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]

def count_hits(text: str, markers: list[str]) -> list[str]:
    low = text.lower()
    return [m for m in markers if m in low]

def layer_of(sent: str) -> Optional[str]:
    """Assign the dominant Human Natural Layer to a sentence by marker count.
    Returns None if no marker is present (layer-neutral)."""
    low = sent.lower()
    scores = {lid: sum(low.count(m) for m in ms) for lid, ms in LAYER_MARKERS.items()}
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else None

def layer_index(lid: str) -> int:
    return int(lid[1])


# ---------------------------------------------------------------------------
# 3. Axis-2 structural detectors (operate on features, never on labels)
# ---------------------------------------------------------------------------

@dataclass
class DetectorResult:
    fired: bool
    failure_type: str
    axis: str
    coordinate: str
    evidence: str

def detect_layer_jump(prompt: str, text: str) -> DetectorResult:
    """HNS-36 / Axis 2. Fire when a single causal link joins two NON-ADJACENT
    layers (|dL| >= 2) with no sentence occupying an intermediate layer
    (no bridging proposition)."""
    sents = sentences(text)
    seq = [(s, layer_of(s)) for s in sents]
    layered = [(s, l) for (s, l) in seq if l]
    # find the widest causal gap inside a causal sentence
    worst = None
    for s, l in layered:
        if any(c in s.lower() for c in CAUSAL_CONNECTIVES):
            # layers mentioned within this one causal sentence
            low = s.lower()
            present = sorted({lid for lid, ms in LAYER_MARKERS.items()
                              if any(m in low for m in ms)}, key=layer_index)
            if len(present) >= 2:
                gap = layer_index(present[-1]) - layer_index(present[0])
                if gap >= 2:
                    worst = (present[0], present[-1], gap, s)
    if worst is None:
        # also check across adjacent causal sentences forming one chain
        cl = [l for _, l in layered]
        for i in range(len(cl) - 1):
            if cl[i] and cl[i + 1]:
                gap = abs(layer_index(cl[i + 1]) - layer_index(cl[i]))
                joined = layered[i][0] + " " + layered[i + 1][0]
                if gap >= 2 and any(c in joined.lower() for c in CAUSAL_CONNECTIVES):
                    a, b = sorted([cl[i], cl[i + 1]], key=layer_index)
                    worst = (a, b, gap, joined)
                    break
    if worst:
        a, b, gap, ev = worst
        # bridging check: is any intermediate layer occupied elsewhere?
        mids = {f"L{k}" for k in range(layer_index(a) + 1, layer_index(b))}
        occupied = {l for _, l in layered if l}
        bridged = bool(mids & occupied)
        if not bridged:
            return DetectorResult(
                True, "Layer Jump", "Axis2/HNS-36", f"{a}->{b}",
                f"causal link spans {a}({LAYERS[a]})->{b}({LAYERS[b]}), "
                f"gap={gap}, no bridging proposition at {sorted(mids)}; "
                f"trigger sentence: \"{ev[:90]}\"")
    return DetectorResult(False, "Layer Jump", "Axis2/HNS-36", "", "")

def detect_category_ambiguity(prompt: str, text: str) -> DetectorResult:
    """HNS-144 / Axis 2. Fire when one claim collapses conflicting quadrants:
    a subjective marker bound (by a necessity/normative connective) to an
    objective/necessary conclusion within the same sentence.

    Guard: a sentence that explicitly DIFFERENTIATES the registers (labels
    them, or says one 'depends on' / is 'not a definition' / 'distinct') is
    grounding, not collapsing — it does not fire."""
    DIFFERENTIATION = ["(subjective", "(objective", "depends on", "distinct",
                       "not a definition", "separately", "three questions",
                       "normative judgement", "normative choice"]
    for s in sentences(text):
        low = s.lower()
        if any(d in low for d in DIFFERENTIATION):
            continue  # registers are being separated, not conflated
        subj = count_hits(low, SUBJ_MARKERS)
        obj = count_hits(low, OBJ_MARKERS)
        nec = count_hits(low, NEC_MARKERS)
        norm = count_hits(low, NORMATIVE_MARKERS)
        # collapse signature: subjective evidence asserted as necessary/normative truth
        if subj and (nec or norm):
            q_from = "Q1(Subjective/Contingent)"
            q_to = "Q4(Objective/Necessary)" if nec else "normative(fact/value collapse)"
            return DetectorResult(
                True, "Category Ambiguity", "Axis2/HNS-144", "Q1->Q4",
                f"subjective marker {subj} asserted as {q_to} via {nec or norm}; "
                f"quadrants {q_from} and {q_to} collapsed in: \"{s[:90]}\"")
        # triple collapse: subjective + objective + normative in one sentence
        if subj and obj and norm:
            return DetectorResult(
                True, "Category Ambiguity", "Axis2/HNS-144", "Q1+Q3+norm",
                f"subjective {subj}, objective {obj}, normative {norm} fused in "
                f"one undifferentiated claim: \"{s[:90]}\"")
    return DetectorResult(False, "Category Ambiguity", "Axis2/HNS-144", "", "")

def detect_unsupported_causality(prompt: str, text: str) -> DetectorResult:
    """HNS-864 / Axis 2+3 (O2 admissibility). Fire when a causal connective
    links cause->effect but NO mechanism/evidence marker discharges it, or a
    coincidence is presented as a cause."""
    for s in sentences(text):
        low = s.lower()
        if any(c in low for c in CAUSAL_CONNECTIVES):
            mech = count_hits(low, MECHANISM_MARKERS)
            coinc = count_hits(low, COINCIDENCE_MARKERS)
            if coinc and not mech:
                return DetectorResult(
                    True, "Unsupported Causality", "Axis2+3/HNS-864", "O2:inadmissible",
                    f"coincidence {coinc} presented as cause, no admissible "
                    f"mechanism: \"{s[:90]}\"")
            if not mech:
                # causal claim with no measurement/test/mechanism anywhere in the sentence
                return DetectorResult(
                    True, "Unsupported Causality", "Axis2+3/HNS-864", "O2:inadmissible",
                    f"causal connective {[c for c in CAUSAL_CONNECTIVES if c in low]} "
                    f"with no mechanistic support: \"{s[:90]}\"")
    return DetectorResult(False, "Unsupported Causality", "Axis2+3/HNS-864", "", "")

def detect_scope_drift(prompt: str, text: str) -> DetectorResult:
    """SMS-2/3 / Axis 3. Fire when the prompt declares a bounded task
    (summarise/list/report/extract) but the output injects opinion or
    recommendation beyond that scope, without signalling."""
    p = prompt.lower()
    bounded = any(b in p for b in BOUNDED_TASK_MARKERS)
    if not bounded:
        return DetectorResult(False, "Scope Drift", "Axis3/SMS-2,3", "", "")
    for s in sentences(text):
        low = s.lower()
        op = count_hits(low, OPINION_MARKERS)
        # a signalled aside ("[beyond scope ...]") is NOT a drift
        signalled = "beyond" in low and ("scope" in low or "not decided" in low)
        if op and not signalled:
            return DetectorResult(
                True, "Scope Drift", "Axis3/SMS-2,3", "SMS-2:intent,SMS-3:scope",
                f"bounded task in prompt but unrequested opinion {op} injected: "
                f"\"{s[:90]}\"")
    return DetectorResult(False, "Scope Drift", "Axis3/SMS-2,3", "", "")

def detect_metaphor_contamination(prompt: str, text: str) -> DetectorResult:
    """SMS-1 / Axis 3. Fire when combat/fire/physical-violence figuration carries
    the operative content and no literal mechanism sentence is present."""
    low = text.lower()
    hits = count_hits(low, METAPHOR_MARKERS)
    if len(hits) >= 2:  # figurative density
        # is there any literal operational mechanism to anchor it?
        literal = count_hits(low, LAYER_MARKERS["L4"]) + count_hits(low, MECHANISM_MARKERS)
        if not literal:
            return DetectorResult(
                True, "Metaphor Contamination", "Axis3/SMS-1", "SMS-1:somatic",
                f"physical/combat figuration {hits} displaces literal coordinates; "
                f"no literal mechanism stated")
    return DetectorResult(False, "Metaphor Contamination", "Axis3/SMS-1", "", "")

ALL_DETECTORS = [
    detect_layer_jump,
    detect_category_ambiguity,
    detect_scope_drift,
    detect_metaphor_contamination,
    detect_unsupported_causality,
]

# ---------------------------------------------------------------------------
# 4. Axis-3 grounding margins g_i in [0,1]  (EXPLICIT functions of features)
#    s = min_i g_i  (Vol.4 Ch.10 conservative aggregate consumed by O6)
# ---------------------------------------------------------------------------

def grounding_margins(prompt: str, text: str) -> dict[str, float]:
    """Compute six per-layer grounding margins from observable features.
    Each margin starts at 1.0 and is reduced by an explicit, bounded penalty.
    NOTHING here reads a case id or an expected label."""
    low = text.lower()
    sents = sentences(text)

    # g1 Somatic: penalised by combat/physical-metaphor density (SMS-1)
    meta = len(count_hits(low, METAPHOR_MARKERS))
    g1 = max(0.0, 1.0 - 0.5 * meta)

    # g2 Protocol: penalised by violation of declared communicative intent (SMS-2)
    sd = detect_scope_drift(prompt, text)
    g2 = 0.0 if sd.fired else 1.0

    # g3 Organizational: penalised by over-scoped organisational recommendation
    org_over = count_hits(low, ["should pivot", "company should", "we should",
                                "restructure", "reorganise", "reorganize"])
    g3 = max(0.0, 1.0 - 0.5 * len(org_over))

    # g4 Economic: penalised by unbalanced/unsupported economic causal claims
    uc = detect_unsupported_causality(prompt, text)
    econ_terms = count_hits(low, ["sales", "revenue", "stock", "price",
                                  "market", "earnings", "valuation"])
    g4 = 0.4 if (uc.fired and econ_terms) else 1.0

    # g5 Governance: penalised by asserting norms/rules without basis
    norm = count_hits(low, NORMATIVE_MARKERS)
    subj = count_hits(low, SUBJ_MARKERS)
    g5 = 0.4 if (norm and subj and not count_hits(low, OBJ_MARKERS)) else 1.0

    # g6 Universal: penalised by logical incoherence (category collapse / contradiction)
    ca = detect_category_ambiguity(prompt, text)
    g6 = 0.3 if ca.fired else 1.0

    return {"SMS-1": round(g1, 3), "SMS-2": round(g2, 3), "SMS-3": round(g3, 3),
            "SMS-4": round(g4, 3), "SMS-5": round(g5, 3), "SMS-6": round(g6, 3)}

def composite_grounding(margins: dict[str, float]) -> tuple[float, int]:
    """Graded s = min_i g_i (Vol.4 Ch.10). Strict G = 1 iff all g_i == 1."""
    s = min(margins.values())
    G = 1 if all(v >= 0.999 for v in margins.values()) else 0
    return round(s, 3), G


# ---------------------------------------------------------------------------
# 5. EVA evaluation: run detectors + grounding, emit verdict + audit record
# ---------------------------------------------------------------------------

@dataclass
class AuditRecord:
    case_id: str
    prompt: str
    candidate: str
    intended_failure: str          # ground-truth label of the case (for scoring only)
    detectors: list = field(default_factory=list)
    margins: dict = field(default_factory=dict)
    s: float = 1.0
    G: int = 1
    axis2_violation: bool = False
    axis3_failure: bool = False
    verdict: str = "PASS"
    detected: bool = False
    correct_type: bool = False
    triggers: list = field(default_factory=list)

def evaluate(case_id: str, prompt: str, candidate: str,
             intended_failure: str) -> AuditRecord:
    fired = [d(prompt, candidate) for d in ALL_DETECTORS]
    fired = [f for f in fired if f.fired]

    margins = grounding_margins(prompt, candidate)
    s, G = composite_grounding(margins)

    axis2 = any(f.axis.startswith("Axis2") and "Axis3" not in f.axis for f in fired) \
        or any("HNS-36" in f.axis or "HNS-144" in f.axis or "HNS-864" in f.axis for f in fired)
    axis3 = any(v <= 0.0 for v in margins.values())

    # verdict per Vol.1 interception logic:
    #   grounding failure (a g_i == 0) -> BLOCKED ; structural violation -> ATTENUATED
    if any(v <= 0.0 for v in margins.values()):
        verdict = "BLOCKED"
    elif fired or s < 0.999:
        verdict = "ATTENUATED"
    else:
        verdict = "PASS"

    detected = bool(fired) or verdict != "PASS"
    types = {f.failure_type for f in fired}
    correct_type = intended_failure in types

    return AuditRecord(
        case_id=case_id, prompt=prompt, candidate=candidate,
        intended_failure=intended_failure,
        detectors=[asdict(f) for f in fired],
        margins=margins, s=s, G=G,
        axis2_violation=bool(axis2), axis3_failure=bool(axis3),
        verdict=verdict, detected=detected, correct_type=correct_type,
        triggers=[f"{f.failure_type}@{f.coordinate}" for f in fired],
    )


# ---------------------------------------------------------------------------
# 6. Baseline and Guardrail arms (for comparison)
# ---------------------------------------------------------------------------

def run_baseline(prompt: str, candidate: str) -> dict:
    """No verification. Emits the candidate verbatim. Detects nothing."""
    return {"mode": "baseline", "emitted": candidate, "detected": False,
            "log": None}

def run_guardrail(prompt: str, candidate: str) -> dict:
    """A generous surface guardrail: safety lexicon + aggression lexicon +
    crude off-topic heuristic. Catches some surface-marked outputs; blind to
    structural/causal/grounding failures by construction. No coordinate log."""
    low = candidate.lower()
    safety = count_hits(low, GUARDRAIL_SAFETY)
    aggression = count_hits(low, GUARDRAIL_AGGRESSION)
    # off-topic heuristic: bounded task but <10% keyword overlap with prompt nouns
    p_words = {w for w in re.findall(r"[a-z]{4,}", prompt.lower())}
    c_words = {w for w in re.findall(r"[a-z]{4,}", low)}
    overlap = len(p_words & c_words) / max(1, len(p_words))
    off_topic = overlap < 0.15 and len(c_words) > 8
    flagged = bool(safety) or len(aggression) >= 2 or off_topic
    reason = []
    if safety:
        reason.append(f"safety:{safety}")
    if len(aggression) >= 2:
        reason.append(f"aggression:{aggression}")
    if off_topic:
        reason.append(f"off_topic:overlap={overlap:.2f}")
    return {"mode": "guardrail", "flagged": flagged,
            "detected": flagged, "reason": reason, "log": None}
