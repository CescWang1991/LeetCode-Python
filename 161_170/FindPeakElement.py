# 162. Find Peak Element

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        n = len(nums)
        lo = 0
        hi = n-1

        if n == 1:
            return nums[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if mid == 0 and nums[mid] > nums[mid+1]:        # mid在最左侧
                return 0
            if mid == n - 1 and nums[mid] > nums[mid-1]:    # mid在最右侧
                return n-1
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: # mid符合峰值条件，直接返回
                return mid

            if nums[mid] < nums[mid+1]:
                lo = mid + 1
            elif nums[mid] < nums[mid-1]:
                hi = mid - 1

        return None