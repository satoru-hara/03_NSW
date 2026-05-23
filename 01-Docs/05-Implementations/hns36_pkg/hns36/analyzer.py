"""
HNS-36 Structural Analyzer
Detects structural errors and assigns coordinates using the Anthropic API.
"""

import json
import os
from typing import Optional

from .core import (
    StructuralAnalysis, StructuralError, ComparisonResult,
    HNSCoordinate, ERROR_TYPES
)
from .prompt import (
    get_constraint_prompt, get_evaluator_prompt, get_coordinate_prompt
)


def _get_client():
    """Get Anthropic client."""
    try:
        from anthropic import Anthropic
        return Anthropic()
    except ImportError:
        raise ImportError(
            "anthropic package required. Install with: pip install anthropic"
        )


def _call_api(client, system: str, user: str, model: str = "claude-sonnet-4-20250514") -> str:
    """Make a single API call and return the text response."""
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    return response.content[0].text


def _parse_json_response(text: str) -> dict:
    """Parse JSON from API response, stripping any markdown fences."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text.strip())


def analyze(
    text: str,
    question: Optional[str] = None,
    model: str = "claude-sonnet-4-20250514",
) -> StructuralAnalysis:
    """
    Analyze a text passage for HNS-36 structural errors.

    Args:
        text: The text to analyze (AI response or any passage)
        question: Optional — the question the text was answering (improves accuracy)
        model: Anthropic model to use

    Returns:
        StructuralAnalysis with detected errors and scores

    Example:
        >>> result = hns36.analyze(
        ...     "The dopamine system causes exhaustion because it keeps the brain aroused.",
        ...     question="Why do people feel tired after using social media?"
        ... )
        >>> print(result.total_errors)  # 2
        >>> print(result.error_types)   # ['UnsupportedCausality', 'MetaphorContamination']
    """
    client = _get_client()

    user_content = f"Analyze this response for HNS-36 structural errors:\n\n"
    if question:
        user_content += f"Question: {question}\n\n"
    user_content += f"Response:\n{text}"

    raw = _call_api(client, get_evaluator_prompt(), user_content, model)

    try:
        data = _parse_json_response(raw)
    except json.JSONDecodeError:
        # Fallback: return empty analysis
        return StructuralAnalysis(
            text=text,
            notes=f"Parse error in API response: {raw[:200]}"
        )

    errors = []
    for etype in ERROR_TYPES:
        err_data = data.get("errors", {}).get(etype, {})
        errors.append(StructuralError(
            error_type=etype,
            detected=err_data.get("detected", False),
            note=err_data.get("note", ""),
        ))

    return StructuralAnalysis(
        text=text,
        errors=errors,
        intention_alignment=data.get("intention_alignment"),
        structural_stability=data.get("structural_stability"),
        layer_activations=data.get("layer_activations", []),
        notes=data.get("notes", ""),
    )


def constrain(
    question: str,
    context: Optional[str] = None,
    mode: str = "full",
    model: str = "claude-sonnet-4-20250514",
) -> str:
    """
    Generate an HNS-36 constrained response to a question.
    
    Uses the HNS-36 structural constraint prompt to produce a response
    that explicitly names layers and states bridge mechanisms.

    Args:
        question: The question to answer
        context: Optional conversation context
        mode: "full" (detailed constraints) or "compact"
        model: Anthropic model to use

    Returns:
        Structurally constrained response string

    Example:
        >>> response = hns36.constrain(
        ...     "Why do people feel exhausted by digital interfaces?"
        ... )
        >>> print(response)
        # [Addressing L2 CognitiveOS → L3 InteractionOS → L5 LoadOS]
        # At L2 CognitiveOS: ...
    """
    client = _get_client()

    user_content = question
    if context:
        user_content = f"Context: {context}\n\nQuestion: {question}"

    return _call_api(client, get_constraint_prompt(mode), user_content, model)


def compare(
    question: str,
    response_a: str,
    response_b: str,
    label_a: Optional[str] = None,
    label_b: Optional[str] = None,
    model: str = "claude-sonnet-4-20250514",
) -> ComparisonResult:
    """
    Compare two responses using HNS-36 structural evaluation.
    
    Replicates the blind evaluation protocol from the HNS-36 PoC experiment.

    Args:
        question: The question both responses are answering
        response_a: First response (blind)
        response_b: Second response (blind)
        label_a: Optional label revealed after evaluation (e.g. "Standard")
        label_b: Optional label revealed after evaluation (e.g. "HNS-36")
        model: Anthropic model to use

    Returns:
        ComparisonResult with analysis for both responses

    Example:
        >>> result = hns36.compare(
        ...     question="Why does burnout occur?",
        ...     response_a=standard_response,
        ...     response_b=hns_response,
        ...     label_a="Standard",
        ...     label_b="HNS-36",
        ... )
        >>> print(result.summary())
    """
    analysis_a = analyze(response_a, question=question, model=model)
    analysis_b = analyze(response_b, question=question, model=model)

    return ComparisonResult(
        question=question,
        analysis_a=analysis_a,
        analysis_b=analysis_b,
        label_a=label_a,
        label_b=label_b,
    )


def coordinate(
    text: str,
    model: str = "claude-sonnet-4-20250514",
) -> HNSCoordinate:
    """
    Assign HNS-36 coordinates to a text passage.

    Args:
        text: Text passage to position in the HNS coordinate space
        model: Anthropic model to use

    Returns:
        HNSCoordinate with primary layer and category

    Example:
        >>> coord = hns36.coordinate("The stress response activates cortisol release.")
        >>> print(coord)  # L1×C2 (PhysicalOS × Core)
    """
    client = _get_client()

    user_content = f"Assign HNS-36 coordinates to this passage:\n\n{text}"
    raw = _call_api(client, get_coordinate_prompt(), user_content, model)

    try:
        data = _parse_json_response(raw)
        layer = data.get("primary_layer", "L1")
        category = data.get("primary_category", "C2")
        return HNSCoordinate(layer=layer, category=category)
    except (json.JSONDecodeError, KeyError):
        return HNSCoordinate(layer="L1", category="C2")


def batch_analyze(
    items: list[dict],
    model: str = "claude-sonnet-4-20250514",
) -> list[StructuralAnalysis]:
    """
    Analyze multiple text passages.

    Args:
        items: List of dicts with 'text' and optional 'question' keys
        model: Anthropic model to use

    Returns:
        List of StructuralAnalysis results

    Example:
        >>> results = hns36.batch_analyze([
        ...     {"text": response1, "question": "Why does burnout occur?"},
        ...     {"text": response2, "question": "What is decision fatigue?"},
        ... ])
    """
    return [
        analyze(item["text"], question=item.get("question"), model=model)
        for item in items
    ]
