# 069. Sqrt(x)

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if 1 <= x <= 3:
            return 1
        base = 1
        while 4 * base * base < x:      # 这样比较我们可以找到base，使得base平方 < x <= (2base)平方
            base *= 2
        if 4 * base * base == x:
            return 2 * base

        lo, hi = base, base * 2
        while lo < hi - 1:          # 如果lo = hi - 1，停止循环，直接返回lo
            mid = (lo + hi) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                hi = mid
            else:
                lo = mid
        return lo