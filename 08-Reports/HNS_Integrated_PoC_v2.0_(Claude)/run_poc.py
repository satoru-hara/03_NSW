"""
run_poc.py — execute the Integrated PoC v2.0 experiment and emit artifacts.

Runs three arms over the 15 controlled cases:
  baseline  : no verification
  guardrail : surface safety/quality filter
  eva_hns   : full EVA-HNS structural + grounding evaluator (with audit log)

Also runs EVA-HNS over the HNS-CORRECTED outputs to produce the before/after
(structural clarity / grounding stability) comparison.

Outputs (to ./out):
  audit_logs.json        full machine-readable audit record per case (failing)
  audit_logs_jsonld.json the same in JSON-LD form (EVA Verifiability)
  results_summary.json   per-arm detection counts and the summary matrix
  before_after.json      EVA verdict on failing vs corrected outputs
  results_table.csv       flat per-case table
"""

import json, csv, os
from dataclasses import asdict
from eva_hns import (evaluate, run_baseline, run_guardrail, LAYERS, CATEGORIES,
                     QUADRANTS, SMS)
from cases import CASES

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)

def to_jsonld(rec) -> dict:
    """Render an audit record in the JSON-LD shape specified in Vol.1 5.4."""
    d2 = rec.detectors[0] if rec.detectors else None
    axis2_cells = [t for t in rec.triggers]
    return {
        "@context": "https://nsw.example/hns/v2",
        "@type": "EvaAuditRecord",
        "case_id": rec.case_id,
        "span": {"start": 0, "end": len(rec.candidate)},
        "axis2": {
            "triggers": axis2_cells,
            "structural_violation": rec.axis2_violation,
        },
        "axis3": {
            "margins": rec.margins,
            "s_min": rec.s,
            "G": rec.G,
            "grounding_failure": rec.axis3_failure,
        },
        "trigger": (d2["evidence"] if d2 else "none"),
        "verdict": rec.verdict,
        "action": ("token probability set to 0 (block)" if rec.verdict == "BLOCKED"
                   else "candidate scaled by g(s) (attenuate)" if rec.verdict == "ATTENUATED"
                   else "emit"),
    }

def main():
    audit_records, jsonld_records, rows = [], [], []
    arm_counts = {"baseline": 0, "guardrail": 0, "eva_hns": 0}
    eva_correct_type = 0
    logged = 0

    for c in CASES:
        # arm 1: baseline
        b = run_baseline(c["prompt"], c["failing"])
        # arm 2: guardrail
        g = run_guardrail(c["prompt"], c["failing"])
        # arm 3: EVA-HNS
        rec = evaluate(c["id"], c["prompt"], c["failing"], c["failure_type"])

        arm_counts["baseline"] += int(b["detected"])
        arm_counts["guardrail"] += int(g["detected"])
        arm_counts["eva_hns"] += int(rec.detected)
        eva_correct_type += int(rec.correct_type)
        logged += 1  # EVA emits a record for every case (auditability)

        audit_records.append(asdict(rec))
        jsonld_records.append(to_jsonld(rec))

        rows.append({
            "case_id": c["id"],
            "intended_failure": c["failure_type"],
            "baseline_detected": b["detected"],
            "guardrail_detected": g["detected"],
            "guardrail_reason": ";".join(g["reason"]),
            "eva_detected": rec.detected,
            "eva_types": ";".join(sorted({t.split("@")[0] for t in rec.triggers})),
            "correct_type": rec.correct_type,
            "s_min": rec.s, "G": rec.G, "verdict": rec.verdict,
        })

    # before/after on corrected outputs
    before_after = []
    corrected_pass = 0
    for c in CASES:
        rec_fail = evaluate(c["id"], c["prompt"], c["failing"], c["failure_type"])
        rec_corr = evaluate(c["id"] + "-corrected", c["prompt"], c["corrected"],
                            c["failure_type"])
        corrected_pass += int(rec_corr.verdict == "PASS")
        before_after.append({
            "case_id": c["id"],
            "failure_type": c["failure_type"],
            "before_verdict": rec_fail.verdict, "before_s": rec_fail.s,
            "before_triggers": rec_fail.triggers,
            "after_verdict": rec_corr.verdict, "after_s": rec_corr.s,
            "after_triggers": rec_corr.triggers,
        })

    n = len(CASES)
    summary = {
        "n_cases": n,
        "arm_detection_counts": arm_counts,
        "eva_correct_type_count": eva_correct_type,
        "eva_logged_count": logged,
        "corrected_pass_count": corrected_pass,
        "summary_matrix": {
            "baseline":  {"detected": arm_counts["baseline"], "undetected": n - arm_counts["baseline"]},
            "guardrail": {"detected": arm_counts["guardrail"], "unresolved": n - arm_counts["guardrail"]},
            "eva_hns":   {"detected": arm_counts["eva_hns"], "logged": logged,
                          "correct_type": eva_correct_type},
        },
        "coordinate_scheme": {"layers": LAYERS, "categories": CATEGORIES,
                              "quadrants": QUADRANTS, "sms": SMS},
    }

    with open(os.path.join(OUT, "audit_logs.json"), "w") as f:
        json.dump(audit_records, f, indent=2)
    with open(os.path.join(OUT, "audit_logs_jsonld.json"), "w") as f:
        json.dump(jsonld_records, f, indent=2)
    with open(os.path.join(OUT, "results_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    with open(os.path.join(OUT, "before_after.json"), "w") as f:
        json.dump(before_after, f, indent=2)
    with open(os.path.join(OUT, "results_table.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    # console report
    print("=" * 64)
    print("INTEGRATED PoC v2.0 — EXECUTION RESULTS")
    print("=" * 64)
    print(f"cases: {n}")
    print(f"baseline  detected: {arm_counts['baseline']}/{n}")
    print(f"guardrail detected: {arm_counts['guardrail']}/{n}  "
          f"(unresolved {n - arm_counts['guardrail']}/{n})")
    print(f"eva_hns   detected: {arm_counts['eva_hns']}/{n}  "
          f"correct-type {eva_correct_type}/{n}  logged {logged}/{n}")
    print(f"corrected outputs PASS: {corrected_pass}/{n}")
    print("-" * 64)
    for r in rows:
        print(f"{r['case_id']:>14} | {r['intended_failure']:<22} | "
              f"base {int(r['baseline_detected'])} grd {int(r['guardrail_detected'])} "
              f"eva {int(r['eva_detected'])} type {int(r['correct_type'])} | "
              f"s={r['s_min']:<5} {r['verdict']}")
    print("=" * 64)

if __name__ == "__main__":
    main()
