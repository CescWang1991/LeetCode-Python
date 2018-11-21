# 136. Single Number
# 137. Single Number II
# 解答：https://blog.csdn.net/jiangxiewei/article/details/82227451

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

    # 遍历所有数,一个二进制位出现1的次数对3取余是否为1,若为1,那么我们目标数字的这一位也就是1。
    # 我们要运用逻辑门的想法设计一个计数器.计数到3就回归0。
    def singleNumberTriple(self, nums):
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