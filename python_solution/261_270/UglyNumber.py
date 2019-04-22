# 263. Ugly Number
# 264. Ugly Number II

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        factors = [2, 3, 5]
        for factor in factors:
            if num % factor == 0:       # 若能整除质因数，且商在[1,2,3,5]中，则直接返回True
                num = num // factor
                if num in factors+[1]:
                    return True
                else:                   # 否则递归返回商是否是ugly number
                    return self.isUgly(num)

        return False

class Solution2:
    # 利用hash table处理#264，Leetcode超时
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dict = {}
        dict[1] = 1
        num = 2
        count = 1
        while True:
            for factor in [2, 3, 5]:
                if num % factor == 0:
                    if dict.get(num // factor):
                        dict[num] = 1
                        count += 1
                        break
            if count == n:
                return num
            num += 1

class Solution3:
    # 原理与# 313类似，用一个idx数组来保存当前的位置，由于三个数固定，可以用三个参数，而不用数组
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = i3 = i5 = 0
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            # 比较对应坐标的丑数与2，3，5的乘积，最小值即为当前坐标的丑数，然后将对应坐标加一。
            res[i] = min(res[i2]*2, res[i3]*3, res[i5]*5)
            if res[i] == res[i2]*2:     # 这里需要用三个if，不能用elif，因为存在重复的值，比如3*2，2*3，需要更新为4，3
                i2 += 1
            if res[i] == res[i3]*3:
                i3 += 1
            if res[i] == res[i5]*5:
                i5 += 1
        return res[n-1]