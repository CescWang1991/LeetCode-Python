# 153. Find Minimum in Rotated Sorted Array
# 154. Find Minimum in Rotated Sorted Array II

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]

    def findMinDup(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        lo = 0
        hi = len(nums) - 1
        # 与#33与#81不同，当搜索左侧区间时，mid=hi，而不是mid=hi-1；这是因为考虑到mid到达边界的时候！
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1        # 可以加1，将查找范围往后推(因为这时mid不可能时我们要找的值)
            elif nums[mid] < nums[hi]:
                hi = mid            # 不可以减1, 因为mid可能就是我们要查找的元素
            # 如果 mid与hi相等，我们则把右边值向左一位即可
            else:
                hi -= 1

        return nums[lo]