# 118. 杨辉三角形
# 119. 杨辉三角形 II

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows <= 0:
            return res

        curr = 0
        while curr < numRows:
            row = [1] * (curr + 1)
            if curr >= 2:
                for i in range(len(row)):
                    if 0 < i < len(row) - 1:
                        row[i] = res[curr-1][i-1] + res[curr-1][i]
            res.append(row)
            curr += 1

        return res


    def getRow(self, rowIndex):
        # 本质上是二维的动态规划，因为dp[i][j]只依赖于dp[i-1][j-1]和dp[i-1][j]，我们可以将它压缩到一维
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(rowIndex+1):
            res.append(1)
            for j in reversed(range(1, i)):     # 注意要从后往前遍历
                res[j] = res[j] + res[j-1]

        return res