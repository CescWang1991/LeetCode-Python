# 005. Longest Palindromic Substring

class Solution:
    # dp[i][j]表示第i位到第j位的子串是否为回文串，对于dp[i][i]，设为True，dp[i][j]如果长度大于2，dp[i][j]依赖于
    # dp[i+1][j-1] && s[i] == s[j]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        res = ""
        dp = [[False] * len(s) for i in range(len(s))]
        # n为s的长度，最长子串为dp[0][n-1]，我们行从下往上，列从左往右遍历。
        for i in reversed(range(len(s))):
            for j in range(len(s)):
                if i == j:      # 单个字符，即s[i]
                    dp[i][j] = True
                elif j - i == 1:    # 两个字符，返回s[i] == s[j]
                    dp[i][j] = s[i] == s[j]
                elif j - i > 1:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and len(res) < j - i + 1:
                    res = s[i:j+1]
        return res