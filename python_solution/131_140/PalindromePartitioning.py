# 131. Palindrome Partitioning
# 132. Palindrome Partitioning II
# 解法：https://blog.csdn.net/jin_kwok/article/details/51423222
# 参考：https://blog.csdn.net/yutianzuijin/article/details/16850031

class Solution:
    # Backtracking: 从头开始遍历，如果s[:i+1]是Palindrome，那么我们在res中添加[s[:i+1] + self.partition(s[i+1:])]
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]

        if len(s) == 1:
            return [[s]]

        res = []
        n = len(s)
        i = 0
        while i < n:
            if self.isValid(s[:i+1]):
                post = self.partition(s[i+1:])
                if post:
                    for list in post:
                        res.append([s[:i+1]] + list)
            i += 1

        return res

    def isValid(self, s):
        if not s:
            return True

        n = len(s)
        lo = 0
        hi = n - 1
        valid = True
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1

        return valid

    # dp[i][j]表示是s[i:j+1]是否为palindrome
    # cut[i]表示第i个字符到最后一个字符所构成的子串的最小分割次数
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        dp = [[0] * n for i in range(n)]
        cut = [float('Inf')] * (n+1)
        cut[n] = -1
        # 从最后一行开始遍历
        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    # 如果第i位到第j位为palindrome，则最小cut[i]为当前cut[i]与cut[j+1]+1的最小值；
                    cut[i] = min(cut[i], 1 + cut[j+1])

        return cut[0]