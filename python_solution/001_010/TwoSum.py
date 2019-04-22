# 001. Two Sum

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        if not nums:
            return res
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if dict.get(complement):
                return [dict[complement], i]
            dict[nums[i]] = i

        return res