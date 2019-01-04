# 290. Word Pattern

class Solution:
    # 与#205. Isomorphic Strings相似，用双字典来对应pattern与str中对应位置的字符
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(" ")
        p = dict()
        s = dict()
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            if not p.get(pattern[i]) and not s.get(str[i]):
                p[pattern[i]] = str[i]
                s[str[i]] = pattern[i]
            elif p.get(pattern[i]) and s.get(str[i]):
                if p[pattern[i]] == str[i] and s[str[i]] == pattern[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True