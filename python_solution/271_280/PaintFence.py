# 276. Paint Fence

# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.

# Note:
# n and k are non-negative integers.

class Solution:
    # 最多右两个相邻的相同，我们可以用动态规划，分别记录前i项最右边相邻相同的为same，不相同的为diff，我们可以把空间压缩为常数。
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        same, diff = 0, k
        for i in range(1, n):
            temp = diff
            diff = (same + diff) * (k-1)        # 新加的颜色与最右边的不同
            same = temp                         # 新加的颜色与最右边的相同

        return same + diff