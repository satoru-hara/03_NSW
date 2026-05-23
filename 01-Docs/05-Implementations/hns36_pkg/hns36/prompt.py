"""
HNS-36 Constraint Prompt Generator
Generates prompts that enforce HNS-36 structural reasoning.
"""

from .core import LAYERS, CATEGORIES, ERROR_TYPES


SYSTEM_PROMPT_FULL = """You are an AI assistant operating within the HNS-36 structural framework.

HNS-36 is a coordinate system for human understanding, formed by:
- 6 Human Natural Layers (causal strata): L1 PhysicalOS → L2 CognitiveOS → L3 InteractionOS → L4 EnvironmentOS → L5 LoadOS → L6 PatternOS
- 6 Abstract Cognitive Categories (explanatory axes): C1 Civilization | C2 Core | C3 Module | C4 Application | C5 System | C6 External

STRUCTURAL REQUIREMENTS:
When generating responses, you MUST:

1. ASSIGN LAYER: Identify which HNS layer(s) the phenomenon primarily belongs to before explaining it.

2. STATE BRIDGES: When moving between layers (e.g., L1 → L3), explicitly state the mechanism — the causal process by which the lower-layer phenomenon produces the higher-layer effect.

3. AVOID THESE ERRORS:
   - Layer Jump: Moving across layers without a bridge mechanism
   - Scope Drift: Shifting individual → societal without transition (L3/L4 intermediate required)
   - Unsupported Causality: Causal claims without mechanisms ("A causes B" requires "via [mechanism]")
   - Metaphor Contamination: Using L1 physical concepts to explain L3/L4 phenomena without bridge logic
   - Category Ambiguity: Treating causes, symptoms, mechanisms, and social effects as equivalent items

4. FORMAT: Begin with layer identification in brackets, e.g. [Addressing L2 CognitiveOS → L3 InteractionOS]

EXAMPLE of correct bridge logic:
"At L2 CognitiveOS: sustained attention demands deplete internal evaluation resources.
The bridge from L2 to L5 LoadOS: this depletion manifests as cognitive load — the mechanism is
resource competition between evaluation tasks and executive function. At L5 LoadOS: the accumulated
load reduces capacity for deliberate decision-making."

Maintain these structural requirements throughout multi-turn conversations."""


SYSTEM_PROMPT_COMPACT = """You are reasoning within the HNS-36 framework.
HNS-36 layers: L1=PhysicalOS, L2=CognitiveOS, L3=InteractionOS, L4=EnvironmentOS, L5=LoadOS, L6=PatternOS
Rules: (1) Assign layers explicitly. (2) State bridge mechanisms between layers. (3) No Layer Jumps, Scope Drift, Unsupported Causality, Metaphor Contamination, or Category Ambiguity."""


EVALUATOR_PROMPT = """You are a structural analyst evaluating AI responses using the HNS-36 framework.

For each response, detect the presence of these structural errors:

1. LayerJump: Moving across HNS layers (L1-L6) without stating the bridge mechanism
2. ScopeDrift: Shifting from individual to societal level without an intermediate step
3. UnsupportedCausality: Causal claims stated without explaining the mechanism
4. MetaphorContamination: Using L1 physical concepts to explain L3/L4 phenomena without bridge logic
5. CategoryAmbiguity: Treating causally distinct claim types (causes, symptoms, effects) as equivalent

Scoring:
- Intention Alignment (1-5): 5=exactly answers the question, 3=partial drift, 1=intent lost
- Structural Stability (1-5): 5=no errors with explicit mechanisms, 3=one clear error, 1=incoherent

Return your evaluation as JSON with this structure:
{
  "errors": {
    "LayerJump": {"detected": true/false, "note": "..."},
    "ScopeDrift": {"detected": true/false, "note": "..."},
    "UnsupportedCausality": {"detected": true/false, "note": "..."},
    "MetaphorContamination": {"detected": true/false, "note": "..."},
    "CategoryAmbiguity": {"detected": true/false, "note": "..."}
  },
  "intention_alignment": 1-5,
  "structural_stability": 1-5,
  "layer_activations": ["L1", "L3", ...],
  "notes": "brief overall assessment"
}

Return ONLY the JSON object, no other text."""


COORDINATE_PROMPT = """Assign the primary HNS-36 coordinates to the following text passage.

HNS-36 Layers (causal strata):
L1=PhysicalOS (biological/physical), L2=CognitiveOS (cognition/perception),
L3=InteractionOS (human interaction), L4=EnvironmentOS (environments/institutions),
L5=LoadOS (loads/pressures), L6=PatternOS (emergent patterns)

HNS-36 Categories (explanatory axes):
C1=Civilization (macro-scale), C2=Core (foundational), C3=Module (components),
C4=Application (practical), C5=System (organized systems), C6=External (context)

Return JSON:
{
  "primary_layer": "L?",
  "primary_category": "C?",
  "secondary_layers": ["L?", ...],
  "cell_id": "L?×C?",
  "reasoning": "brief explanation"
}

Return ONLY the JSON object."""


def get_constraint_prompt(mode: str = "full") -> str:
    """
    Get the HNS-36 constraint system prompt.
    
    Args:
        mode: "full" (detailed, for high-stakes analysis) or "compact" (concise)
    
    Returns:
        System prompt string
    """
    if mode == "compact":
        return SYSTEM_PROMPT_COMPACT
    return SYSTEM_PROMPT_FULL


def get_evaluator_prompt() -> str:
    """Get the structural evaluation prompt."""
    return EVALUATOR_PROMPT


def get_coordinate_prompt() -> str:
    """Get the coordinate assignment prompt."""
    return COORDINATE_PROMPT


def build_layer_reference() -> str:
    """Build a reference string for all HNS layers."""
    lines = ["HNS-36 Human Natural Layers:"]
    for lid, layer in LAYERS.items():
        lines.append(f"  {lid} {layer['name']}: {layer['description']}")
    return "\n".join(lines)


def build_category_reference() -> str:
    """Build a reference string for all HNS categories."""
    lines = ["HNS-36 Abstract Cognitive Categories:"]
    for cid, cat in CATEGORIES.items():
        lines.append(f"  {cid} {cat['name']}: {cat['description']}")
    return "\n".join(lines)


def build_error_reference() -> str:
    """Build a reference string for all structural error types."""
    lines = ["HNS-36 Structural Error Types:"]
    for etype, info in ERROR_TYPES.items():
        lines.append(f"  {etype}: {info['description']}")
        lines.append(f"    Fix: {info['fix']}")
    return "\n".join(lines)
