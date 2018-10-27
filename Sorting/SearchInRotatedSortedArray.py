class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1
        while start < end:
            mid = int((start + end) / 2)
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        shift = start
        end = shift + len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if target == nums[int(mid % len(nums))]:
                return int(mid % len(nums))
            elif target > nums[int(mid % len(nums))]:
                start = mid + 1
            else:
                end = mid - 1

        return -1


list = [1, 3]
print(Solution().search(list, 3))
