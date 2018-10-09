class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [([0] * n) for i in range(n)]

        left = 0
        right = n - 1
        up = 0
        down = n - 1
        count = 1


print(Solution().generateMatrix(4))
