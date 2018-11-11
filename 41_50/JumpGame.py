# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# We use "last" to keep track of the maximum distance that has been reached by using the minimum steps "ret",
# whereas "curr" is the maximum distance that can be reached by using "ret+1" steps.
# Thus,curr = max(i+A[i]) where 0 <= i <= last.


class Solution(object):
    def jump(self, A):
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i + A[i])
        return ret


nums = [3, 2, 1, 0, 4]
print(Solution().jump(nums))
