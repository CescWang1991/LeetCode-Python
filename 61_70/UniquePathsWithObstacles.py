class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        ways = [0] * n
        for i in range(n):
            ways[i] = [0] * m
        for i in range(m):
            for j in range(n):
                if obstacleGrid[j][i] == 1:
                    ways[j][i] = 0
                elif i==0 and j==0:
                    ways[j][i] = 1
                else:
                    ways[j][i] = ways[j-1][i] + ways[j][i-1]

        return ways[n-1][m-1]


ob = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
print(Solution().uniquePathsWithObstacles(ob))
