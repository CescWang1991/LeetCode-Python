# dynamic programming
# DP(n,k) = DP(n-1,k) + DP(n-1,k-1)

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        lists = []
        if n < k:
            return lists

        for s in reversed(range(k, n+1)):
            if k == 1:
                lists.append([s])
            else:
                for l in self.combine(s-1, k-1):
                    l += [s]
                    lists.append(l)

        return lists


print(Solution().combine(108, 4))