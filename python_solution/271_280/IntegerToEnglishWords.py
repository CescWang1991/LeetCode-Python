# 273. Integer to English Words

class Solution:
    def __init__(self):
        self.num1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.num2 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                     "Eighteen", "Nineteen"]
        self.tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        if num == 0:
            return "Zero"
        if num >= 1000000000:
            res += self.threeNumbers(num//1000000000) + " Billion"
            num = num % 1000000000
        if num >= 1000000:
            if res:     # 注意在前面右数字时加空格，否则就是开头，不需要空格
                res += " "
            res += self.threeNumbers(num // 1000000) + " Million"
            num = num % 1000000
        if num >= 1000:
            if res:
                res += " "
            res += self.threeNumbers(num // 1000) + " Thousand"
            num = num % 1000
        if num >= 1:
            if res:
                res += " "
            res += self.threeNumbers(num)

        return res

    # 输出最多三个数字的英文读法
    def threeNumbers(self, num):
        res = ""
        hundred = num // 100
        if hundred > 0:
            res += self.num1[hundred-1] + " Hundred"
        num = num % 100
        decade = num // 10
        if decade > 1:
            if res:
                res += " "
            res += self.tens[decade-2]
        elif decade == 1:
            num = num % 10
            if res:
                res += " "
            res += self.num2[num]
            return res
        num = num % 10
        if num > 0:
            if res:
                res += " "
            res += self.num1[num-1]
        return res