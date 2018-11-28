# 169. Majority Element

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if not dict.get(num):
                dict[num] = 1
            else:
                dict[num] += 1
            if dict[num] > len(nums) // 2:
                return num