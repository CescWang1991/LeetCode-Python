# 64. Minimum path sum
class Solution:
    # DP in O(m*n)
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        sums = [[0 for i in range(m)] for j in range(n)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if j == n-1 and i == m-1:
                    sums[j][i] = grid[j][i]
                elif j == n-1:
                    sums[j][i] = grid[j][i] + sums[j][i+1]
                elif i == m - 1:
                    sums[j][i] = grid[j][i] + sums[j + 1][i]
                else:
                    sums[j][i] = min(grid[j][i]+sums[j+1][i], grid[j][i]+sums[j][i+1])

        return sums[0][0]

    # 优化到用O(n)的空间复杂度
    # dp[i][j]依赖dp[i][j-1], dp[i-1][j]，那么我们在循环时，只需要用到dp[j-1]与dp[j]，再更新dp[j]
    def pathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(grid)
        dp[0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i] = dp[i - 1] + grid[i][0]
        for j in range(1, len(grid[0])):
            for i in range(len(grid)):
                dp[i] = min(dp[i], dp[i - 1]) + grid[i][j] if i > 0 else dp[i] + grid[i][j]
        return dp
