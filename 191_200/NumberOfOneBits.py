# 191. Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = list('{:b}'.format(n))
        return b.count('1')


print(Solution().hammingWeight(5345))