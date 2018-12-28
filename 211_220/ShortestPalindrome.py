# 214. Shortest Palindrome

class Solution:
    # 先判断整个字符串是否回文，否的话再判断前n-1个子串是否回文，这样依次缩减长度，直到找到一个回文子串就是最大的前缀回文子串．
    # Leetcode测试：119 / 120 个通过测试用例。
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        cut = 0
        for i in reversed(range(len(s))):
            if self.valid(s[:i+1]):
                cut = i+1
                break

        return "".join(reversed(list(s[cut:]))) + s[:cut] + s[cut:]
    # 运用双指针验证
    def validPalindrome(self, s):
        if not s or len(s) == 1:
            return True
        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    def valid(self, s):
        if not s or len(s) == 1:
            return True
        mid = len(s) // 2
        left = s[:mid]
        right = s[len(s)-mid:]
        return "".join(reversed(list(left))) == right

class Solution2:
    #
    # Leetcode通过，112ms
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s + "#" + "".join(reversed(list(s)))
        table = self.kmp(temp)
        return "".join(reversed(list(s[table[len(table) - 1]:]))) + s

    # 构造kmp算法中的pmt(Partial Match Table)数组，即新构造的字符串(s+"#"+s.reverse)前缀集合与后缀集合的交集中最长元素的长度
    def kmp(self, s):
        table = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = table[j-1]
            if s[i] == s[j]:
                j += 1
            table[i] = j
        return table