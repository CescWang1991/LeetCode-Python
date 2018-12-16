# 007. Reverse Integer

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = list(str(x))
        if res[0] == "-":   # 如果为负数，则1到len(res)-1反转
            mid = len(res) // 2
            for i in range(1, mid+1):
                res[i], res[len(res) - i] = res[len(res) - i], res[i]
        else:               # 正数，则0到len(res)-1反转
            mid = (len(res) - 1) // 2
            for i in range(mid+1):
                res[i], res[len(res)-1-i] = res[len(res)-1-i], res[i]
        res = int("".join(res))
        if res > 2 ** 31 - 1 or res < - (2 ** 31):   # 判断res是否在int范围内
            res = 0
        return res