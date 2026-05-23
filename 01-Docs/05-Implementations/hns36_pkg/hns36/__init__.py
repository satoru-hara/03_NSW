"""
HNS-36: Human Natural Structure — Structural Coordinate System for AI
======================================================================

The world's first structural OS kernel for human-aligned AI.

Quick start:
    import hns36

    # Detect structural errors in an AI response
    result = hns36.analyze(
        text="The dopamine system causes exhaustion.",
        question="Why do people feel tired?"
    )
    print(result.total_errors)       # 2
    print(result.error_types)        # ['UnsupportedCausality', 'MetaphorContamination']
    print(result.structural_stability)  # 3.0

    # Generate an HNS-36 constrained response
    response = hns36.constrain("Why does workplace burnout occur?")
    print(response)  # [Addressing L4 EnvironmentOS → L5 LoadOS → L3 InteractionOS] ...

    # Compare two responses (blind evaluation protocol)
    result = hns36.compare(
        question="Is this a personal or societal problem?",
        response_a=standard_response,
        response_b=hns_constrained_response,
    )
    print(result.summary())

    # Assign HNS-36 coordinates to a passage
    coord = hns36.coordinate("Cultural norms shape individual behavior over generations.")
    print(coord)  # L6×C1 (PatternOS × Civilization)

References:
    Hara, S. (2026). Human Natural Structure (HNS). SSRN. https://doi.org/10.2139/ssrn.6439661
    GitHub: https://github.com/satoru-hara/03_NSW
"""

__version__ = "1.0.0"
__author__  = "Satoru Hara"
__email__   = "satoru.hara@nifty.com"
__license__ = "CC BY 4.0"

from .core import (
    LAYERS,
    CATEGORIES,
    ERROR_TYPES,
    HNSCoordinate,
    StructuralError,
    StructuralAnalysis,
    ComparisonResult,
    get_cell,
    all_cells,
    layer_info,
    category_info,
)

from .analyzer import (
    analyze,
    constrain,
    compare,
    coordinate,
    batch_analyze,
)

from .prompt import (
    get_constraint_prompt,
    get_evaluator_prompt,
    build_layer_reference,
    build_category_reference,
    build_error_reference,
)

__all__ = [
    # Core data
    "LAYERS",
    "CATEGORIES",
    "ERROR_TYPES",
    # Data classes
    "HNSCoordinate",
    "StructuralError",
    "StructuralAnalysis",
    "ComparisonResult",
    # Core utilities
    "get_cell",
    "all_cells",
    "layer_info",
    "category_info",
    # Analysis functions (require Anthropic API)
    "analyze",
    "constrain",
    "compare",
    "coordinate",
    "batch_analyze",
    # Prompts
    "get_constraint_prompt",
    "get_evaluator_prompt",
    "build_layer_reference",
    "build_category_reference",
    "build_error_reference",
]
