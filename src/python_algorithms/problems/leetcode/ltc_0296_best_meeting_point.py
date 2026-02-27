"""
Best Meeting Point | https://leetcode.com/problems/best-meeting-point/

You are given an m x n binary grid where each cell contains either 0 or 1. Each cell with value 1 represents the home of a friend. Your task is to find a meeting point such that the total travel distance for all friends to reach this meeting point is minimized.

The total travel distance is calculated as the sum of individual distances from each friend's home to the meeting point. The distance between any two points is measured using Manhattan Distance, which is defined as distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, if you have a grid with friends at positions (0,0), (0,2), and (2,1), and you choose meeting point (0,1), the total travel distance would be:

Friend at (0,0) to (0,1): |0-0| + |1-0| = 1
Friend at (0,2) to (0,1): |0-0| + |1-2| = 1
Friend at (2,1) to (0,1): |0-2| + |1-1| = 2
Total: 1 + 1 + 2 = 4

The meeting point can be any cell in the grid (not necessarily a cell with value 1). Your goal is to return the minimum possible total travel distance.

"""

class BestMeetingPoint:
    # def minTotalDistance(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     # sort
    #     rows = []
    #     cols = []
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 1:
    #                 rows.append(i)
    #                 cols.append(j)
    #     row = rows[len(rows) / 2]
    #     cols.sort()
    #     col = cols[len(cols) / 2]
    #     return self.minDistance1D(rows, row) + self.minDistance1D(cols, col)

    # def minDistance1D(self, points, origin):
    #     distance = 0
    #     for point in points:
    #         distance += abs(point - origin)
    #     return distance

    def minDistance1D(self, points):
        """
        Minimum distance ID
        :param points:
        :return:
        """
        distance = 0
        i, j = 0, len(points) - 1
        while i < j:
            distance += points[j] - points[i]
            i += 1
            j -= 1
        return distance

    def minTotalDistance(self, grid):
        """
        Minimum total distance
        :param grid:
        :return:
        """
        rows = self.collectRows(grid)
        cols = self.collectCols(grid)
        row = rows[len(rows) / 2]
        col = cols[len(cols) / 2]
        return self.minDistance1D(rows) + self.minDistance1D(cols)

    def collectRows(self, grid):
        rows = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
        return rows

    def collectCols(self, grid):
        """
        Collect cols
        :param grid:
        :return:
        """
        cols = []
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    cols.append(j)
        return cols
