# 84. Largest Rectangle Area
# 85. Maximal Rectangle

class Solution:
    # https://www.cnblogs.com/ganganloveu/p/4148303.html
    def largestRectangleArea(self, nums):
        if not nums:
            return 0

        nums.append(0)
        length = len(nums)
        m = 0
        stack = []      # 维持一个堆栈，堆栈中的元素按从小到大排序
        i = 0
        # 由于height本身不是升序的，我们需要构造升序的stack。
        while i < length:
            if not stack or nums[i] >= nums[stack[-1]]:     # 若当前高度大于栈顶，将其加入堆栈
                stack.append(i)
                i += 1
            else:                                           # 否则弹出栈顶元素，计算栈顶到i之前的面积
                h = nums[stack[-1]]
                stack.pop()
                if not stack:
                    m = max(m, h * i)
                else:
                    m = max(m, h * (i - stack[-1] - 1))

        return m

    # 逐层遍历，用height来记录0到当前层的柱状图高度，如果当前高度为1，则为前一层高度加一，否则为0。
    # 然后利用largestRectangleArea来计算当前height的最大面积，并更新maxArea。
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