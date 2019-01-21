# 311. Sparse Matrix Multiplication

# Given two sparse matrices A and B, return the result of AB.
# You may assume that A's column number is equal to B's row number.
#
# Example:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]

#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

# C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][k]*B[k][j]

class Solution:
    # 稀疏矩阵的特点是矩阵中绝大多数的元素为0，而相乘的结果是还应该是稀疏矩阵，即还是大多数元素为0
    def multiply(self, A, B):
        """
        :type A: list[list[int]]
        :param B: list[list[int]]
        :rtype: list[list[int]]
        """
        n = len(A)
        m = len(A[0])
        p = len(B[0])
        C = [[0] * p for i in range(n)]

        for i in range(n):
            for k in range(m):
                # 我们首先遍历A数组，要确保A[i][k]不为0，才继续计算
                if A[i][k] != 0:
                    for j in range(p):
                        # 然后我们遍历B矩阵的第k行，如果B[K][J]不为0，我们累加
                        if B[k][j] != 0:
                            C[i][j] += A[i][k] * B[k][j]
        return C