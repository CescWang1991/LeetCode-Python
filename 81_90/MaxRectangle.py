class Solution:
    def largestRectangleArea(self, nums):
        if not nums:
            return 0

        nums.append(0)
        length = len(nums)
        m = 0
        stack = []
        i = 0
        while i < length:
            if not stack or nums[i] >= nums[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = nums[stack[-1]]
                stack.pop()
                if not stack:
                    m = max(m, h * i)
                else:
                    m = max(m, h * (i - stack[-1] - 1))

        return m

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix[0])
        n = len(matrix)
        maxArea = 0
        height = [0] * m
        for i in range(n):
            for j in range(m):
                height[j] = height[j] + 1 if matrix[i][j] == "1" else 0
            maxArea = max(self.largestRectangleArea(height), maxArea)

        return maxArea

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(Solution().maximalRectangle(matrix))