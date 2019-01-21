# 319. Bulb Switcher

class Solution:
    # 对于第n个灯泡，只有当次数是n的因子的之后，才能改变灯泡的状态
    # 所有平方数都有这么一个相等的因数对，即所有平方数的灯泡都将会是点亮的状态。
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 简化为了求1到n之间完全平方数的个数
        res = 1
        while res * res <= n:
            res += 1
        return res - 1