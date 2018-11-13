# 87. Scramble String

class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True


s1 = "ab"
s2 = "ba"
print(Solution().isScramble(s1, s2))