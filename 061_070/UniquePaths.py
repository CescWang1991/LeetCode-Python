# 062. Unique Path
# 063. Unique Paths II

class Solution:
    # dp方法，由于dp[i][j]值依赖于dp[i-1][j]和dp[i][j-1]，所以可以将空间压缩至一维。
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways = [0] * n
        ways[0] = 1
        for i in range(m):
            for j in range(1, n):
                ways[j] += ways[j-1]
        return ways[n-1]

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