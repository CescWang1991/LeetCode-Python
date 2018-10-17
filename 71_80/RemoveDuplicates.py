class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        total = 1
        num = 1
        pointer = 1
        while pointer < len(nums):
            if nums[pointer-1] == nums[pointer]:
                num += 1
                if num <= 2:
                    total += 1
                    pointer += 1
                else:
                    num -= 1
                    nums.pop(pointer)
            else:
                num = 1
                total += 1
                pointer += 1
        print(nums)

        return total


print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))