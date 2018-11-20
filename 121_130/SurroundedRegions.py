# 130. Surrounded Regions

class Solution:
    # 解法一：运用DFS方法
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board[0])
        n = len(board)
        # 扫面矩阵的四条边，如果有O，则用DFS遍历，将所有连着的O都变成另一个字符，比如$，这样剩下的O都是被包围的，然后将
        # 这些O变成X，把$变回O就行了。
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and self.isBorder([i, j], m, n):
                    self.dfsBroad(board, i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "$":
                    board[i][j] = "O"

    def dfsBroad(self, board, i, j):
        m = len(board[0])
        n = len(board)
        board[i][j] = "$"
        # 向左DFS
        if j >= 1 and board[i][j-1] == "O":
            self.dfsBroad(board, i, j-1)
        # 向右DFS
        if j <= m-2 and board[i][j+1] == "O":
            self.dfsBroad(board, i, j+1)
        # 向上DFS
        if i >= 1 and board[i-1][j] == "O":
            self.dfsBroad(board, i-1, j)
        # 向下DFS
        if i <= n-2 and board[i+1][j] == "O":
            self.dfsBroad(board, i+1, j)

    def isBorder(self, pos, m, n):
        if pos[0] == 0 or pos[0] == n-1 or pos[1] == 0 or pos[1] == m-1:
            return True
        else:
            return False

    # 解法二：运用并查集方法
    def solveUnionFind(self, board):
        if not board:
            return
        m = len(board[0])
        n = len(board)
        # 建立字典，将"O"节点的位置设为key放入字典中
        dict = {}
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    dict[(i, j)] = 0

        for i in range(n):
            for j in range(m):
                if (i, j) in dict.keys() and self.isBorder([i, j], m, n):
                    del dict[(i, j)]
                    self.dfs((i, j), dict)

        for pos in dict.keys():
            board[pos[0]][pos[1]] = "X"

    def dfs(self, pos, dict):
        i, j = pos[0], pos[1]
        # 向上遍历
        upper = (i - 1, j)
        if dict.get(upper) == 0:
            del dict[upper]
            self.dfs(upper, dict)
        # 向下遍历
        lower = (i + 1, j)
        if dict.get(lower) == 0:
            del dict[lower]
            self.dfs(lower, dict)
        # 向左遍历
        left = (i, j - 1)
        if dict.get(left) == 0:
            del dict[left]
            self.dfs(left, dict)
        # 向右遍历
        right = (i, j + 1)
        if dict.get(right) == 0:
            del dict[right]
            self.dfs(right, dict)


board = [
     ["O", "O", "O", "O", "X", "X"],
     ["O", "O", "O", "O", "O", "O"],
     ["O", "X", "O", "X", "O", "O"],
     ["O", "X", "O", "O", "X", "O"],
     ["O", "X", "O", "X", "O", "O"],
     ["O", "X", "O", "O", "O", "O"]
]
Solution().solveUnionFind(board)
for line in board:
    print(line)