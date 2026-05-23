"""
HNS-36 Basic Usage Examples
Requires: pip install anthropic hns36
API key: set ANTHROPIC_API_KEY environment variable
"""

import hns36

# ── 1. Explore the coordinate system (no API needed) ─────────────────────────
print("=== HNS-36 Coordinate System ===\n")
print(hns36.build_layer_reference())
print()
print(hns36.build_category_reference())

# Get a specific cell
cell = hns36.get_cell("L3", "C5")
print(f"\nCell L3×C5: {cell['layer']} × {cell['category']}")
print(f"Layer: {cell['layer_description']}")
print(f"Category: {cell['category_description']}")

# ── 2. Analyze a response for structural errors ───────────────────────────────
print("\n=== Structural Error Analysis ===\n")

# This response contains structural errors (from the PoC experiment)
standard_response = """
Digital fatigue is essentially a mismatch between conscious enjoyment and unconscious 
cognitive cost. The dopamine system is partly responsible: enjoyable apps trigger reward 
responses that keep the brain in a state of heightened arousal, which is energetically 
costly over time. Additionally, the constant switching of attention fragments our focus 
in ways that accumulate into exhaustion.
"""

result = hns36.analyze(
    text=standard_response,
    question="Why do people feel exhausted by digital interfaces even when they enjoy using them?"
)

print(f"Total structural errors: {result.total_errors}")
print(f"Error types: {', '.join(result.error_types) or 'None'}")
print(f"Intention alignment: {result.intention_alignment}/5")
print(f"Structural stability: {result.structural_stability}/5")
print()
for error in result.errors:
    if error.detected:
        print(f"  [{error.error_type}] {error.note}")

# ── 3. Generate an HNS-36 constrained response ───────────────────────────────
print("\n=== HNS-36 Constrained Response ===\n")

response = hns36.constrain(
    "Why do people feel exhausted by digital interfaces even when they enjoy using them?"
)
print(response)

# ── 4. Compare two responses ─────────────────────────────────────────────────
print("\n=== Blind Comparison ===\n")

hns_response = """
[Addressing L2 CognitiveOS and L3 InteractionOS, with bridge to L4 EnvironmentOS]

At L2 CognitiveOS: digital interfaces demand continuous attention tracking — scanning 
for new information, detecting changes, processing visual hierarchies. This is an active, 
resource-consuming process.

The bridge from L2 to L3: continuous novelty creates persistent anticipation at L3 — 
not relaxation, but readiness for the next stimulus.

At L4 EnvironmentOS (design level): interface design that removes endpoint cues extends 
engagement beyond intentional time boundaries, working against the user's own goals.

The mechanism: L4 design structure → L2 perceptual demands → L3 unresolved arousal → 
cognitive resource depletion.
"""

result = hns36.compare(
    question="Why do people feel exhausted by digital interfaces?",
    response_a=standard_response,
    response_b=hns_response,
    label_a="Standard",
    label_b="HNS-36",
)

print(result.summary())

# ── 5. Assign coordinates ─────────────────────────────────────────────────────
print("\n=== Coordinate Assignment ===\n")

passages = [
    "Cultural norms that developed over decades now shape individual behavior.",
    "The stress response activates the hypothalamic-pituitary-adrenal axis.",
    "Team members negotiate task allocation through informal conversation.",
    "Institutional regulations constrain individual decision-making options.",
]

for passage in passages:
    coord = hns36.coordinate(passage)
    print(f"  {coord}  |  \"{passage[:60]}...\"")
