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


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9, 21, 1, 6]
    Solution().partition(a, 0, len(a)-1)