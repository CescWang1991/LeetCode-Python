# 031. Next Permutation

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first = len(nums) - 1
        # 数组从i开始是降序的
        while first > 0 and nums[first-1] > nums[first]:
            first -= 1
        # 如果给定数组是降序，则说明是全排列的最后一种情况，则下一个排列就是最初始情况.
        if first == 0:
            nums = list(reversed(nums))
        # 在nums[i:]中找到比nums[i-1]大的最小数，交换元素，然后将nums[first:]翻转成升序.
        else:
            minNum = [float('Inf'), -1]
            for i in range(first, len(nums)):
                if nums[first-1] < nums[i] < minNum[0]:
                    minNum = [nums[i], i]
            nums[first-1], nums[minNum[1]] = nums[minNum[1]], nums[first-1]
            nums = nums[:first] + list(reversed(nums[first:]))
        print(nums)


Solution().nextPermutation([1, 3, 2])