"""
HNS-36 Core Coordinate System
Human Natural Structure — 6 Layers × 6 Categories = 36 Cells
Natural Structure Works (NSW) | Version 1.0 | May 2026
"""

from dataclasses import dataclass, field
from typing import Optional


# ── Human Natural Layers (Causal Structure) ──────────────────────────────────

LAYERS = {
    "L1": {
        "name": "PhysicalOS",
        "description": "Physical and biological foundations that enable all higher-order functions.",
        "examples": ["reflexes", "neural substrates", "physical constraints", "muscle fatigue"],
    },
    "L2": {
        "name": "CognitiveOS",
        "description": "Perception, memory, internal processing, and interpretation.",
        "examples": ["memory retrieval", "perception", "decision-making", "attention"],
    },
    "L3": {
        "name": "InteractionOS",
        "description": "Human-to-human and human-to-environment interactions.",
        "examples": ["conversation", "cooperation", "conflict", "behavioral exchange"],
    },
    "L4": {
        "name": "EnvironmentOS",
        "description": "Physical, social, and institutional environments.",
        "examples": ["laws", "institutions", "physical settings", "social norms"],
    },
    "L5": {
        "name": "LoadOS",
        "description": "Internal and external loads, pressures, and constraints.",
        "examples": ["stress", "workload", "resource scarcity", "cognitive load"],
    },
    "L6": {
        "name": "PatternOS",
        "description": "Emergent behavioral patterns and long-term regularities.",
        "examples": ["culture", "norms", "behavioral trends", "civilizational patterns"],
    },
}

# ── Abstract Cognitive Categories (Non-causal Explanatory Axes) ───────────────

CATEGORIES = {
    "C1": {
        "name": "Civilization",
        "description": "Macro-scale, historical, and civilizational framing.",
        "question": "How does this phenomenon relate to civilizational-scale structures?",
    },
    "C2": {
        "name": "Core",
        "description": "Foundational principles and essential structures.",
        "question": "What is the essential structure or irreducible principle here?",
    },
    "C3": {
        "name": "Module",
        "description": "Components, elements, and functional units.",
        "question": "What are the discrete, analyzable parts of this phenomenon?",
    },
    "C4": {
        "name": "Application",
        "description": "Practical uses and applied contexts.",
        "question": "How is this phenomenon used or applied in practice?",
    },
    "C5": {
        "name": "System",
        "description": "Organized systems, mechanisms, and structured processes.",
        "question": "How does this phenomenon operate as a system?",
    },
    "C6": {
        "name": "External",
        "description": "Outer contextual factors and external influences.",
        "question": "What external conditions shape or constrain this phenomenon?",
    },
}

# ── Structural Error Types ─────────────────────────────────────────────────────

ERROR_TYPES = {
    "LayerJump": {
        "description": "Moving across HNS layers without a bridge mechanism.",
        "pattern": "Response moves between causal levels without stating the connecting mechanism.",
        "example": "Explaining psychological exhaustion (L3) directly from biology (L1) without mechanism.",
        "fix": "Add explicit bridge logic: state the causal mechanism that connects the layers.",
    },
    "ScopeDrift": {
        "description": "Shifting from individual to societal level without transition.",
        "pattern": "Individual experience becomes social phenomenon without intermediate step.",
        "example": "Moving from personal stress (L5) directly to societal norms (L6) without L3/L4 bridge.",
        "fix": "Insert the intermediate relational layer (L3 InteractionOS or L4 EnvironmentOS).",
    },
    "UnsupportedCausality": {
        "description": "Causal claim stated without a mechanism.",
        "pattern": "A causes B asserted without explaining how.",
        "example": '"Dopamine triggers exhaustion" — stated as fact, mechanism not given.',
        "fix": "State the mechanism: describe the causal process by which A produces B.",
    },
    "MetaphorContamination": {
        "description": "L1 Physical concept used to explain L3/L4 phenomena without bridge logic.",
        "pattern": "Biological or physical analogy applied to psychological/social phenomena.",
        "example": '"The brain goes offline" to explain decision fatigue — metaphor without mechanism.',
        "fix": "Add bridge logic: explain the causal pathway from the physical substrate to the target layer.",
    },
    "CategoryAmbiguity": {
        "description": "Causally distinct types of claims treated as equivalent items.",
        "pattern": "Causes, symptoms, mechanisms, and social effects listed as if equivalent.",
        "example": 'Listing burnout "causes" that mix L3 experiences, L4 conditions, and L6 patterns.',
        "fix": "Assign each claim to its correct layer before listing; distinguish types explicitly.",
    },
}


# ── Data Classes ──────────────────────────────────────────────────────────────

@dataclass
class HNSCoordinate:
    """A position in the HNS-36 coordinate space."""
    layer: str        # e.g. "L3"
    category: str     # e.g. "C2"

    @property
    def layer_name(self) -> str:
        return LAYERS[self.layer]["name"]

    @property
    def category_name(self) -> str:
        return CATEGORIES[self.category]["name"]

    @property
    def cell_id(self) -> str:
        return f"{self.layer}×{self.category}"

    def __str__(self) -> str:
        return f"{self.cell_id} ({self.layer_name} × {self.category_name})"


@dataclass
class StructuralError:
    """A detected structural error in a text."""
    error_type: str                    # Key from ERROR_TYPES
    detected: bool
    note: str = ""

    @property
    def description(self) -> str:
        return ERROR_TYPES[self.error_type]["description"]

    @property
    def fix(self) -> str:
        return ERROR_TYPES[self.error_type]["fix"]


@dataclass
class StructuralAnalysis:
    """Full structural analysis of a text passage."""
    text: str
    errors: list[StructuralError] = field(default_factory=list)
    intention_alignment: Optional[float] = None   # 1–5
    structural_stability: Optional[float] = None  # 1–5
    layer_activations: list[str] = field(default_factory=list)
    notes: str = ""

    @property
    def total_errors(self) -> int:
        return sum(1 for e in self.errors if e.detected)

    @property
    def error_types(self) -> list[str]:
        return [e.error_type for e in self.errors if e.detected]

    @property
    def is_structurally_clean(self) -> bool:
        return self.total_errors == 0

    def summary(self) -> str:
        lines = [
            f"Structural errors: {self.total_errors}",
            f"Error types: {', '.join(self.error_types) if self.error_types else 'None'}",
        ]
        if self.intention_alignment is not None:
            lines.append(f"Intention alignment: {self.intention_alignment:.1f}/5")
        if self.structural_stability is not None:
            lines.append(f"Structural stability: {self.structural_stability:.1f}/5")
        if self.layer_activations:
            lines.append(f"Layers activated: {', '.join(self.layer_activations)}")
        return "\n".join(lines)


@dataclass
class ComparisonResult:
    """Result of comparing two responses (blind or labeled)."""
    question: str
    analysis_a: StructuralAnalysis
    analysis_b: StructuralAnalysis
    label_a: Optional[str] = None   # Revealed after evaluation
    label_b: Optional[str] = None

    def summary(self) -> str:
        lines = [
            f"Question: {self.question}",
            "",
            "Response A:",
            f"  Errors: {self.analysis_a.total_errors} ({', '.join(self.analysis_a.error_types) or 'none'})",
            f"  Stability: {self.analysis_a.structural_stability or '—'}/5",
            "",
            "Response B:",
            f"  Errors: {self.analysis_b.total_errors} ({', '.join(self.analysis_b.error_types) or 'none'})",
            f"  Stability: {self.analysis_b.structural_stability or '—'}/5",
        ]
        if self.label_a:
            lines += ["", f"[Label reveal] A={self.label_a}, B={self.label_b}"]
        return "\n".join(lines)


# ── Cell Reference Utilities ───────────────────────────────────────────────────

def get_cell(layer: str, category: str) -> dict:
    """Get the structural position description for a given L×C cell."""
    l = LAYERS.get(layer)
    c = CATEGORIES.get(category)
    if not l or not c:
        raise ValueError(f"Invalid cell: {layer}×{category}")
    return {
        "cell_id": f"{layer}×{category}",
        "layer": l["name"],
        "category": c["name"],
        "layer_description": l["description"],
        "category_description": c["description"],
    }


def all_cells() -> list[dict]:
    """Return all 36 cells in the HNS matrix."""
    cells = []
    for layer in LAYERS:
        for category in CATEGORIES:
            cells.append(get_cell(layer, category))
    return cells


def layer_info(layer_id: str) -> dict:
    """Return information about a Human Natural Layer."""
    if layer_id not in LAYERS:
        raise ValueError(f"Unknown layer: {layer_id}. Valid: {list(LAYERS.keys())}")
    return {**LAYERS[layer_id], "id": layer_id}


def category_info(category_id: str) -> dict:
    """Return information about an Abstract Cognitive Category."""
    if category_id not in CATEGORIES:
        raise ValueError(f"Unknown category: {category_id}. Valid: {list(CATEGORIES.keys())}")
    return {**CATEGORIES[category_id], "id": category_id}
