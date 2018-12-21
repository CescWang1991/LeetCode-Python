# 080. Remove Duplicates from Sorted Array II
# 参见 # 026. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        total = 1
        num = 1
        pointer = 1
        while pointer < len(nums):
            if nums[pointer-1] == nums[pointer]:
                num += 1            # 计数当前遍历到的元素的个数
                if num <= 2:
                    total += 1
                    pointer += 1
                else:
                    nums.pop(pointer)   # 加入计数大于2，将其pop
            else:                       # 不同时，重置num
                num = 1
                total += 1
                pointer += 1

        return total