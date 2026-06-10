# Post-Hoc EVA Auditor Pseudocode

```text
input: emitted_ai_output

segments = split_output_into_claims(emitted_ai_output)

for each segment:
    hns36 = assign_hns36_coordinate(segment)
    hns144 = assign_onto_modal_quadrant(segment)
    hns864 = identify_inference_or_control_operator(segment)
    sms6 = check_grounding_layer(segment)
    failure_type = classify_structural_failure(segment)
    verdict = determine_eva_verdict(hns36, hns144, hns864, sms6, failure_type)
    emit_audit_record(segment, hns36, hns144, hns864, sms6, failure_type, verdict)

return audit_records
```
