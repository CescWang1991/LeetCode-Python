# 130. Surrounded Regions

class Solution:
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

board = [
     ["O", "O", "O", "O", "X", "X"],
     ["O", "O", "O", "O", "O", "O"],
     ["O", "X", "O", "X", "O", "O"],
     ["O", "X", "O", "O", "X", "O"],
     ["O", "X", "O", "X", "O", "O"],
     ["O", "X", "O", "O", "O", "O"]
]
Solution().solve(board)
for line in board:
    print(line)