# 280. Wiggle Sort

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

class Solution:
    # 时间复杂度O(nlogn)，将数组排序，奇数项与其后面的偶数项交换
    def wiggleSort(self, nums):
        """
        :type nums:
        :rtype: void
        """
        nums = sorted(nums)
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

class Solution2:
    # 时间复杂度为O(n)的解法
    def wiggleSort(self, nums):
        for i in range(len(nums)-1):
            if i % 2 == 0:          # i为偶数时，需要满足nums[i] <= nums[i+1]，否则交换
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:                   # i为偶数时，需要满足nums[i] >= nums[i+1]，否则交换
                if nums[i] < nums[i+1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]