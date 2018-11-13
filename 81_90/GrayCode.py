# 89. Gray Code

class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n <= 0:
            return [0]

        result = []
        rest = self.grayCode(n - 1)
        if rest:
            for num in rest:
                result.append(num)
            for num in reversed(rest):
                result.append(int(pow(2, n-1)) + num)

        return result

print(Solution().grayCode(2))