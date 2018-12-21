# 075. Sort Colors
# 使用双指针，保证第一个指针one的前面都是0(不包括1)，第二个指针two后面都是2(包括2)。

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
            if nums[i] == 1:    # 如果当前点为1，与指针2交换。指针2加一
                nums[i], nums[two] = nums[two], nums[i]
                two = two + 1
            elif nums[i] == 0:
                if one == two:  # 两者相同，即指针2后面没有
                    nums[i], nums[one] = nums[one], nums[i]
                    one = one + 1
                    two = two + 1
                else:           # 否则先将指针1与当前元素交换，交换过来的是1，然后按照第一种情况和2交换
                    nums[i], nums[one] = nums[one], nums[i]
                    one = one + 1

                    nums[i], nums[two] = nums[two], nums[i]
                    two = two + 1
