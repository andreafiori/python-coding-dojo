"""
rotate image | leetcode 48 | https://leetcode.com/problems/rotate-image/
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
method: actual rotation

testcase 1
matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

testcase 2
"""

class RotateImage(object):
    matrix: list[list[int]] = [[5, 1, 9, 11], [2, 4, 8, 10],[13, 3, 6, 7],[15, 14, 12, 16]]

    def solution_one(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # rotate from outside to inside
        if matrix is None or len(matrix) == 1:
            return
        ls = len(matrix)
        for i in range(ls / 2):
            # border
            begin, end = i, ls - 1 - i
            for k in range(ls - 2 * i - 1):
                temp = matrix[end - k][begin]
                matrix[end - k][begin] = matrix[end][end - k]
                matrix[end][end - k] = matrix[begin + k][end]
                matrix[begin + k][end] = matrix[begin][begin + k]
                matrix[begin][begin + k] = temp
        return

    def solution_two(self, matrix: list[list[int]]) -> None:
        n:      int = len(matrix)   # size (n x n)
        left:   int = 0             # left pointer
        right:  int = n - 1         # right pointer
        top:    int = 0             # top pointer
        bottom: int = 0             # bottom pointer
        temp:   int = 0             # temp variable

        # if left pointer is on
        # the right of the right pointer
        # stop iterating
        while left < right:

            # for each square in layer
            for i in range(right - left):
                top:    int = left
                bottom: int = right

                temp                        = matrix[top][left + i]     # save top-left
                matrix[top][left + i]       = matrix[bottom - i][left]  # bottom-left to top-left
                matrix[bottom - i][left]    = matrix[bottom][right - i] # bottom-right to bottom-left
                matrix[bottom][right - i]   = matrix[top + i][right]    # top-right to bottom-right
                matrix[top + i][right]      = temp                      # (saved) top-left to top-right

            # next layer
            left  = left + 1
            right = right - 1

    # transpose of the matrix
    def transpose(self, matrix: list[list[int]]) -> None:
        n: int = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

    # reflection of the matrix
    def reflect(self, matrix: list[list[int]]) -> None:
        n: int = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    def rotate(self, matrix: list[list[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
