# 055. Jump Game

class Solution:
    # Greedy Algorithm
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pos = len(nums) - 1
        # 从右至左遍历，对于每一个位置，假如i+nums[i]可以达到pos的index，将pos至为i(代表能从pos出发到达最后)
        for i in reversed(range(len(nums))):
            if i + nums[i] >= pos:
                pos = i
        # 检验最后的pos是否在起点
        return pos == 0
