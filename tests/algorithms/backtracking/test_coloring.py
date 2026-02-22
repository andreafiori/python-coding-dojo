import pytest
from typing import List

from src.python_algorithms.algorithms.backtracking.coloring import Coloring

class TestColoring:
    @pytest.fixture
    def coloring(self):
        return Coloring()

    def test_valid_coloring_valid(self, coloring):
        """Matches the first docstring example"""
        neighbours = [0,1,0,1,0]
        colored_vertices = [0, 2, 1, 2, 0]
        assert coloring.valid_coloring(neighbours, colored_vertices, 1) is True

    def test_valid_coloring_invalid(self, coloring):
        """Matches the second docstring example"""
        neighbours = [0,1,0,1,0]
        colored_vertices = [0, 2, 1, 2, 0]
        assert coloring.valid_coloring(neighbours, colored_vertices, 2) is False

    def test_valid_coloring_no_neighbors(self, coloring):
        assert coloring.valid_coloring([], [], 0) is True

    def test_valid_coloring_same_color_conflict(self, coloring):
        neighbours = [1]
        colored_vertices = [0]
        assert coloring.valid_coloring(neighbours, colored_vertices, 0) is False

    def test_color_success(self, coloring):
        """Uses EXACT graph from color() docstring"""
        graph = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        result = coloring.color(graph, 3)
        assert len(result) == 5
        assert result.count(-1) == 0
        assert result == [0, 1, 0, 2, 0]  # Expected from docstring

    def test_color_fail(self, coloring):
        """Uses same graph, but max_colors=2 should fail"""
        graph = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        result = coloring.color(graph, 2)
        assert result == []

    def test_color_empty_graph(self, coloring):
        assert coloring.color([], 1) == []

    def test_util_color_complete_base_case(self, coloring):
        """Tests index == len(graph) base case"""
        graph = [[0]]  # Single vertex graph
        colored_vertices = [0]  # Already colored
        assert coloring.util_color(graph, 3, colored_vertices, 1) is True

    def test_util_color_partial_success(self, coloring):
        """Tests partial coloring that can be completed"""
        graph = [
            [0, 1],
            [1, 0]
        ]
        colored_vertices = [-1, -1]
        result = coloring.util_color(graph, 2, colored_vertices, 0)
        assert result is True
        assert colored_vertices[0] != -1 and colored_vertices[1] != -1
