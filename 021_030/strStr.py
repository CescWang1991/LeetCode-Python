# 028. Implement strStr()

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        if m < n:
            return -1

        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1

haystack = "hello"
needle = "et"
print(Solution().strStr(haystack, needle))