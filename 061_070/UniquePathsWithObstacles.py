class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid and not obstacleGrid[0]:
            return 0

        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        ways = [[0] * m for i in range(n)]

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    ways[i][j] = 0
                elif i == 0 and j == 0:
                    ways[i][j] = 1
                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[n - 1][m - 1]


ob = [
  [1, 0]
]
print(Solution().uniquePathsWithObstacles(ob))
