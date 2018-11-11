# 53. Maximum Subarray
# Dynamic Programming in O(n): 从头到尾遍历每一个数组元素，如果前面元素的和为正，则加上本元素的值继续搜索；
# 如果前面元素的和为负，则此元素开始新的和计数。整个过程中要注意更新和的最大值。
# Divide and Conquer in O(nlogn)

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        maxSum = 0
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum
            elif currSum < 0:
                currSum = 0

        return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4,-3]
print(Solution().maxSubArray(nums))