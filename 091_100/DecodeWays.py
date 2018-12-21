# 091. Decode Ways
# Dynamic Programming: 从后往前遍历,dp[n]表示s[n:]的数量
# 分三种情况讨论：s[n] == "0"; 10 <= s[n:n+2] <= 26; s[n:n+2] > 26
# 这三种情况处理：dp[n] = 0; dp[n] = dp[n+1] + dp[n+2]; dp[n] = dp[n+1]

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1
        dp[n-1] = 1 if s[n-1] != "0" else 0

        for i in reversed(range(n-1)):
            if s[i] != "0" and int(s[i:i+2]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            elif s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

        return dp[0]