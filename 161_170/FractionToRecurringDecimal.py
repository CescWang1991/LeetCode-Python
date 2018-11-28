# 166. Fraction to Recurring Decimal


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 判断结果是正还是负
        positive = True if (numerator >= 0 and denominator > 0) or (numerator <= 0 and denominator < 0) else False
        numerator = abs(numerator)
        denominator = abs(denominator)

        integer = str(numerator//denominator) if positive else "-"+str(numerator//denominator)
        decimal = []

        numerator = numerator % denominator
        if numerator == 0:
            return integer
        # 对于小数部分，我们每次作除，取整数部分加入decimal，然后余数*10，作为下一位小数的被除数。
        # 我们建立一个hash表，key为被除数，value为小数的位数，当key重复时，就表示小数部分开始循环。
        dict = {}
        while numerator != 0:
            if numerator not in dict.keys():
                dict[numerator] = len(decimal)
            else:
                decimal.insert(dict[numerator], "(")
                decimal.append(")")
                break
            decimal.append(str(numerator*10//denominator))
            numerator = numerator * 10 % denominator

        return integer+"."+"".join(decimal)