# 调整数组的顺序使奇数位于偶数前面

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

class Solution:
    def reorderArray(self, nums):
        if not nums:
            return nums
        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] % 2 == 1:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1

        return nums

