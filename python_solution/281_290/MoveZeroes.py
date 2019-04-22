# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        index = 0
        count = 0       # 用一个count参数记录遍历过的元素个数
        while count < len(nums):
            if nums[index] == 0:
                nums.append(0)
                del nums[index]
            else:
                index += 1
            count += 1
        return