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


print(Solution().spiralOrder([[1, 2], [3, 4]]))
