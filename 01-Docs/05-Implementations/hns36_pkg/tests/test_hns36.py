"""
HNS-36 Unit Tests (no API required)
Run: python -m pytest tests/
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
import hns36
from hns36.core import (
    LAYERS, CATEGORIES, ERROR_TYPES,
    HNSCoordinate, StructuralError, StructuralAnalysis,
    get_cell, all_cells, layer_info, category_info,
)


class TestCoordinateSystem:
    def test_layers_count(self):
        assert len(LAYERS) == 6

    def test_categories_count(self):
        assert len(CATEGORIES) == 6

    def test_error_types_count(self):
        assert len(ERROR_TYPES) == 5

    def test_all_cells_count(self):
        cells = all_cells()
        assert len(cells) == 36

    def test_get_cell_valid(self):
        cell = get_cell("L3", "C5")
        assert cell["cell_id"] == "L3×C5"
        assert cell["layer"] == "InteractionOS"
        assert cell["category"] == "System"

    def test_get_cell_invalid(self):
        with pytest.raises(ValueError):
            get_cell("L7", "C1")

    def test_layer_info(self):
        info = layer_info("L1")
        assert info["name"] == "PhysicalOS"
        assert "id" in info

    def test_category_info(self):
        info = category_info("C1")
        assert info["name"] == "Civilization"

    def test_layer_info_invalid(self):
        with pytest.raises(ValueError):
            layer_info("L9")


class TestDataClasses:
    def test_hns_coordinate(self):
        coord = HNSCoordinate(layer="L6", category="C1")
        assert coord.layer_name == "PatternOS"
        assert coord.category_name == "Civilization"
        assert coord.cell_id == "L6×C1"
        assert "PatternOS" in str(coord)

    def test_structural_error_detected(self):
        err = StructuralError(
            error_type="LayerJump",
            detected=True,
            note="Moves from L1 to L3 without bridge"
        )
        assert err.detected is True
        assert "bridge" in err.fix.lower()

    def test_structural_analysis_empty(self):
        analysis = StructuralAnalysis(text="Test text")
        assert analysis.total_errors == 0
        assert analysis.is_structurally_clean is True
        assert analysis.error_types == []

    def test_structural_analysis_with_errors(self):
        analysis = StructuralAnalysis(
            text="Test",
            errors=[
                StructuralError("LayerJump", True, "L1 to L3"),
                StructuralError("ScopeDrift", False, ""),
                StructuralError("UnsupportedCausality", True, "no mechanism"),
            ]
        )
        assert analysis.total_errors == 2
        assert "LayerJump" in analysis.error_types
        assert "UnsupportedCausality" in analysis.error_types
        assert "ScopeDrift" not in analysis.error_types


class TestPrompts:
    def test_constraint_prompt_full(self):
        prompt = hns36.get_constraint_prompt("full")
        assert "HNS-36" in prompt
        assert "Layer Jump" in prompt
        assert "bridge" in prompt.lower()

    def test_constraint_prompt_compact(self):
        prompt = hns36.get_constraint_prompt("compact")
        assert "HNS-36" in prompt
        assert len(prompt) < len(hns36.get_constraint_prompt("full"))

    def test_evaluator_prompt(self):
        prompt = hns36.get_evaluator_prompt()
        assert "JSON" in prompt
        assert "LayerJump" in prompt
        assert "structural_stability" in prompt

    def test_layer_reference(self):
        ref = hns36.build_layer_reference()
        assert "PhysicalOS" in ref
        assert "PatternOS" in ref
        assert "L1" in ref
        assert "L6" in ref

    def test_category_reference(self):
        ref = hns36.build_category_reference()
        assert "Civilization" in ref
        assert "External" in ref

    def test_error_reference(self):
        ref = hns36.build_error_reference()
        assert "LayerJump" in ref
        assert "ScopeDrift" in ref
        assert "Fix:" in ref


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
