# 303. Range Sum Query - Immutable

class NumArray:
    # dp[i]表示0到i-1位的数之和，这里设dp[0]是为了应对i=0的情况
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.dp = [0] * (n + 1)
        for i in range(n):
            self.dp[i+1] = self.dp[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]

# 304. Range Sum Query 2D - Immutable

class NumMatrix:
    # dp[i][j]表示右上角为[i-1, j-1]的点组成的矩形的总和
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        self.dp = [[0] * (m + 1) for i in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] - self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # (row2, col2) - (row2, col1-1) - (row1-1, col2) + (row1-1, col1-1)
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

# 307. Range Sum Query - Mutable

class NumArrayMutable:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0] * (len(nums) + 1)
        self.bits = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i+1]
        j = i + 1
        while j < len(self.nums):
            self.bits[j] += diff
            j += j & (-j)
        self.nums[i+1] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumPrefix(j+1) - self.sumPrefix(i)
    # 表示数组前i为元素的和
    def sumPrefix(self, i):
        res = 0
        while i > 0:
            res += self.bits[i]
            i -= i & (-i)
        return res

# 308. Range Sum Query 2D - Mutable

# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1)
# and lower right corner (row2, col2).

# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

class NumMatrix2:
    # 与308思路一样，利用树状数组，把问题放到二维
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = [[0] * (n + 1) for i in range(m + 1)]
        self.bits = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, i, j, val):
        diff = val - self.matrix[i+1][j+1]
        i, j = i + 1, j + 1
        self.matrix[i][j] = val
        while i < len(self.matrix):
            while j < len(self.matrix[0]):
                self.bits[i][j] += diff
                i += i & (-i)
                j += j & (-j)

    def sumRegion(self, row1, col1, row2, col2):
        return self.getSum(row2+1, col2+1) - self.getSum(row2+1, col1) - self.getSum(row1, col2+1) + self.getSum(row1, col1)

    def getSum(self, i, j):
        res = 0
        while i > 0:
            while j > 0:
                res += self.bits[i][j]
                i -= i & (-i)
                j -= j & (-j)
        return res