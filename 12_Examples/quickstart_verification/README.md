# Quickstart Verification Demo (HNS-36 / EVA)

This demo lets external reviewers and standardization evaluators verify the **HNS-36 / EVA** JSON Schema structure and inspect sample structural hallucination detections **without requiring external API keys**.

## Run

```bash
python examples/quickstart_verification/run_quick_demo.py
```

## What It Demonstrates
1. **Structural Violation Detection:** Compares an unconstrained response (`LAYER_JUMP` / `UNSUPPORTED_CAUSALITY`) against an HNS-36 coordinate-annotated response (`PASS`).
2. **EVA Audit Metadata:** Attaches a SHA-256 payload digest and explicit `SOFTWARE_SIMULATION` hardware-root profile (`TPM` / `FPGA` / `ASIC` in production/hardware deployments).
3. **Schema Conformance:** Validates generated records against `01-Docs/06-Schemas/hns36-eva-verification.schema.json`.
