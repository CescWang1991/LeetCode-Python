# 258. Add Digits

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        # 公式解，num每加一，结果在1~9的循环队列
        return (num-1) % 9 + 1