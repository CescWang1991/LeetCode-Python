class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            if nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1