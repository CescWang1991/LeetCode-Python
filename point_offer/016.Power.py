# 数值的整数次方

# 实现函数double Power(double base, int exponent)，求base的exponent次方、不得使用库函数，同时不需要考虑大数问题。

class Solution:
    def power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == -1:
            return 1/base
        if exponent == 1:
            return base
        if base == 0 and exponent < 0:
            return 0.0
        if exponent % 2 == 1:
            return self.power(base, exponent//2) * self.power(base, exponent//2) * base
        else:
            return self.power(base, exponent // 2) * self.power(base, exponent // 2)
