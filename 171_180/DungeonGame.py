# 174. Dungeon Game
# Dynamic Programming:
# 从后往前遍历，从右下角出发，dp[i][j]表示到达[i,j]时的最小HP值，dp[i][j]始终大于等于1
# 如果dungeon[i][j]为负，则dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]，为右边和下边hp的最小值 - dungeon[i][j]
# 如果dungeon[i][j]为正，当dp[i][j]为负时，将其设为1。

class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 1

        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0] * n for i in range(m)]
        dp[m-1][n-1] = -dungeon[m-1][n-1]+1 if dungeon[m-1][n-1] < 0 else 1

        for i in reversed(range(m - 1)):
            dp[i][n-1] = dp[i+1][n-1] - dungeon[i][n-1]
            dp[i][n-1] = 1 if dp[i][n-1] <= 0 else dp[i][n-1]

        for j in reversed(range(n - 1)):
            dp[m-1][j] = dp[m-1][j+1] - dungeon[m-1][j]
            dp[m-1][j] = 1 if dp[m-1][j] <= 0 else dp[m-1][j]

        for i in reversed(range(m - 1)):
            for j in reversed(range(n - 1)):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = 1 if dp[i][j] <= 0 else dp[i][j]

        return dp[0][0]