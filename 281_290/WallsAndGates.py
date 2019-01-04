# 286. Walls and Gates

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the
# distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution:
    # 运用dfs，遍历所有gate，以0为出发点向四周搜索，搜索到的点grid更新为grid与dist的最小值
    def wallsAndGates(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: void
        """
        if not grid or not grid[0]:
            return
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    self.dfs(i, j, grid, 0)

    def dfs(self, x, y, grid, dist):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return
        if grid[x][y] > 0:
            grid[x][y] = min(dist, grid[x][y])
        self.dfs(x-1, y, grid, dist+1)
        self.dfs(x+1, y, grid, dist+1)
        self.dfs(x, y-1, grid, dist+1)
        self.dfs(x, y+1, grid, dist+1)