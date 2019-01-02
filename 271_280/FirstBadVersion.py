# 278. First Bad Version

# The isBadVersion API is already defined for you.
def isBadVersion(version):
    """
    :param version: an integer
    :return: a bool
    """

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi