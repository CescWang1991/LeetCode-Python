# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        res = [str(nums[0])]
        for i in range(1, len(nums)):
            # 如果i与i-1无法成为连续区间
            if nums[i] - nums[i-1] > 1:
                # 如果i-1与res的最后一位不相等，那么它们可以组成一个区间
                if res[-1] != str(nums[i-1]):
                    res[-1] += "->" + str(nums[i-1])
                res.append(str(nums[i]))
        # 判断最后一位是否可以和res的最后组成区间
        if str(nums[-1]) != res[-1]:
            res[-1] += "->" + str(nums[-1])

        return res