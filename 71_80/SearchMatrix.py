# 74. Search a 2D Matrix
# 240. Search a 2D Matrix II
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

class Solution2:
    # 用二分法搜索，先搜索没行头元素，确定所在的行，具体方法可参考 # 35. Search Insert Position
    # 之后用二分法搜索所在行是否有相同的值。
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

        m = len(matrix[0])
        n = len(matrix)
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] < target:
                lo = mid + 1
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                return True

        row = lo - 1
        if row < 0:
            return False

        lo = 0
        hi = m - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False


class Solution3:
    # 与74一样，用二分法搜索，先搜索没行头元素，确定所在的行。
    # 然后从目标行开始，向上逐行搜索(二分法搜索列)，如果target大于该列最后一个元素，则返回false。
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] < target:
                lo = mid + 1
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                return True
        row = lo - 1
        if row < 0:
            return False

        for i in reversed(range(row+1)):
            if target > matrix[i][-1]:
                return False
            if self.searchCol(matrix[i], target):
                return True

        return False

    def searchCol(self, col, target):
        lo = 0
        hi = len(col) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if col[mid] == target:
                return True
            elif col[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False