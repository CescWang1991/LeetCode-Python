# 172. Factorial Trailing Zeroes
# 要求末尾有多少个零，则该数应为x*10^k 的形式等于x*（2^k *5^k）
# 也就是求该数分解质因子后有几个5就行，：如1*2*3*4*5=1*2*3*2*2*5（里面有一个5）所以结果为1个0

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n >= 1:
            n //= 5
            total += n
        return total