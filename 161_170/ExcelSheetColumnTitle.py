# 168. Excel Sheet Column Title
# 171. Excel Number Column Number

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        bit = 0
        title = []
        while n > 0:
            n = n - (26 ** bit)
            remain = n % (26**(bit+1))
            title.append(str(chr((remain // 26**(bit)) + 65)))
            n = n - remain
            bit += 1

        return "".join(reversed(title))


    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        num = 0
        for i in range(length):
            num += (ord(s[length-i-1]) - 64) * (26**i)

        return num

print(Solution().titleToNumber("ZY"))