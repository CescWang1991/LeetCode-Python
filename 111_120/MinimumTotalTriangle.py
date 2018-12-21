# 120. Triangle
# Dynamic Programming: 使用O(n)的空间复杂度。dp(i)表示在最后一行到达i位置所用最小的和，即dp[i] = min(dp[i-1] + dp[i])+ triangle[i]
# 每次迭代，在dp最后添加(dp(-1) + triangle(i))作为末尾，然后根据dp公式从后向前更新。

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        dp = [triangle[0][0]]
        n = len(triangle)

        for i in range(1, n):
            dp.append(dp[-1] + triangle[i][-1])     # 在末尾添加最后一个元素的路径和
            for j in reversed(range(1, i)):         # 同#119，从后往前遍历
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            if i >= 1:                              # 更新第一个元素
                dp[0] = dp[0] + triangle[i][0]

        return min(dp)