# 数组中出现次数超过一半的数字

# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

class Solution:
    def MoreThanHalfNum(self, nums):
        if not nums:
            return 0
        # 设定res为nums[0]，若res为真，则遍历数组后times大于1
        res = nums[0]
        times = 1
        for i in range(1, len(nums)):
            # 当times等于0，余下数组中res出现次数依然大于一半
            if times == 0:
                res = nums[i]
                times = 1
            elif nums[i] == res:
                times += 1
            else:
                times -= 1
        sum = 0
        for i in range(len(nums)):
            if nums[i] == res:
                sum += 1
        return res if sum * 2 > len(nums) else 0
