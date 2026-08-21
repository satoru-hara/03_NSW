# 🛠️ Human Natural Structure (HNS) — Pre-Decode Interception Concept Demo

> **Status:** Non-normative concept demo / PoC scaffold  
> **Purpose:** Demonstrate the control flow of an HNS-inspired pre-decode interception layer and an EVA-style external audit log.  
> **Important:** This file does **not** implement the complete HNS-36 / HNS-144 / HNS-864 matrices, SMS-6 grounding, or production EVA. It uses a deliberately small mock structural rule so that the interception mechanism can be inspected and executed safely.

## What this demo shows

This sandbox illustrates the following architecture:

```text
Base language model
        ↓
next-token logits
        ↓
external structural admissibility check
        ↓
pre-decode attenuation / blocking
        ↓
token selection
        ↓
external EVA-style audit record
```

The demonstration is intended to make one engineering idea concrete:

> A verifier can inspect candidate tokens **before decoding**, reduce the probability of candidates that violate an external structural rule, and record the intervention in a machine-readable audit trail.

This is an **illustrative implementation pattern**, not evidence that HNS eliminates Layer Jump errors, hallucinations, or unsupported causality in general.

---

## What you should observe

1. **Baseline run:** generation proceeds using the base model without structural intervention.
2. **Intercept run:** a small mock rule checks high-probability candidate tokens before selection.
3. **Attenuation:** candidates rejected by the mock rule receive a mathematically correct logit penalty equivalent to multiplying their relative probability weight by a chosen factor.
4. **Audit log:** each intervention is recorded as JSON-LD using an explicit EVA demonstration namespace and W3C PROV terms.
5. **Optional synthetic self-test:** verifies that the attenuation operator actually lowers the target token probability.

Because this is a real language model rather than a scripted output generator, a particular prompt may produce **zero interventions**. That is a valid result. The demo does not fabricate a structural violation simply to make the output look different.

---

## Python implementation

The script below is designed for Google Colab or a local Python environment with `torch` and `transformers`.

```python
# ==============================================================================
# HNS Pre-Decode Interception Concept Demo
# (C) 2026 Satoru Hara / Natural Structure Works (NSW)
#
# Non-normative demonstration scaffold.
# This does NOT implement the complete HNS-36/144/864, SMS-6, or production EVA.
# Use is subject to the applicable HNS Dual License terms.
# ==============================================================================

import json
import math
from datetime import datetime, timezone

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# ------------------------------------------------------------------------------
# 1. Model setup
# ------------------------------------------------------------------------------

MODEL_ID = "distilgpt2"

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID).to(device)
model.eval()

if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token

prompt = "Why did the company's stock fall?"
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# ------------------------------------------------------------------------------
# 2. Minimal mock structural rule
# ------------------------------------------------------------------------------

# IMPORTANT:
# This is a toy rule used only to demonstrate the interception mechanism.
# It is NOT the complete HNS-36 matrix and does not claim to perform genuine
# HNS-36 structural classification.

MOCK_DISALLOWED_TERMS = {
    "lazy",
    "sad",
    "angry",
    "unmotivated",
}

def normalize_candidate(text: str) -> str:
    return text.strip().lower()

def check_structural_admissibility_mock(token_id: int):
    """
    Illustrative rule:
    reject a small set of candidate token strings representing an
    unbridged move from a macro/market explanation toward an unsupported
    individual-psychological explanation.
    """
    token_text = tokenizer.decode([token_id])
    normalized = normalize_candidate(token_text)

    if normalized in MOCK_DISALLOWED_TERMS:
        return (
            False,
            "Illustrative unbridged macro-to-psychological transition.",
            token_text,
        )

    return True, "No mock-rule violation.", token_text

# ------------------------------------------------------------------------------
# 3. Mathematically correct logit attenuation
# ------------------------------------------------------------------------------

def attenuate_logit_(logits, token_id: int, probability_factor: float = 0.01):
    """
    Reduces the token's relative softmax weight by `probability_factor`.

    Since softmax uses exp(logit), multiplying relative weight by alpha
    corresponds to adding log(alpha) to that token's logit.
    """
    if not (0.0 < probability_factor <= 1.0):
        raise ValueError("probability_factor must be in (0, 1].")

    logits[0, token_id] += math.log(probability_factor)

# ------------------------------------------------------------------------------
# 4. EVA-style JSON-LD audit record
# ------------------------------------------------------------------------------

JSONLD_CONTEXT = {
    "prov": "http://www.w3.org/ns/prov#",
    "eva": "https://example.org/hns/eva-demo#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}

def make_audit_record(
    step,
    token_id,
    token_text,
    reason,
    probability_before,
    probability_after,
    attenuation_factor,
):
    """
    Illustrative EVA-style audit record.

    The `eva:` vocabulary below is a demonstration namespace, not an official
    standardized HNS/EVA ontology.
    """
    return {
        "@context": JSONLD_CONTEXT,
        "@type": "prov:Entity",
        "eva:recordType": "PreDecodeInterventionDemo",
        "eva:timestamp": datetime.now(timezone.utc).isoformat(),
        "eva:step": step,
        "eva:candidateTokenId": token_id,
        "eva:candidateTokenText": token_text,
        "eva:configuration": "Illustrative HNS-inspired mock rule",
        "eva:flag": "MockStructuralViolation",
        "eva:trigger": reason,
        "eva:attenuationFactor": attenuation_factor,
        "eva:probabilityBefore": probability_before,
        "eva:probabilityAfter": probability_after,
        "prov:wasGeneratedBy": {
            "@id": "eva:sidecarConceptDemo",
            "@type": "prov:Activity",
        },
    }

# ------------------------------------------------------------------------------
# 5. Pre-decode interception loop
# ------------------------------------------------------------------------------

def generate_with_interceptor(
    model,
    inputs,
    use_interceptor=True,
    max_new_tokens=40,
    top_k_to_check=50,
    attenuation_factor=0.01,
):
    generated = inputs["input_ids"]
    log_records = []

    for step in range(max_new_tokens):
        with torch.no_grad():
            outputs = model(input_ids=generated)
            logits = outputs.logits[:, -1, :].clone()

        if use_interceptor:
            probs_before = torch.softmax(logits, dim=-1)
            _, top_k_ids = torch.topk(
                probs_before,
                k=min(top_k_to_check, logits.shape[-1]),
                dim=-1,
            )

            # top_k_ids shape is [batch, k]; this demo assumes batch size = 1.
            for idx in top_k_ids[0]:
                token_id = int(idx.item())

                is_valid, reason, token_text = (
                    check_structural_admissibility_mock(token_id)
                )

                if not is_valid:
                    p_before = float(probs_before[0, token_id].item())

                    attenuate_logit_(
                        logits,
                        token_id,
                        probability_factor=attenuation_factor,
                    )

                    probs_after = torch.softmax(logits, dim=-1)
                    p_after = float(probs_after[0, token_id].item())

                    log_records.append(
                        make_audit_record(
                            step=step,
                            token_id=token_id,
                            token_text=token_text,
                            reason=reason,
                            probability_before=p_before,
                            probability_after=p_after,
                            attenuation_factor=attenuation_factor,
                        )
                    )

        # Greedy decoding keeps the comparison deterministic.
        next_token = torch.argmax(logits, dim=-1, keepdim=True)
        generated = torch.cat((generated, next_token), dim=-1)

        if tokenizer.eos_token_id is not None:
            if int(next_token.item()) == tokenizer.eos_token_id:
                break

    return tokenizer.decode(generated[0], skip_special_tokens=True), log_records

# ------------------------------------------------------------------------------
# 6. Synthetic attenuation self-test
# ------------------------------------------------------------------------------

def attenuation_self_test():
    """Verify independently that the attenuation operator lowers probability."""
    test_logits = torch.tensor([[2.0, 1.0, -2.0]], dtype=torch.float32)

    before = torch.softmax(test_logits, dim=-1)[0, 0].item()

    modified = test_logits.clone()
    attenuate_logit_(modified, token_id=0, probability_factor=0.01)

    after = torch.softmax(modified, dim=-1)[0, 0].item()

    print("=== [SELF-TEST] LOGIT ATTENUATION ===")
    print(f"Target probability before: {before:.6f}")
    print(f"Target probability after : {after:.6f}")
    print(f"Probability reduced      : {after < before}")
    print()

# ------------------------------------------------------------------------------
# 7. Execute comparison
# ------------------------------------------------------------------------------

attenuation_self_test()

print("=== [TEST 1] BASELINE RUN (INTERCEPTOR DISABLED) ===")
baseline_output, _ = generate_with_interceptor(
    model,
    inputs,
    use_interceptor=False,
)
print(baseline_output)
print()

print("=== [TEST 2] HNS-INSPIRED INTERCEPT RUN ===")
intercept_output, logs = generate_with_interceptor(
    model,
    inputs,
    use_interceptor=True,
)
print(intercept_output)
print()

print("=== [TEST 3] EVA-STYLE JSON-LD AUDIT LOG ===")
print(json.dumps(logs, indent=2, ensure_ascii=False))

if not logs:
    print(
        "\nNOTE: No mock-rule violation appeared among the checked candidate "
        "tokens in this run. This is a valid result and does not indicate "
        "that the interceptor failed."
    )
```

---

## Why the attenuation is implemented this way

A softmax probability is derived from:

\[
p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}
\]

If the intended intervention is to reduce a candidate's **relative probability weight** by a factor \(\alpha\), the correct logit operation is:

\[
z_i' = z_i + \log(\alpha)
\]

because:

\[
e^{z_i + \log(\alpha)} = \alpha e^{z_i}
\]

For example, with:

```python
attenuation_factor = 0.01
```

the selected candidate receives a relative softmax-weight penalty of approximately 100× before renormalization.

This is preferable to:

```python
logits[token_id] *= 0.01
```

because multiplying a negative logit by `0.01` can move it **toward zero** and accidentally make the token *more* likely.

For a hard block rather than soft attenuation, a production implementation could instead assign:

```python
logits[0, token_id] = -float("inf")
```

subject to explicit safety and fallback rules.

---

## Relationship to HNS

This demo represents only the **control-flow pattern** of a future HNS runtime.

A fuller implementation would replace:

```python
check_structural_admissibility_mock(...)
```

with externally defined evaluators derived from the canonical HNS specifications, potentially including:

- HNS-36 structural coordinates
- HNS-144 observational distinctions
- HNS-864 analytical / causal operators
- SMS-6 contextual grounding
- policy-defined intervention thresholds
- EVA provenance and conformance records
- ECS escalation, blocking, or human-override logic

The verifier should remain logically separable from the base model so that the model is not the sole authority judging its own output.

---

## What this demo does **not** establish

This sandbox does not establish that:

- Layer Jump errors are reduced to 0%
- hallucinations are eliminated
- HNS guarantees factual truth
- HNS guarantees legal or regulatory compliance
- the mock rule is equivalent to HNS-36
- the audit schema is an official W3C or standards-body HNS ontology
- a production pre-decode HNS runtime meets latency, robustness, or security requirements

Those questions require independent empirical testing and a complete implementation of the relevant HNS specifications.

---

## Recommended next PoC

The natural next step is to replace the lexical mock with a **small explicit structural transition table**.

For example:

```text
current structural state
        ↓
candidate proposition / token span
        ↓
HNS layer + category assignment
        ↓
allowed / bridged / unsupported transition
        ↓
attenuate, block, or allow
        ↓
EVA record
```

That would move this project from a **concept demonstration** toward an **HNS-aware PoC**, while still remaining smaller and easier to audit than a complete HNS-864 runtime.

---

## Suggested status labels

For GitHub, the safest labels for this file are:

- **Concept Demo**
- **Non-Normative**
- **HNS-Inspired Pre-Decode Interception**
- **PoC Scaffold**
- **Not a Complete HNS Runtime**

These labels preserve the value of the demonstration without overstating what the current code proves.
