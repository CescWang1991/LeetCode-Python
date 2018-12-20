# 060. Permutation Sequence

import math

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        output = []
        nums = []
        for i in range(n):
            nums.append(i + 1)

        if k > math.factorial(n):       # k大于n!，超出返回
            return None
        for i in reversed(range(n)):    # 从最高位开始寻找k所在的区间，每一个元素占据(n-1)!个空间，以此类推
            # 例如n = 4，则1为1-6，2为7-12，3为13-18，4为19-24
            pos = (k - 1) // math.factorial(i)  # 这里-1使k从0开始
            num = nums[pos]
            k -= pos * math.factorial(i)
            nums.remove(num)
            output.append(num)

            return output
