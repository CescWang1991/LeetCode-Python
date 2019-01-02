# 274. H-Index
# 275. H-Index II

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        res = 0
        citations = sorted(citations, reverse=True)     # 先将citations按逆序排序
        for i in range(len(citations)):
            if citations[i] >= i + 1:  # 只要当前的数值大于等于个数(i+1)，就对res赋值，否则直接break
                res = i + 1
            else:
                break
        return res

class Solution2:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n - mid:
                hi = mid        # 此处不能减一，因为会取到hi的值
            else:
                lo = mid + 1
        # 需要注意[0, 0, ... , 0]的情况，这时返回0
        return n - hi if citations[hi] != 0 else 0