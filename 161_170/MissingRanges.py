# 163. Missing Ranges

# Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: list
        :type lower: int
        :type upper: int
        :rtype: list[str]
        """
        if lower > upper:
            return []
        if not nums:        # 数组为空，直接返回lower和upper组成的区间
            return [str(lower) + "->" + str(upper)] if upper - lower >= 1 else [str(lower)]
        if nums[0] < lower:
            return self.findMissingRanges(nums[1:], lower, upper)
        elif nums[0] == lower:  # 相等时，lower加一
            return self.findMissingRanges(nums[1:], lower+1, upper)
        else:                   # nums[0]大于lower，添加lower和nums[0]组成的区间，lower更新为nums[0]+1
            interval = str(lower) if nums[0] - lower == 1 else str(lower) + "->" + str(nums[0]-1)
            return [interval] + self.findMissingRanges(nums[1:], nums[0]+1, upper)