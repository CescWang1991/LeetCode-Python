# 迷宫寻路

# 题目描述
# 假设一个探险家被困在了地底的迷宫之中，要从当前位置开始找到一条通往迷宫出口的路径。迷宫可以用一个二维矩阵组成，有的部分
# 是墙，有的部分是路。迷宫之中有的路上还有门，每扇门都在迷宫的某个地方有与之匹配的钥匙，只有先拿到钥匙才能打开门。请设计
# 一个算法，帮助探险家找到脱困的最短路径。如前所述，迷宫是通过一个二维矩阵表示的，每个元素的值的含义如下 0-墙，1-路，
# 2-探险家的起始位置，3-迷宫的出口，大写字母-门，小写字母-对应大写字母所代表的门的钥匙

# 输入描述:
# 迷宫的地图，用二维矩阵表示。第一行是表示矩阵的行数和列数M和N
# 后面的M行是矩阵的数据，每一行对应与矩阵的一行（中间没有空格）。M和N都不超过100, 门不超过10扇。

# 输出描述:
# 路径的长度，是一个整数

# 解法一：DFS(不成功)
class Solution1:
    def findWays(self, matrix, m, n):
        """
        :type matrix: list[list[str]]
        :rtype: int
        """
        start = [0, 0]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "2":
                    start = [i, j]
                    break
        self.matrix = matrix
        self.origin = [matrix[i].copy() for i in range(m)]
        self.m = m
        self.n = n
        self.length = float('inf')
        self.search(start[0], start[1], [], 0)

        return self.length

    def search(self, i, j, keys, length):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.matrix[i][j] == "0" or self.matrix[i][j] == "#":
            return
        print(i, j, self.matrix[i][j], keys, length)
        if self.matrix[i][j] == "3":
            self.length = min(self.length, length)
            return
        if self.matrix[i][j].isupper():
            if self.matrix[i][j].lower() in keys:
                self.matrix[i][j] = "#"
                self.dfs(i, j, keys, length)
            return
        if self.matrix[i][j].islower():
            if self.matrix[i][j] in keys:
                return
            keys.append(self.matrix[i][j])
            self.matrix = [self.origin[i].copy() for i in range(self.m)]
            self.matrix[i][j] = "#"
            self.dfs(i, j, keys, length)
            return
        if self.matrix[i][j] == "1" or self.matrix[i][j] == "2":
            self.matrix[i][j] = "#"
            self.dfs(i, j, keys, length)
            return
        return

    def dfs(self, i, j, keys, length):
        self.search(i - 1, j, keys.copy(), length + 1)
        self.search(i + 1, j, keys.copy(), length + 1)
        self.search(i, j - 1, keys.copy(), length + 1)
        self.search(i, j + 1, keys.copy(), length + 1)


# 解法二：BFS
class Solution2:
    def findWays(self, matrix, m, n):
        """
        :type matrix: list[list[str]]
        :rtype: int
        """
        start = [0, 0]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "2":
                    start = [i, j]
                    break
        self.queue = [[start[0], start[1], [], 0]]   # row, col, keys, length
        self.matrix = matrix
        while self.queue:
            row = self.queue[0][0]
            col = self.queue[0][1]
            print(self.queue[0], self.matrix[row][col])
            if 0 <= row - 1 <= m - 1:  # 向上遍历
                if self.bfs(row-1, col, self.queue[0][2].copy(), self.queue[0][3]):
                    return self.queue[-1][3]
            if 0 <= row + 1 <= m - 1:  # 向下遍历
                if self.bfs(row+1, col, self.queue[0][2].copy(), self.queue[0][3]):
                    return self.queue[-1][3]
            if 0 <= col - 1 <= n - 1:  # 向左遍历
                if self.bfs(row, col-1, self.queue[0][2].copy(), self.queue[0][3]):
                    return self.queue[-1][3]
            if 0 <= col + 1 <= n - 1:  # 向右遍历
                if self.bfs(row, col+1, self.queue[0][2].copy(), self.queue[0][3]):
                    return self.queue[-1][3]
            del self.queue[0]
        return None

    def bfs(self, i, j, keys, length):
        if self.matrix[i][j] == "3":
            self.queue.append([i, j, keys, length + 1])
        if self.matrix[i][j] == "1" or "2":
            self.queue.append([i, j, keys, length + 1])
        if self.matrix[i][j].islower():
            keys.append(self.matrix[i][j])
            self.queue.append([i, j, keys, length + 1])
        if self.matrix[i][j].isupper():
            if self.matrix[i][j].lower() in keys:
                self.queue.append([i, j, keys, length + 1])

        return False



if __name__ == '__main__':
    '''
    while True:
        try:
            line = list(map(lambda x: int(x), input().split()))
            m, n = line[0], line[1]
            matrix = [['0'] * n for i in range(m)]
            for i in range(m):
                s = input()
                if len(s) != n:
                    break
                for j in range(len(s)):
                    matrix[i][j] = s[j]
            print(matrix)
            print(Solution().findWays(matrix, m, n))
        except:
            break
    '''
    matrix = [['a', '1', '1', '0', '0', '0', '0', '0', '1', '1'],
              ['0', '0', '2', '1', '1', '1', '1', '1', '1', '0'],
              ['1', '1', '1', '0', '1', '0', '0', '0', 'A', '0'],
              ['1', '0', '0', '1', '1', '0', '0', '1', '1', '1'],
              ['1', '0', '0', 'B', '0', '0', '0', '1', '0', '1'],
              ['1', '1', '0', '3', '0', '0', '0', '1', 'b', '1']]

    print(Solution2().findWays(matrix, 6, 10))