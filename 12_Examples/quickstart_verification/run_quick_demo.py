import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
PKG_DIR = REPO_ROOT / "01-Docs" / "05-Implementations" / "hns36_pkg"
SCHEMA_PATH = REPO_ROOT / "01-Docs" / "06-Schemas" / "hns36-eva-verification.schema.json"
SAMPLE_PATH = Path(__file__).resolve().parent / "sample_trace.json"

if PKG_DIR.exists():
    sys.path.insert(0, str(PKG_DIR))


def fallback_structural_check(text: str) -> list[dict]:
    """Lightweight heuristic check when running offline without external LLM calls."""
    violations = []
    if "自動的にゼロ" in text or "必ず" in text:
        violations.append({
            "taxonomy_code": "UNSUPPORTED_CAUSALITY",
            "severity": "high",
            "detail": "Deterministic causal claim asserted without structural mechanism."
        })
    if "神経系" in text and "コンプライアンス" in text and "[Layer:" not in text:
        violations.append({
            "taxonomy_code": "LAYER_JUMP",
            "severity": "high",
            "detail": "Biological/physical layer directly equated with institutional/normative layer."
        })
    return violations


def validate_basic_schema(record: dict, schema: dict) -> list[str]:
    """Minimal dependency-free schema check for required keys and enum values."""
    errors = []
    for req in schema.get("required", []):
        if req not in record:
            errors.append(f"Missing required field: {req}")
    status = record.get("verification_result", {}).get("status")
    if status not in {"PASS", "WARN", "FAIL"}:
        errors.append(f"Invalid verification status: {status}")
    return errors


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    samples = json.loads(SAMPLE_PATH.read_text(encoding="utf-8"))

    records = []
    for idx, item in enumerate(samples, start=1):
        violations = fallback_structural_check(item["response"])
        for v in violations:
            v["turn_index"] = item["turn_index"]

        payload_bytes = json.dumps(item, ensure_ascii=False, sort_keys=True).encode("utf-8")
        digest = hashlib.sha256(payload_bytes).hexdigest()
        err_count = len(violations)

        record = {
            "schema_version": "1.0.0",
            "record_id": f"eva-demo-{idx:03d}",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "hns_spec_level": "HNS-36",
            "target_model": {
                "provider": "local-quickstart",
                "model_id": "demo-fixture-v1",
                "mode": item["mode"]
            },
            "coordinates": {
                "layer_index": 2,
                "layer_name": "Cognitive/Structural",
                "category_index": 1,
                "category_name": "Structure",
                "cell_id": "C1-L2"
            },
            "verification_result": {
                "status": "PASS" if err_count == 0 else "FAIL",
                "structural_error_count": err_count,
                "violations": violations
            },
            "eva_audit": {
                "non_invasive_blackbox": True,
                "independent_monitor": True,
                "hardware_root_profile": "SOFTWARE_SIMULATION",
                "payload_sha256": digest
            }
        }

        schema_errors = validate_basic_schema(record, schema)
        if schema_errors:
            raise ValueError(f"Schema validation failed for {record['record_id']}: {schema_errors}")

        records.append(record)

    print(json.dumps(records, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
