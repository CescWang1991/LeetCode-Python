# 312. Burst Balloons

class Solution:
    # dp[i][j]表示打爆区间[i,j]中的所有气球能得到的最多金币
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        nums.insert(0, 1)
        nums.append(1)
        # 因为dp[i][j]需要依赖于dp[i+1][j]和dp[i][j]，所以我们需要从下到上，从左至右遍历
        for i in reversed(range(n)):
            for j in range(n):
                if i == j:
                    dp[i][j] = nums[i] * nums[i+1] * nums[i+2]
                if i < j:
                    # 对于dp[i][j]，我们需要遍历[i,j]中间的数字k，表示最后一个删除的数字是nums[k]，然后更新dp[i][j]为
                    # dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i] * nums[k+1] * nums[j+2])，表示dp[i][j]
                    # 更新为nums[k]乘以i,j两边的数，再加上[i,k-1]和[k+1,j]对应的dp。
                    for k in range(i, j+1):
                        if k == i:
                            dp[i][j] = max(dp[i][j], dp[i+1][j] + nums[i] * nums[k+1] * nums[j+2])
                        elif k == j:
                            dp[i][j] = max(dp[i][j], dp[i][j-1] + nums[i] * nums[k+1] * nums[j+2])
                        else:
                            dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i] * nums[k+1] * nums[j+2])

        return dp[0][n-1]