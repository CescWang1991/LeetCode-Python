# 076. Minimum Window Substring

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""

        dict = {}  # 建立子串的hash表
        for c in t:
            if not dict.get(c):
                dict[c] = 1
        min = ""
        a, b = 0, 0
        while b < len(s):
            if a == b:
                if dict.get(s[a]) == None:
                    a += 1
                    b += 1
                else:
                    dict[s[a]] -= 1
                    b += 1
            else:
                if dict.get(s[b]) == None:
                    b += 1
                else:
                    dict[s[b]] -= 1
                if self.comp(dict.values()):    # dict中的values都小于等于0，则s[a:b+1]包含t中所有字符
                    if not min or b-a+1 < len(min):
                        min = s[a:b+1]
                    b += 1
                    a = b
                else:
                    b+= 1

        return min

    def comp(self, values):
        for v in values:
            if v > 0:
                return False
        return True