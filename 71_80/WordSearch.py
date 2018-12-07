# 79. Word Search

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True

        return False

    def dfs(self, board, word, x, y):
        if not word or board[x][y] == "#":
            return False

        letter = word[0]
        if len(word) == 1 and letter == board[x][y]:
            return True
        if letter != board[x][y]:
            return False
        row = len(board)
        col = len(board[0])

        board[x][y] = "#"
        left = self.dfs(board, word[1:], x, y-1) if y > 0 else False
        right = self.dfs(board, word[1:], x, y+1) if y < col-1 else False
        upper = self.dfs(board, word[1:], x-1, y) if x > 0 else False
        lower = self.dfs(board, word[1:], x+1, y) if x < row-1 else False
        board[x][y] = letter

        return left or right or upper or lower