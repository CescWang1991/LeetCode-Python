# 300. Longest Increasing Subsequence

class Solution:
    # DP，dp[i]表示以nums[i]结尾的最长递增序列的长度，遍历到i，需要再次遍历前面所有的dp，对于所有小于nums[i]的点，
    # dp[i] = max(dp[i], dp[j] + 1)，然后更新最大值，时间复杂度O(n2)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        n = len(nums)
        dp = [1] * n
        maxLen = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxLen = max(maxLen, dp[i])
        return maxLen

class Solution2:
    # 维持一个ends数组，表示构成的递增序列，在这个过程中，我们对大于队首，小于队尾的数做特殊处理，找到ends中第一个不大于
    # 它的数，将其替换，这样可能造成ends数组的值可能不是一个真实的LIS，但是不会对长度有影响。
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ends = [nums[0]]
        for i in range(1, n):
            if nums[i] < ends[0]:   # 当前元素小于队首元素，直接将队首替换
                ends[0] = nums[i]
            elif ends[0] < nums[i] < ends[-1]:   # 当前元素小于队尾，大于队首
                # 我们用二分法找到第一个不小于当前元素的下标，将其替换成当前元素
                lo, hi = 0, len(ends) - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if ends[mid] < nums[i]:
                        lo = mid + 1
                    else:
                        hi = mid
                ends[hi] = nums[i]
            elif nums[i] > ends[-1]:    # 大于队尾，直接插入
                ends.append(nums[i])
        return len(ends)
