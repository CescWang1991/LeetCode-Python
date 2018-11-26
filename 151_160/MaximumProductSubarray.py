# 152. Maximum Product Subarray
# Dynamic Programming in O(n): 维持一个到当前元素的乘积最大值(max_curr)和最小值(min_curr)
# 状态转移方程:
# max_curr[i] = Max(A[i], max_curr[i-1] * A[i], min_curr * A[i])
# min_curr[i] = Min(A[i], max_curr[i-1] * A[i], min_curr * A[i])
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        n = len(nums)
        maxPro = - float('Inf')
        maxCurr, minCurr = 1, 1
        for i in range(n):
            maxLast = maxCurr
            minLast = minCurr
            maxCurr = max(nums[i], maxLast*nums[i], minLast*nums[i])
            minCurr = min(nums[i], maxLast*nums[i], minLast*nums[i])
            print(nums[i], maxCurr, minCurr)
            maxPro = max(maxPro, maxCurr)

        return maxPro


print(Solution().maxProduct([-4, -3, -2]))