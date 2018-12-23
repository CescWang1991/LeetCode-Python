# 149. Maximum Points in a Line

from decimal import *

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # [[0, 0], [94911151, 94911150], [94911152, 94911151]]造成精度问题，用Decimal，精度为28
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if length < 3: return length
        max_points = 0
        for i in range(length):
            maps = {'inf': 0}
            # 与起点相同的点的个数，如果没有，则为1，最后加到map的value中，因为循环的时候没有算起始点。
            same = 1
            for j in range(i, length):
                if i == j:
                    continue
                if points[i].x == points[j].x and points[i].y != points[j].y:   # 在一条垂直于x轴的直线上
                    maps['inf'] += 1
                elif points[i].x != points[j].x:        # 算出斜率，加入到字典中计数
                    k = Decimal(points[i].y - points[j].y) / Decimal(points[i].x - points[j].x)
                    maps[k] = maps.get(k, 0) + 1
                else:
                    same += 1
            max_points = max(max_points, max(maps.values()) + same)
        return max_points