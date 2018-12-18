# 026. Remove Duplicates from Sorted Array
# 027. Remove Element

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        while index < len(nums):
            if nums[index-1] == nums[index]:
                del nums[index]
            else:
                index += 1

        return len(nums)


    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
            else:
                index += 1

        return len(nums)