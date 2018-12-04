# 202. Happy Number
# 建立hash表，将数字平方和不为1的数加入hash表。如果循环后的数在hash表中，则返回False。

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = {}
        while True:
            if self.digitSum(n) == 1:
                return True
            n = self.digitSum(n)
            if not dict.get(n):
                dict[n] = 1
            else:
                return False

    def digitSum(self, n):
        if n == 0:
            return 0
        digt = n % 10
        return digt * digt + self.digitSum(n//10)

print(Solution().isHappy(68))