# 把数字翻译成字符串

# 给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成“a”，1翻译成“b”，……，11翻译成“1”,……，25翻译成“z”。
# 一个数字可能有多个翻译。例如：12258有5种不同的翻译，分别是“bccfi”、“bwfi”、“bczi”、“mcfi”和“mzi”。请编程实
# 现一个函数，用来计算一个数字有多少种不同的翻译方法。

class Solution:
    def getTranslationCount(self, num):
        """
        :type num: str
        :rtype: int
        """
        if not num:
            return 0
        dp = [0] * len(num)
        dp[0] = 1
        dp[1] = 2 if 10 <= int(num[:2]) <= 25 else 1
        for i in range(2, len(num)):
            if 10 <= int(num[i-1:i+1]) <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[len(num) - 1]

print(Solution().getTranslationCount("12258"))