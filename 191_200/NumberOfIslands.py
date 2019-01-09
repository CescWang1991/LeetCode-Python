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

# 305. Number of Islands II

# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns
# the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after
# each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or
# vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution2:
    # 运用并查集的方法，建立一个m*n的数组表示根岛屿的情况，初始设全部元素为-2，代表水；遍历positions，将pos对应的岛屿设
    # 为-1，然后上下左右遍历，调用find函数，返回周围元素的跟岛屿情况，然后做union操作。
    def numIslands(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: list[list[int]]
        :rtype: list[int]
        """
        self.m = m
        self.n = n
        self.islands = [-2] * (m * n)
        count = 0
        res = []
        for pos in positions:
            res.append(count)
            index = pos[0] * n + pos[1]
            self.islands[index] = -1
            count += 1
            upper = self.find(index - n)
            if upper != None:
                self.islands[index] = upper     # 相当于union操作，将当前岛屿与上面的合并
                count -= 1
                continue
            lower = self.find(index + n)
            if lower != None:
                self.islands[index] = lower
                count -= 1
                continue
            left = self.find(index - 1)
            if left != None:
                self.islands[index] = left
                count -= 1
                continue
            right = self.find(index + 1)
            if right != None:
                self.islands[index] = right
                count -= 1
                continue

        res = res[1:] + [count]
        return res

    def find(self, index):
        if index < 0 or index >= self.m * self.n or self.islands[index] == -2:
            return None
        if self.islands[index] == -1:   # 跟岛屿为本身，返回本身的index
            return index
        else:
            return self.find(self.islands[index])   # 找寻当前index的根岛屿