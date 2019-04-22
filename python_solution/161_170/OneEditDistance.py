# 161. One Edit Distance

# Given two strings S and T, determine if they are both one edit distance apart.

class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return not t or len(t) == 1
        if len(s) == len(t):        # 替换
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
        elif len(s) - len(t) == 1:  # t中插入
            for i in range(len(t)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
        elif len(t) - len(s) == 1:  # s中插入
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
        else:
            return False