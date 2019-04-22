# 054. Spiral Matrix
# 059. Spiral Matrix II

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            spiral += matrix[0]
        elif len(matrix[0]) == 1:
            for row in range(len(matrix)):
                spiral.append(matrix[row][0])
        else:
            # first row
            spiral += matrix[0]
            matrix.remove(matrix[0])
            # last column
            col = len(matrix[0]) - 1
            for row in range(0, len(matrix)):
                spiral.append(matrix[row][col])
                matrix[row].remove(matrix[row][col])
            # last row
            spiral += reversed(matrix[len(matrix) - 1])
            matrix.remove(matrix[len(matrix) - 1])
            # first column
            if len(matrix) != 0:
                if matrix[0]:
                    for row in reversed(range(0, len(matrix))):
                        spiral.append(matrix[row][0])
                        matrix[row].remove(matrix[row][0])
            if len(matrix) != 0:
                if matrix[0]:
                    spiral += self.spiralOrder(matrix)

        return spiral

class Solution2:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.generateWithStart(1, n)

    # 递归调用，s表示在当前层左上角开始的值
    def generateWithStart(self, s, n):
        if n == 0:
            return []
        if n == 1:
            return [[s]]
        ans = []
        # 第一行
        ans.append(list(range(s, s+n)))
        s = s + n
        # 最右列
        for i in range(s, s+n-2):
            ans.append([i])
        s = s+n-2
        # 最后一行
        ans.append(list(reversed(range(s, s+n))))
        s = s + n -1 + n - 1    # 直接将s指向内圈矩阵最开始的s
        mid = self.generateWithStart(s, n-2)    # 递归给出内圈的矩阵
        # 左列以及中圈
        if mid:
            for i in range(len(mid)):
                ans[i+1] = [s-i-1] + mid[i] + ans[i+1]
        return ans