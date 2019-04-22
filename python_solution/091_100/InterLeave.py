# 097. Interleaving String
# Dynamic Programming: dp[i][j]表示s1的前i位与s2的前j位能否匹配s3的前i+j位
# dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i-1+j]) || (dp[i][j-1] && s2[j-1] == s3[j-1+i])

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1) + 1
        n = len(s2) + 1
        dp = [[False] * n for i in range(m)]
        dp[0][0] = True

        for i in range(m):
            for j in range(n):
                if i == 0 and j >= 1:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                elif j == 0 and i >= 1:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                elif i >= 1 and j >= 1:
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])

        return dp[m-1][n-1]