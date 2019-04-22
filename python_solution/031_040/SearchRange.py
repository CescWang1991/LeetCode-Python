# 034. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        if not nums:
            return result

        index = -1
        l = 0
        h = len(nums) - 1
        while l <= h:
            m = int((l + h)/2)
            if nums[m] == target:
                index = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1

        if index == -1:
            return result
        else:
            ls = index
            while ls >= 0 and nums[ls] == target:
                result[0] = ls
                ls -= 1
            rs = index
            while rs < len(nums) and nums[rs] == target:
                result[1] = rs
                rs += 1

        return result