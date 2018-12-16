# 75. Sort Colors
# 使用双指针，保证第一个指针one的前面都是0，第二个指针two后面都是2，one初始在头，two初始在尾。

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        one = 0
        two = 0

        for i in range(m):
            if nums[i] == 1:
                nums[i], nums[two] = nums[two], nums[i]
                two = two + 1
            elif nums[i] == 0:
                if one == two:
                    nums[i], nums[one] = nums[one], nums[i]
                    one = one + 1
                    two = two + 1
                else:
                    nums[i], nums[one] = nums[one], nums[i]
                    one = one + 1

                    nums[i], nums[two] = nums[two], nums[i]
                    two = two + 1

        print(nums)


Solution().sortColors([0,2,2,2,0,2,1,1])
