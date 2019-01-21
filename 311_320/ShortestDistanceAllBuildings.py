# 317. Shortest Distance from All Buildings

# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only
# move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
#
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

class Solution:
    # 运用bfs，从每一个建筑出发，计算到每一个land的距离，并用字典记录，遍历完所有之后，用字典找到距离和最小的land
    def shortestDistance(self, grid):
        """
        :type grid: list[list[int]]
        :return:
        """
        self.n = len(grid)
        self.m = len(grid[0])
        from collections import defaultdict
        self.dict = defaultdict(list)       # 字典key为land的坐标，value为到每一个建筑的距离列表
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    count += 1
                    land = [grid[k].copy() for k in range(self.n)]      # 二维数组copy，需要逐行进行copy
                    self.buildDistDict(i, j, land)
        if not self.dict or len(list(self.dict.items())[0][1]) != count:    # 字典不存在或者对应的value数组数量不等于建筑个数
            return -1
        for k, v in self.dict.items():
            self.dict[k] = sum(v)
        return min(self.dict, key=self.dict.get)    # 返回最小距离所对应的key

    def buildDistDict(self, x, y, land):
        queue = [([x, y], 0)]
        while queue:
            curr = queue[0][0]
            dist = queue[0][1]
            del queue[0]
            self.bfs(curr[0] - 1, curr[1], land, queue, dist)
            self.bfs(curr[0] + 1, curr[1], land, queue, dist)
            self.bfs(curr[0], curr[1] - 1, land, queue, dist)
            self.bfs(curr[0], curr[1] + 1, land, queue, dist)
        return

    def bfs(self, x, y, land, queue, dist):
        if 0 <= x < self.n and 0 <= y < self.m and land[x][y] == 0:
            queue.append(([x, y], dist + 1))
            self.dict[(x, y)].append(dist+1)
            land[x][y] = -1
        return