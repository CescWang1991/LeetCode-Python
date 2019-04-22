# 296. Best Meeting Point

# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values
# 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where
# distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
#
# For example, given three people living at (0,0), (0,4), and (2,2):
#
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
#
# Hint:
# Try to solve it in one dimension first. How can this solution apply to the two dimension case?

class Solution:
    # 我们考虑一维情况，将所有点按顺序排列[A, B, C, D]，最佳开会地点在B, C之间，且距离为D - A + C - B。
    # 拓展到二维空间，由于计算曼哈顿距离，只要把每个维度的距离相加即可。
    def minTotalDistance(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        xAxis = []
        yAxis = []
        dist = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    xAxis.append(i)
                    yAxis.append(j)
        xAxis = sorted(xAxis)
        yAxis = sorted(yAxis)
        n = len(xAxis)
        lo, hi = 0, n-1
        while lo < hi:      # 从两头开始向中间遍历
            dist += xAxis[hi] - xAxis[lo] + yAxis[hi] - yAxis[lo]
            lo += 1
            hi -= 1

        return dist