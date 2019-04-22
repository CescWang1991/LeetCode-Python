# 070. Climbing Stairs

class Solution:
    # 斐波那契数列
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            dp = [0] * n
            dp[0] = 1
            dp[1] = 2
            for i in range(2, n):
                dp[i] = dp[i - 1] + dp[i - 2]

            return dp[n-1]