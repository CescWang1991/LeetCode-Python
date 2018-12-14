# 238. Product of Array Except Self

class Solution:
    # 基本原理：left是前i位的乘积的数组，right是后i位乘积的数组，对于nums[i]，他的结果是left[i-1]*right[i+1]。
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        res[0] *= nums[0]
        # 由于需要空间复杂度O(1)，output数组不算空间复杂度，我们用output数组来代替left数组，循环一次。
        for i in range(len(nums)):
            res[i] = res[i-1] * nums[i]
        # 第二次循环，从后往前遍历，用一个数right表示累乘值，循环开始时，res[i] = res[i-1]*right，然后right *= nums[i]。
        right = 1
        for i in reversed(range(1, len(nums))):
            res[i] = res[i-1] * right
            right *= nums[i]
        res[0] = right

        return res

print(Solution().productExceptSelf([2,3,4,5]))