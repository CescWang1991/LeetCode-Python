# 168. Excel Sheet Column Title


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

print(Solution().convertToTitle(701))