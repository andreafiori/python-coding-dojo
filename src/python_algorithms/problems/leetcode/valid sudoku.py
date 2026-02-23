"""
valid sudoku | leetcode 36 | https://leetcode.com/problems/valid-sudoku/
Determine if a n^2 x n^2 Psuedo-Sudoku board is valid.
Only the filled cells need to be validated.
"""

import collections

class Solution(object):
    def isValidSudoku(self, board):
        vset = [0] * 9
        hset = [0] * 9
        bset = [0] * 9
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != '.':
                    index = 1 << (ord(curr) - ord('0'))
                    if (hset[i] & index) > 0 or\
                                    (vset[j] & index) > 0 or\
                                    (bset[(i / 3) * 3 + j / 3] & index) > 0:
                        return False
                    hset[i] |= index
                    vset[j] |= index
                    bset[(i / 3) * 3 + j / 3] |= index
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] == '.':
                    continue

                isInRow = board[i][j] in rows[i]
                isInColumn = board[i][j] in columns[j]
                isInSquare = board[i][j] in squares[(i//3, j//3)]
                if (isInRow or isInColumn or isInSquare):
                    return False

                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])

        return True