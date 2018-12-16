# Greedy
# Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index
# currPosition + nums[currPosition] >= leftmostGoodIndex
# If we can reach a GOOD index, then our position is itself GOOD.
# Also,this new GOOD position will be the new leftmost GOOD index.

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pos = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= pos:
                pos = i

        return pos == 0


print(Solution().canJump([9, 4, 2, 1, 0, 2, 0]))
