# 233. Number of Digit One

class Solution:
    # 运用递归方法，将数字从最高位开始拆解。
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 9:
            return 1

        count = 0
        # 例如2332，我们将他拆成2000与332，先计算1-2000有都多少个1，设当前数字最高位位n(这里为4)
        s = str(n)
        n = len(s)
        # 例如1332，最高位为1，千位有332+1个1(1000-1332的个数)
        if s[0] == "1":
            count += 1 + int("".join(s[1:]))
        # 例如2332，我们将他拆成2000与332，先计算1-2000有都多少个1，因为最高位不为1，则千位有10**(n-1)个1 (1000)
        else:
            count += 10**(n-1)
        # 百、十、个位分别有2 * 10**(n-2)个1(200)
        count += int(s[0]) * (n-1) * 10**(n-2)
        # 最后递归调用算出332的1个数
        return count + self.countDigitOne(int("".join(s[1:])))