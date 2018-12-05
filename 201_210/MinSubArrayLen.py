# 209. Minimum Size Subarray Sum

class Solution:
    # 使用动态规划，构造local数组，local[i]表示包含i元素的子数组的和以及最小长度，同时使用全局globa，更新最小长度。
    def minSubArrayLenWithDp(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        local = [[0, 0] for i in range(len(nums))]
        local[0] = [nums[0], 1] if nums[0] >= s else [nums[0], 0]
        globa = local[0][1]

        for i in range(1, len(nums)):
            sum, length = local[i-1][0], local[i-1][1]
            shift = 0
            sum += nums[i]
            if length == 0:
                if sum < s:
                    local[i] = [sum, 0]
                    continue
                else:
                    length = i
                    globa = i + 1
            while True:
                if sum - nums[i-length+shift] >= s:
                    sum -= nums[i-length+shift]
                    shift += 1
                else:
                    break
            length = length + 1 - shift
            local[i] = [sum, length]
            globa = min(globa, length)

        return globa

    # 双指针做法：如果sum<s，则r右移一位，反之则l右移一位。循环中注意更新最小长度。
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        sum = 0
        minLength = len(nums) + 1
        while l < len(nums):
            if r < len(nums) and sum < s:
                sum += nums[r]
                r += 1
            else:
                sum -= nums[l]
                l += 1

            if sum >= s:
                minLength = min(minLength, r - l)

        if minLength == len(nums) + 1:
            return 0

        return minLength