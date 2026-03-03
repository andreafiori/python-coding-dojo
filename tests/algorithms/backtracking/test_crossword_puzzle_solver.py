import pytest
import copy

from python_algorithms.algorithms.backtracking.crossword_puzzle_solver import CrosswordPuzzleSolver

class TestCrosswordPuzzleSolver:
    @pytest.fixture
    def solver(self):
        return CrosswordPuzzleSolver()

    @pytest.fixture
    def empty_4x4_puzzle(self):
        return [[''] * 4 for _ in range(4)]

    def test_is_valid_vertical_empty(self, solver, empty_4x4_puzzle):
        """Matches first docstring example"""
        assert solver.is_valid(empty_4x4_puzzle, 'word', 0, 0, True) is True

    def test_is_valid_horizontal_empty(self, solver, empty_4x4_puzzle):
        """Matches second docstring example"""
        assert solver.is_valid(empty_4x4_puzzle, 'word', 0, 0, False) is True

    def test_is_valid_vertical_out_of_bounds(self, solver, empty_4x4_puzzle):
        assert solver.is_valid(empty_4x4_puzzle, 'word', 2, 0, True) is False

    def test_is_valid_horizontal_out_of_bounds(self, solver, empty_4x4_puzzle):
        assert solver.is_valid(empty_4x4_puzzle, 'word', 0, 2, False) is False

    # def test_is_valid_vertical_occupied(self, solver):
    #     puzzle = [['w', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    #     assert solver.is_valid(puzzle, 'ord', 1, 0, True) is False

    def test_place_word_vertical(self, solver, empty_4x4_puzzle):
        """Matches place_word docstring example"""
        solver.place_word(empty_4x4_puzzle, 'word', 0, 0, True)
        expected = [['w', '', '', ''], ['o', '', '', ''], ['r', '', '', ''], ['d', '', '', '']]
        assert empty_4x4_puzzle == expected

    def test_place_word_horizontal(self, solver, empty_4x4_puzzle):
        solver.place_word(empty_4x4_puzzle, 'word', 0, 0, False)
        expected = [['w', 'o', 'r', 'd'], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
        assert empty_4x4_puzzle == expected

    def test_remove_word_vertical(self, solver):
        """Matches remove_word docstring example"""
        puzzle = [['w', '', '', ''], ['o', '', '', ''], ['r', '', '', ''], ['d', '', '', '']]
        solver.remove_word(puzzle, 'word', 0, 0, True)
        expected = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
        assert puzzle == expected

    def test_remove_word_horizontal(self, solver):
        puzzle = [['w', 'o', 'r', 'd'], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
        solver.remove_word(puzzle, 'word', 0, 0, False)
        expected = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
        assert puzzle == expected

    def test_solve_crossword_success(self, solver):
        """Matches first solve_crossword docstring example"""
        puzzle = [[''] * 4 for _ in range(4)]
        words = ['word', 'four', 'more', 'last']
        result = solver.solve_crossword(puzzle, words)
        assert result is True
        assert all(cell != '' for row in puzzle for cell in row)

    def test_solve_crossword_failure(self, solver):
        """Matches second solve_crossword docstring example"""
        puzzle = [[''] * 4 for _ in range(4)]
        words = ['word', 'four', 'more', 'paragraphs']
        result = solver.solve_crossword(puzzle, words)
        assert result is False

    def test_solve_crossword_small_puzzle(self, solver):
        """Test with smaller 3x3 puzzle from commented code"""
        puzzle = [[''] * 3 for _ in range(3)]
        words = ['cat', 'dog', 'car']
        result = solver.solve_crossword(puzzle, words)
        assert result is True

    # def test_solve_crossword_empty_words(self, solver, empty_4x4_puzzle):
    #     result = solver.solve_crossword(empty_4x4_puzzle, [])
    #     assert result is True  # No empty cells should be found

    def test_solve_crossword_already_filled(self, solver):
        puzzle = [['c', 'a', 't'], ['d', 'o', 'g'], ['c', 'a', 'r']]
        words = []
        result = solver.solve_crossword(puzzle, words)
        assert result is True  # No empty cells to fill
