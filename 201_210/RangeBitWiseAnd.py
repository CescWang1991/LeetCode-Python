# 201. Range Bit Wise And
# 比较两个数bit的位数，如果位数不同，直接返回0；如果相同，我们把m，n的最高位去掉，递归调用。

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mBit = m.bit_length()
        nBit = n.bit_length()
        if nBit > mBit or m == 0:
            return 0
        # 最高位恒定位1，将它提取出来，和后面位数的结果相加
        return 2**(nBit-1) + self.rangeBitwiseAnd(m-2**(nBit-1), n-2**(nBit-1))