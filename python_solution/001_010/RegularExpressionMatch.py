# 010. Regular Expression Matching
# 相似话题：# 044. Wildcard Matching

class Solution:
    # 回溯算法，超时
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 处理特殊情况，p为空时，返回s是否为空
        if not p:
            return not s
        # 第一个字符匹配，因为此时p不为空，所以s也不能为空
        firstMatch = bool(s) and p[0] in (s[0], '.')

        if len(p) >= 2 and p[1] == '*':
            # 第二个字符是*时，他前面的字母可以出现0次，此时只需要直接把*和前面的字符去掉递归即可
            # 或者把str第一个去掉，剩下的部分再与p匹配
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:
            # 与没有*时一样，只要第一个一样，然后去掉首字母后在比较，都相等则匹配
            return firstMatch and self.isMatch(s[1:], p[1:])

class Solution2:
    # Dynamic Programming: dp[i][j]表示s的前i位与p的前j位匹配的结果
    # 第一种情况：s[i-1]是否和p[j-1]相等，或者p[j-1]是否为"."，这时需要考虑dp[i-1][j-1]
    # 第二种情况：p[j-1] = "*"，匹配零个前面的元素(将p[j-2]也一并消去)，这时需要考虑dp[i][j-2]
    # 第三种情况：p[j-1] = "*"，匹配多个前面的元素，这时需要考虑dp[i-1][j]以及s[i-1]是否等于p[j-2]或者p[j-2] = "."
    def isMatch(self, s, p):
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
                    dp[i][j] = dp[i][j - 2] if p[j - 1] == "*" else False
                elif j == 0:
                    dp[i][j] = False
                else:
                    dp[i][j] = (dp[i-1][j-1] and p[j-1] in (s[i-1], ".")) or \
                               (dp[i][j-2] and p[j-1] == "*") or \
                               (dp[i-1][j] and p[j-1] == "*" and (s[i-1] == p[j-2] or p[j-2] == "."))
        return dp[m-1][n-1]