# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n,打印出s的所有可能的值出现的概率。

class Solution:
    # 动态规划：dp[i][j]表示i+1个骰子掷出j+1点的概率
    # 状态方程：dp[i][j] += dp[i-1][j-k-1] for k in range(6)
    def findSum(self, n: int, s: int) -> float:
        if s > 6 * n or s < n:
            return 0
        if n == 1 and 1 <= s <= 6:
            return 1.0 / 6
        dp = [[0.0] * s for i in range(n)]
        for j in range(6):
            dp[0][j] = 1.0 / 6
        for i in range(1, n):
            for j in range(s):
                for k in range(6):
                    if j > k:
                        dp[i][j] += dp[i-1][j-k-1] / 6

        return dp[n-1][s-1]