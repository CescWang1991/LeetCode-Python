# 051. N-Queens
# 052. N-Queens II
# From: https://www.jianshu.com/p/8f3b8df612ae

class Solution:
    #  回溯算法，对于每一行，试验每一个位置，然后验证是否存在冲突。
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n <= 0:
            return result

        cols = []       # 列数组，每一个位置上的数字代表该index所在列上Q的位置
        self.search(n, cols, result)
        return result

    def search(self, n, cols, result):
        """
        :type n: int
        :type cols: list[int]
        :type result: list[list[str]]
        :return: None
        """
        if len(cols) == n:
            result.append(self.drawBoard(cols))
            return

        for col in range(n):                        # 遍历每一行
            if not self.isValid(cols, col):         # 假如存在冲突，直接跳过
                continue
            self.search(n, cols + [col], result)    # 继续搜索下一列
    # 验证新的一列是否和之前的列存在冲突
    def isValid(self, cols, col):
        currentRowNumber = len(cols)
        for i in range(currentRowNumber):
            # 是否在同一列
            if cols[i] == col:
                return False
            # 左上角至右下角的斜线
            if i - cols[i] == currentRowNumber - col:
                return False
            # 右上角至左下角的斜线
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
