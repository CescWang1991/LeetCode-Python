# 190. Reverse Bits

class Solution:
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ’{0:032b}’.format(n)将n转化为32位无符号数
        b = list('{:032b}'.format(n))
        for i in range(16):
            b[i], b[31 - i] = b[31 - i], b[i]
        r = int(''.join(b), 2)
        return r