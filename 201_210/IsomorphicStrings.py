# 205. Isomorphic Strings
# 建立两个hash表，一个key为s，value为t中对应的字符。

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        n = len(s)
        dict_s = {}
        dict_t = {}
        for i in range(n):
            if not dict_s.get(s[i]) and not dict_t.get(t[i]):
                dict_s[s[i]] = t[i]
                dict_t[t[i]] = s[i]
            else:
                if not dict_s.get(s[i]) or not dict_t.get(t[i]):
                    return False
                if dict_s[s[i]] != t[i] or dict_t[t[i]] != s[i]:
                    return False

        return True

Solution().isIsomorphic("egg", "add")