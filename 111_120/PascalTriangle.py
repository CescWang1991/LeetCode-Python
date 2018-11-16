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
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(rowIndex+1):
            res.append(1)
            for j in reversed(range(1, i)):
                res[j] = res[j] + res[j-1]

        return res