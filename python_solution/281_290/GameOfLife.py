# 289. Game Of Life

# 状态0： 死细胞转为死细胞
# 状态1： 活细胞转为活细胞
# 状态2： 活细胞转为死细胞
# 状态3： 死细胞转为活细胞

class Solution:
    # 遍历数组，对于每个元素，找寻八个方向的活细胞数目，然后按上述状态方程进行状态更新，然后对于状态1，2，我们可认为是活细胞，
    # count加一，最后将每一状态对2取余
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                count = 0
                count += self.isValid(i - 1, j - 1, board)
                count += self.isValid(i - 1, j, board)
                count += self.isValid(i - 1, j + 1, board)
                count += self.isValid(i, j - 1, board)
                count += self.isValid(i, j + 1, board)
                count += self.isValid(i + 1, j - 1, board)
                count += self.isValid(i + 1, j, board)
                count += self.isValid(i + 1, j + 1, board)
                if board[i][j] == 1 and count < 2:      # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡
                    board[i][j] = 2
                elif board[i][j] == 1 and count > 3:    # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡
                    board[i][j] = 2
                elif board[i][j] == 0 and count == 3:   # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活
                    board[i][j] = 3

        for i in range(self.m):
            for j in range(self.n):
                board[i][j] %= 2

    def isValid(self, x, y, board):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return 0
        else:
            if board[x][y] == 1 or board[x][y] == 2:
                return 1
            else:
                return 0