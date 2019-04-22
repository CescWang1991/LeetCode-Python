# 011. Container With Most Water

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height) - 1
        maxArea = 0
        while lo < hi:
            area = (hi - lo) * min(height[lo], height[hi])
            maxArea = max(maxArea, area)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1

        return maxArea