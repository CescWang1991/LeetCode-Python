# 200. Number of islands
# dfs：从左上角开始遍历，将遍历到的"1"设为"s"，即起始点，然后做dfs，将搜索到的陆地点设为"0"，并继续dfs。
# 最后统计grid中的"s"的数量。

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "s"
                    self.dfs(i, j, grid)

        return sum(list(map(lambda x:x.count("s"), grid)))

    def dfs(self, x, y, grid):
        # 向左遍历
        if y > 0:
            if grid[x][y-1] == "1":
                grid[x][y-1] = "0"
                self.dfs(x, y-1, grid)
        # 向上遍历
        if x > 0:
            if grid[x-1][y] == "1":
                grid[x-1][y] = "0"
                self.dfs(x-1, y, grid)
        # 向右遍历
        if y < len(grid[0])-1:
            if grid[x][y+1] == "1":
                grid[x][y+1] = "0"
                self.dfs(x, y+1, grid)
        # 向下遍历
        if x < len(grid)-1:
            if grid[x+1][y] == "1":
                grid[x+1][y] = "0"
                self.dfs(x+1, y, grid)