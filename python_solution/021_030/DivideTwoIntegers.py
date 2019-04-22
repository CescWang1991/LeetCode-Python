# 029. Divide Two Integers

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        coef = 1 if (dividend >= 0)^(divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        # 寻找倍数的上界，为2, 4, 8, 16...即dividend在2**(n-1)与2**n之间
        quot = 1
        while divisor < dividend:
            divisor <<= 1       # 左移一位，表示乘2
            quot <<= 1
        # 判断溢出情况
        if quot >= 2**31 and coef == 1:
            return 2**31 - 1
        if divisor == dividend:
            return quot * coef
        # 此时dividend在quot/2和quot倍数之间，用二分法找到dividend所在的倍数区间
        lo, hi = quot >> 1, quot
        l, r = divisor >> 1, divisor
        while hi - lo > 1:
            mid = (lo + hi) >> 1
            half = (l + r) >> 1
            if half == dividend:
                return mid * coef
            elif half > dividend:
                hi = mid
                r = half
            else:
                lo = mid
                l = half
        return lo * coef