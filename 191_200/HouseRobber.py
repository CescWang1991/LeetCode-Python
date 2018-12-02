# 198. House Robber
# Dynamic Programming：维持两个数组local和global，分别表示局部最大值(取i位时总量的最大值)以及全局最大值(前i位的最大值)。
# 状态转移方程：local[i] = global[i-2]+nums[i]；global[i] = max(global[i-1], local[i])

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        local = [0] * len(nums)
        globa = [0] * len(nums)

        local[0] = globa[0] = nums[0]

        if len(nums) == 1:
            return globa[0]

        local[1] = nums[1]
        globa[1] = max(local[1], globa[0])

        for i in range(2, len(nums)):
            local[i] = globa[i-2] + nums[i]
            globa[i] = max(globa[i-1], local[i])

        return globa[len(nums)-1]