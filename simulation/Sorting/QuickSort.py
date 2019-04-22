class Solution:
    def quickSort(self, nums, p, r):
        if not nums or len(nums) == 1:
            return nums

        if p < r:
            q = self.partition(nums, p, r)
            self.quickSort(nums, p, q - 1)
            self.quickSort(nums, q + 1, r)

    def partition(self, nums, p, r):
        pivot = nums[r]
        i = p
        for j in range(p, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        print(nums[p: r+1])
        nums[r], nums[i] = nums[i], nums[r]
        print(nums[p: r + 1])
        return i


class TopK:
    def partition(self, nums, p, r):
        pivot = nums[r]
        i = p
        for j in range(p, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        print(nums[p: r + 1])
        nums[r], nums[i] = nums[i], nums[r]

        return i

    def topk(self, nums, k):
        if k == 0:
            return None
        if len(nums) <= k:
            return nums
        left = 0
        right = len(nums) - 1
        s = self.partition(nums, left, right)
        while s != len(nums) - k:
            if s < len(nums) - k:
                left = s + 1
            elif s < len(nums) - k:
                right = s - 1
            s = self.partition(nums, left, right)

        return nums[len(nums) - k:]