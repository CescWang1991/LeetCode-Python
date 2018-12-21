# 089. Gray Code

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n <= 0:
            return [0]

        result = []
        rest = self.grayCode(n - 1)                     # 递归返回除最高位的所有结果
        if rest:
            for num in rest:
                result.append(num)                      # 最高位为0的情况
            for num in reversed(rest):                  # 注意将rest逆序，交界处最高位不同，其余位均相同
                result.append(int(pow(2, n-1)) + num)   # 最高位为1的情况

        return result