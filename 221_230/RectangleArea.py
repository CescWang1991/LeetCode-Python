# 223. Rectangle Area

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # 两个矩形的面积
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        print(area1, area2, self.overlap(A, B, C, D, E, F, G, H))
        return area1 + area2 - self.overlap(A, B, C, D, E, F, G, H)

    # 相交的面积
    def overlap(self, A, B, C, D, E, F, G, H):
        h = min(C, G) - max(A, E)
        v = min(D, H) - max(B, F)

        if  h <= 0 or v <= 0:
            return 0
        else:
            return h * v

print(Solution().computeArea(-2, -2, 2, 2, 3, 3, 4, 4))