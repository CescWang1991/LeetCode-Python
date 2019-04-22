# 和为s的数字

# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积
# 最小的。

class Solution:
    def findNumWithSum(self, nums, s):
        if not nums:
            return None
        i, j = 0, len(nums) - 1
        minVal = -float('inf')
        while i < j:
            if nums[i] + nums[j] == s:
                minVal = min(minVal, nums[i] * nums[j])
                i += 1
                j -= 1
            elif nums[i] + nums[j] < s:
                i += 1
            else:
                j -= 1

        return minVal