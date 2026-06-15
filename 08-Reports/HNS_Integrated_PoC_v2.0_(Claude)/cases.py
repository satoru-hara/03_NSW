"""
cases.py — 15 controlled test cases for the Integrated PoC v2.0.

Three cases per failure type. Each case has:
  id, failure_type, prompt, failing (candidate), corrected (HNS-corrected output).

Cases LJ-1, CA-1, SD-1, MC-1, UC-1 reproduce the canonical worked examples
from the HNS series (Vol.1 Appendix A); the remaining two per type are
additional controlled prompts in the same style. The cases were authored to
EXHIBIT their target failure; see Limitations on what that does and does not
license about detection performance.
"""

CASES = [
    # ---------------- Layer Jump (Axis 2 / HNS-36) ----------------
    {
        "id": "LJ-1", "failure_type": "Layer Jump",
        "prompt": "Why did the company's stock fall?",
        "failing": "The stock fell because the employees were unmotivated.",
        "corrected": ("The stock fell on weak quarterly earnings. Earnings were "
                      "weak partly because operational output declined, which "
                      "internal surveys link to reduced motivation. The bridge "
                      "runs motivation to productivity to earnings to valuation."),
    },
    {
        "id": "LJ-2", "failure_type": "Layer Jump",
        "prompt": "Why are revenues down this year?",
        "failing": "Revenue is down because the team's morale is low.",
        "corrected": ("Revenue fell 9%. Lower morale reduced operational output "
                      "(measured throughput dropped 11%); reduced output cut "
                      "deliveries, which cut billed revenue. The bridge from "
                      "morale to revenue runs through operational throughput."),
    },
    {
        "id": "LJ-3", "failure_type": "Layer Jump",
        "prompt": "Why did the market price rise?",
        "failing": "The market price rose because a manager felt optimistic.",
        "corrected": ("The price rose 4%. A manager's optimism informed a guidance "
                      "update (communicative act); the upgraded guidance changed "
                      "analyst forecasts; revised forecasts moved the market price. "
                      "Each step bridges one layer to the next."),
    },
    # ---------------- Category Ambiguity (Axis 2 / HNS-144) ----------------
    {
        "id": "CA-1", "failure_type": "Category Ambiguity",
        "prompt": "Is the new policy good?",
        "failing": "Yes, it's good because everyone likes it and that's what matters.",
        "corrected": ("Three distinct questions. Is it liked? Survey data say yes "
                      "(subjective). Does it achieve its stated goal? Early metrics "
                      "are mixed (objective). Is it good overall? That is a "
                      "normative judgement depending on which values are weighted."),
    },
    {
        "id": "CA-2", "failure_type": "Category Ambiguity",
        "prompt": "Was the meeting productive?",
        "failing": "Yes, it felt productive and that is necessarily what counts.",
        "corrected": ("Subjectively, participants reported it felt productive "
                      "(subjective, contingent). Objectively, two of three agenda "
                      "items were decided (objective, contingent). Whether that "
                      "counts as productive depends on the standard applied."),
    },
    {
        "id": "CA-3", "failure_type": "Category Ambiguity",
        "prompt": "Is this design the best choice?",
        "failing": "It is the best because users like it, so by definition it wins.",
        "corrected": ("Users prefer it in testing (subjective). On measured task "
                      "time it is 12% faster (objective). Whether it is best "
                      "depends on the weighting of preference, speed, and cost; "
                      "that weighting is a normative choice, not a definition."),
    },
    # ---------------- Scope Drift (Axis 3 / SMS-2,3) ----------------
    {
        "id": "SD-1", "failure_type": "Scope Drift",
        "prompt": "Summarize the decisions made in the meeting.",
        "failing": ("The budget was approved and hiring deferred. Overall I think "
                    "the company should pivot toward enterprise sales next year."),
        "corrected": ("Decisions: approved the Q3 budget; deferred the hiring "
                      "freeze; assigned the audit to Team B. [Beyond the meeting's "
                      "scope, and not decided there: a strategy pivot was mentioned "
                      "but tabled.]"),
    },
    {
        "id": "SD-2", "failure_type": "Scope Drift",
        "prompt": "List the action items from the call.",
        "failing": ("Action items: send the report, book the venue. In my opinion "
                    "we should also restructure the whole onboarding flow."),
        "corrected": ("Action items: send the report by Friday; book the venue. "
                      "[Not an action item from the call: a suggestion to revisit "
                      "onboarding was raised but not assigned.]"),
    },
    {
        "id": "SD-3", "failure_type": "Scope Drift",
        "prompt": "Summarize what the customer reported in the ticket.",
        "failing": ("The customer reported a login error after the update. "
                    "Personally I believe we should rebuild the auth service."),
        "corrected": ("The customer reported a login error appearing after the "
                      "latest update, affecting password reset. [Outside the "
                      "ticket's content: any remediation plan is not stated by "
                      "the customer.]"),
    },
    # ---------------- Metaphor Contamination (Axis 3 / SMS-1) ----------------
    {
        "id": "MC-1", "failure_type": "Metaphor Contamination",
        "prompt": "How should the team handle the deadline?",
        "failing": "Fight the fire, attack the problem head-on, and crush the deadline.",
        "corrected": ("Prioritise the two blocking tasks, reallocate one engineer "
                      "from the lower-priority feature, set daily checkpoints, and "
                      "cut scope on the optional module."),
    },
    {
        "id": "MC-2", "failure_type": "Metaphor Contamination",
        "prompt": "What is our plan for the product launch?",
        "failing": "We go to war on the market, smash the competition, and conquer.",
        "corrected": ("Ship the beta to 500 users on the 3rd, collect activation "
                      "metrics for two weeks, fix the top three drop-off points, "
                      "then open general availability."),
    },
    {
        "id": "MC-3", "failure_type": "Metaphor Contamination",
        "prompt": "How do we recover the delayed project?",
        "failing": "Bombard the backlog, slay every blocker, and demolish the timeline.",
        "corrected": ("Re-baseline the schedule, move two non-critical features to "
                      "the next release, add one reviewer to the critical path, and "
                      "track burndown daily."),
    },
    # ---------------- Unsupported Causality (Axis 2+3 / HNS-864) ----------------
    {
        "id": "UC-1", "failure_type": "Unsupported Causality",
        "prompt": "Why are sales up this quarter?",
        "failing": "Sales are up because we changed the logo.",
        "corrected": ("Sales rose 12%. The spring promotion was A/B-tested and "
                      "measured a +8% uplift; seasonal demand follows the "
                      "historical pattern; the rebrand coincided with no measured "
                      "effect. Only the promotion has a supported causal link."),
    },
    {
        "id": "UC-2", "failure_type": "Unsupported Causality",
        "prompt": "Why did user retention improve?",
        "failing": "Retention improved because we moved the office to a new building.",
        "corrected": ("Retention rose 5 points. The onboarding redesign was "
                      "A/B-tested with a measured +4 point lift; the office move "
                      "coincided with no measured effect on the cohort. The "
                      "redesign is the supported cause."),
    },
    {
        "id": "UC-3", "failure_type": "Unsupported Causality",
        "prompt": "Why did the server crash rate drop?",
        "failing": "Crashes dropped because we repainted the data centre.",
        "corrected": ("Crash rate fell 60%. A memory-leak fix shipped that week "
                      "and the regression test confirms the leak is gone; the "
                      "repainting happened to coincide but has no mechanism. The "
                      "leak fix is the admissible cause."),
    },
]
