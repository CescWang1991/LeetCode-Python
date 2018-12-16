class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        numRow = len(matrix)
        numCol = len(matrix[0])
        zeroCols = []
        for row in range(numRow):
            if matrix[row].count(0) > 0:
                for col in range(numCol):
                    if matrix[row][col] == 0:
                        zeroCols.append(col)
                    matrix[row][col] = 0

        for col in zeroCols:
            for row in range(numRow):
                matrix[row][col] = 0

        return matrix


input = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
print(Solution().setZeroes(input))