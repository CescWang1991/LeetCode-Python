# 081. Search in Rotated Sorted Array II

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target:
                return True
            # 如果中值大于左边值，则左半边有序，我们搜索左半边
            if nums[mid] > nums[lo]:
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # 如果中值小于左边值，则右半边有序。。。
            elif nums[mid] < nums[lo]:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # 如果两者相等，我们则把左边值向右一位即可
            else:
                lo += 1

        return False