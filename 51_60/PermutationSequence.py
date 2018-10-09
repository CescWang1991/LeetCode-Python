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

        if k > math.factorial(n):
            return None
        else:
            for i in reversed(range(n)):
                pos = (k - 1) // math.factorial(i)
                num = nums[pos]
                k -= pos * math.factorial(i)
                nums.remove(num)
                output.append(num)

            return output


print(Solution().getPermutation(5, 57))
