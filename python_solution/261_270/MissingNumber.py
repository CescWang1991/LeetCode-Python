# 268. Missing Number

class Solution:
    # 参见#136 Single Number，nums中的元素在nums和0-n中出现两次，只有缺失元素出现一次
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        for i in range(n):
            res ^= (i + 1) ^ nums[i]
        return res