# 073. Set Zeroes

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        numRow = len(matrix)
        numCol = len(matrix[0])
        zeroCols = []
        for row in range(numRow):   # 遍历行，找寻有0的行，记录0所在的列
            if matrix[row].count(0) > 0:
                for col in range(numCol):
                    if matrix[row][col] == 0:
                        zeroCols.append(col)
                    matrix[row][col] = 0

        for col in zeroCols:        # 将0所在的列都置为0
            for row in range(numRow):
                matrix[row][col] = 0

        return matrix