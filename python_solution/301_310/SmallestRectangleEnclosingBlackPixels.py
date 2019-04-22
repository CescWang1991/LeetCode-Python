# 302. Smallest Rectangle Enclosing Black Pixels

# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected,
# i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one
# of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
#
# For example, given the following image:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2,
# Return 6.

class Solution:
    # 运用dfs，从x，y开始遍历，然后更新最大最小的x，y坐标，为了减少重复遍历，我们把遍历过的点设为"#"
    def minArea(self, image, x, y):
        """
        :type image: list[str]
        :type x: int
        :type y: int
        :rtype: int
        """
        self.image = image
        self.minX = x
        self.maxX = x
        self.minY = y
        self.maxY = y
        self.n = len(image)
        self.m = len(image[0])
        self.dfs(x, y)
        return (self.maxX - self.minX + 1) * (self.maxY - self.minY + 1)

    def dfs(self, x, y):
        if x < 0 or x >= self.n or y < 0 or y >= self.m or self.image[x][y] != "1":
            return
        self.image[x] = self.image[x][:y] + "#" + self.image[x][y+1:]
        self.minX = min(self.minX, x)
        self.maxX = max(self.maxX, x)
        self.minY = min(self.minY, y)
        self.maxY = max(self.maxY, y)
        self.dfs(x - 1, y)
        self.dfs(x + 1, y)
        self.dfs(x, y - 1)
        self.dfs(x, y + 1)