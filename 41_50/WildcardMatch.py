class Solution:
    # Dynamic Programming
    def isMatchWithDp(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = 1 if not s else len(s) + 1
        n = 1 if not p else len(p) + 1

        dp = [([False] * n) for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and p[j-1] == "*"
                elif j == 0:
                    dp[i][j] = False
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] in (s[i-1], "?", "*") or (dp[i][j-1] and p[j-1] == "*") or (dp[i-1][j] and p[j-1] == "*")

        return dp

    # Backtracking
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        firstMatch = bool(s) and p[0] in (s[0], "?", "*")
        sRes = [] if len(s) == 1 else s[1:]
        pRes = [] if len(p) == 1 else p[1:]

        if p[0] == "*":
            return self.isMatch(s, pRes) or (firstMatch and self.isMatch(sRes, p))
        else:
            return firstMatch and self.isMatch(sRes, pRes)


print(Solution().isMatchWithDp("aa", "*"))