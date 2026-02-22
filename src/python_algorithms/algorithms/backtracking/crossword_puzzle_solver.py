"""
A solution to puzzle problem is to solve the crossword puzzle
https://www.geeksforgeeks.org/solve-crossword-puzzle/
"""

class CrosswordPuzzleSolver(object):
    def is_valid(
        self, puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
    ) -> bool:
        """
        Check if a word can be placed at the given position.

        >>> puzzle = [
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', '']
        ... ]
        >>> is_valid(puzzle, 'word', 0, 0, True)
        True
        >>> puzzle = [
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', '']
        ... ]
        >>> is_valid(puzzle, 'word', 0, 0, False)
        True
        """
        for i in range(len(word)):
            if vertical:
                if row + i >= len(puzzle) or puzzle[row + i][col] != "":
                    return False
            elif col + i >= len(puzzle[0]) or puzzle[row][col + i] != "":
                return False
        return True

    def place_word(
        self, puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
    ) -> None:
        """
        Place a word at the given position.

        >>> puzzle = [
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', '']
        ... ]
        >>> place_word(puzzle, 'word', 0, 0, True)
        >>> puzzle
        [['w', '', '', ''], ['o', '', '', ''], ['r', '', '', ''], ['d', '', '', '']]
        """
        for i, char in enumerate(word):
            if vertical:
                puzzle[row + i][col] = char
            else:
                puzzle[row][col + i] = char


    def remove_word(
        self, puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
    ) -> None:
        """
        Remove a word from the given position.

        >>> puzzle = [
        ...     ['w', '', '', ''],
        ...     ['o', '', '', ''],
        ...     ['r', '', '', ''],
        ...     ['d', '', '', '']
        ... ]
        >>> remove_word(puzzle, 'word', 0, 0, True)
        >>> puzzle
        [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
        """
        for i in range(len(word)):
            if vertical:
                puzzle[row + i][col] = ""
            else:
                puzzle[row][col + i] = ""


    def solve_crossword(self, puzzle: list[list[str]], words: list[str]) -> bool:
        """
        Solve the crossword puzzle using backtracking.

        >>> puzzle = [
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', '']
        ... ]

        >>> words = ['word', 'four', 'more', 'last']
        >>> solve_crossword(puzzle, words)
        True
        >>> puzzle = [
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', ''],
        ...     ['', '', '', '']
        ... ]
        >>> words = ['word', 'four', 'more', 'paragraphs']
        >>> solve_crossword(puzzle, words)
        False
        """
        for row in range(len(puzzle)):
            for col in range(len(puzzle[0])):
                if puzzle[row][col] == "":
                    for word in words:
                        for vertical in [True, False]:
                            if self.is_valid(puzzle, word, row, col, vertical):
                                self.place_word(puzzle, word, row, col, vertical)
                                words.remove(word)
                                if self.solve_crossword(puzzle, words):
                                    return True
                                words.append(word)
                                self.remove_word(puzzle, word, row, col, vertical)
                    return False
        return True
