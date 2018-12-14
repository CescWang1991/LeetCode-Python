# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        # 如果n为2的幂次，其二进制位1(0)_n，则n-1为0(1)_n，它们的与运算结果为0
        return n & (n-1) == 0