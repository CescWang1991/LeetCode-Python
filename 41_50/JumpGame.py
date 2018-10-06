# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.


class Solution(object):
    def jump(self, nums):
        steps = 1
        if(len(nums) - 1 <= nums[0]):
            return 1
        else:
            for i in range(nums[0]):
                rest = Solution().jump(nums[(i + 1):])
                if steps == 1:
                    steps = rest + 1
                else:
                    if rest + 1 < steps:
                        steps = rest + 1

        return steps


nums = [2, 3, 0, 1, 4]
print(Solution().jump(nums))
