# 050. Pow(x, n)

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign = 1 if n > 0 else 0    # 判断幂次是否为正
        n = abs(n)
        if n == 0:
            return 1
        if n == 1:
            return x if sign else 1.0/ x
        sqrt = self.myPow(x, n // 2)    # 递归二分返回结果的根
        if n % 2 == 0:      # 判断奇偶情况
            return sqrt * sqrt if sign else 1.0 / (sqrt * sqrt)
        else:
            return sqrt * sqrt * x if sign else 1.0 / (sqrt * sqrt * x)