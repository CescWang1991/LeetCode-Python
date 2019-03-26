# 圆圈中最后剩下的数字

# 0，1，...，n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

class Solution:
    def LastNumber(self, n, m):
        if n < 1 or m < 1:
            return -1
        res = 0
        for i in range(2, n+1):
            res = (res+m) % i
        return res

Solution().LastNumber(8, 3)