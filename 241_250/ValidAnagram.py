# 242. Valid Anagram

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def buildDict(s):
            dict = {}
            for c in s:
                if not dict.get(c):
                    dict[c] = 1
                else:
                    dict[c] += 1
            return dict

        dict_s = buildDict(s)
        dict_t = buildDict(t)

        return dict_s == dict_t