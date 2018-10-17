class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        one = 1
        two = 1

        if nums[0] == 1:
            one = 0
            two = 1
        elif nums[0] == 2:
            one = 0
            two = 0

        for i in range(1, m):
            if nums[i] == 1:
                temp = nums[two]
                nums[two] = nums[i]
                nums[i] = temp
                two = two + 1
            elif nums[i] == 0:
                if one == two:
                    temp = nums[one]
                    nums[one] = nums[i]
                    nums[i] = temp
                    one = one + 1
                    two = two + 1
                else:
                    temp = nums[one]
                    nums[one] = nums[i]
                    nums[i] = temp
                    one = one + 1

                    temp = nums[two]
                    nums[two] = nums[i]
                    nums[i] = temp
                    two = two + 1

            print(nums)


Solution().sortColors([1,0,2,1,1,0])
