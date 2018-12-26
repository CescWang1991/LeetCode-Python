# 136. Single Number
# 137. Single Number II [解答：https://blog.csdn.net/jiangxiewei/article/details/82227451]
# 260. Single Number III

class Solution:
    # 需要用位操作Bit Operation来解此题，出现两次的元素异或为0。
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        res = 0
        for num in nums:
            res ^= num

        return res

class Solution2:
    # 遍历所有数,一个二进制位出现1的次数对3取余是否为1,若为1,那么我们目标数字的这一位也就是1。
    # 我们要运用逻辑门的想法设计一个计数器.计数到3就回归0。
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for num in nums:
            b = b ^ num & ~a
            a = a ^ num & ~b
        return b

class Solution3:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        sum = 0
        for i in range(len(nums)):
            sum ^= nums[i]          # sum是所有nums异或的结果，同样的元素异或结果为0，sum最后为两个元素的异或结果
        # 对于sum来说，位为1说明num1和num2在该位不同，我们以sum为1的最低位i，将nums分为两部分，num1和num2分别在不同的部分
        sum = "{:032b}".format(sum)
        bit = 0
        for i in range(len(sum)):
            if sum[i] == "1":
                bit = i
                break
        num1, num2 = 0, 0
        for i in range(len(nums)):
            target = "{:032b}".format(nums[i])
            if target[bit] == "0":
                num1 ^= nums[i]
            else:
                num2 ^= nums[i]
        return [num1, num2]