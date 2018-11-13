# 74. Search Matrix
# 用二分法先查询target在第一列(matrix[i][0])中的位置，然后在相应的排中搜索target是否存在于matrix[i][j]

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        if not matrix[0]:
            return False

        numRow = len(matrix)
        numCol = len(matrix[0])
        targetRow = 0

        for row in range(numRow-1):
            if target >= matrix[row][0] and target < matrix[row+1][0]:
                targetRow = row
                break
            elif target >= matrix[numRow-1][0]:
                targetRow = numRow - 1

        for col in range(numCol):
            if target == matrix[targetRow][col]:
                return True

        if target != matrix[targetRow][numCol - 1]:
            return False

    def binarySearchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        if not matrix[0]:
            return False

        m = len(matrix[0])
        n = len(matrix)
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target:
                lo = mid + 1
            else:
                hi = mid - 1

        row = lo - 1
        if row < 0:
            return False

        lo = 0
        hi = m - 1
        col = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                col = mid
                break
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return col >= 0


input = [
  [1]
]
target = 1
print(Solution().binarySearchMatrix(input, target))