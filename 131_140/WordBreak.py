# 139. Word Break
# 140. Word Break II

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False

        length = len(s)

        # dp(n)代表长度为n的单词是否可分，如果可分，则最后长度为i的单词出现在dict中，同时dp(n-i) = True
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(length):
            for j in reversed(range(i+1)):
                #从长度为i的单词末尾向前寻找出现在dict中的单词
                sub = s[j:i+1]
                if sub in wordDict and dp[j]:
                    dp[i+1] = True
                    break

        return dp

    # Backtracking方法：Leetcode超时
    def wordSplit(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []

        dict = {}
        for word in wordDict:
            if dict.get(word):
                dict[word] += 1
            else:
                dict[word] = 1

        res = []
        if dict.get(s):
            res.append(s)
        for i in range(len(s)):
            if dict.get(s[:i+1]):
                post = self.wordSplit(s[i+1:], wordDict)
                if post:
                    for str in post:
                        res.append(s[:i+1]+" "+str)

        return res

    # DP+DFS方法：LeetCode超时
    def wordBreakDp(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []

        n = len(s)
        # dp[i]记录了s的前i位的workBreak解的最后一个单词的集合
        dp = []
        dp.append([])

        for i in range(1, n+1):
            first = s[:i]
            dp.append([])
            for length in range(i):
                if first[i-1-length:] in wordDict:
                    dp[i].append(first[i-1-length:])
        return self.dfs(s, dp)


    def dfs(self, s, dp):
        if not s:
            return []

        res = []
        if dp[len(s)]:
            for word in dp[len(s)]:
                if word == s:
                    res.append(word)
                else:
                    prev = self.dfs(s[:(len(s) - len(word))], dp)
                    if prev:
                        for str in prev:
                            res.append(str+" "+word)

        return res