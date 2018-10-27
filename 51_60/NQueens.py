# Brute force
# From: https://www.jianshu.com/p/8f3b8df612ae

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n <= 0:
            return result

        cols = []
        self.search(n, cols, result)
        return result

    def search(self, n, cols, result):
        if len(cols) == n:
            result.append(self.drawBoard(cols))
            return

        for col in range(n):
            if not self.isValid(cols, col):
                continue
            self.search(n, cols + [col], result)

    def isValid(self, cols, col):
        currentRowNumber = len(cols)
        for i in range(currentRowNumber):
            # same column
            if cols[i] == col:
                return False
            # left-top to right-bottom
            if i - cols[i] == currentRowNumber - col:
                return False
            # right-top to left-bottom
            if i + cols[i] == currentRowNumber + col:
                return False
        return True

    def drawBoard(self, cols):
        board = []
        for i in range(len(cols)):
            line = ""
            for j in range(len(cols)):
                if j == cols[i]:
                    line += "Q"
                else:
                    line += "."
            board.append(line)
        return board


print(Solution().solveNQueens(4))
