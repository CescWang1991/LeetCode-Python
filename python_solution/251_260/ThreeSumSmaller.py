# 259. 3Sum Smaller

# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n 
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.

# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?

class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        count = 0
        for i in range(len(nums)-2):
            j = i + 1               # 第二个数从左边开始，第三个数从右边开始
            k = len(nums) - 1
            while j < k:            # 当三数值和小于target，隐含的条件是第二个数和第三个之间的任何一对数字都能够符合条件
                if nums[i] + nums[j] + nums[k] < target:
                    count += k - j
                    j += 1
                if nums[i] + nums[j] + nums[k] >= target:
                    k -= 1

        return count