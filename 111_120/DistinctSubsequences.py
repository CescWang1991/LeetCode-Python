# 115. Distinct Subsequences

class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        # Dynamic Programming: dp[i][j]表示t[:j+1]在s[:i+1]中的字串数
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1 if s[0] == t[0] else 0

        for i in range(m):
            for j in range(n):
                if i < j:
                    dp[i][j] = 0
                elif i == j and i != 0:
                    dp[i][j] = dp[i-1][j-1] if s[i] == t[j] else 0
                elif i > j:
                    if j == 0:
                        dp[i][j] = dp[i-1][j] + 1 if s[i] == t[j] else dp[i-1][j]
                    else:
                        # 如果i>j并且j>0: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                        # 当s[i] = t[j]时，前一项表示s[i]保留时的个数，后一项表示s[i]消除时的个数
                        # 当s[i] != t[j]时，dp[i][j] = dp[i-1][j]
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] == t[j] else dp[i-1][j]

        return dp[m-1][n-1]