"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3

Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    All the points are unique.

"""

from typing import List

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class MaxPointOnALine(object):
    def maxPoints(self, points: List[Point]):
        """
        :type points: List[Point]
        :rtype: int
        """
        # map all possible angle
        if points is None or len(points) == 0:
            return 0
        ls = len(points)
        res = 0
        for i in range(ls):
            line_map = {}
            overlap = max_point = 0
            for j in range(i + 1, ls):
                x, y = points[j].x - points[i].x, points[j].y - points[i].y
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                gcd = self.generateGCD(x, y)
                if gcd != 0:
                    x /= gcd
                    y /= gcd
                if x in line_map:
                    if y in line_map[x]:
                        line_map[x][y] += 1
                    else:
                        line_map[x][y] = 1
                else:
                    line_map[x] = {}
                    line_map[x][y] = 1
                max_point = max(max_point, line_map[x][y])
            res = max(res, max_point + overlap + 1)
        return res

    def generateGCD(self, x, y):
        if y == 0:
            return x
        else:
            return self.generateGCD(y, x % y)
