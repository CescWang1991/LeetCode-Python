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


input = [[1], [3], [5]]
target = 3
print(Solution().searchMatrix(input, target))