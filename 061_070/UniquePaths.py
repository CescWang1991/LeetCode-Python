class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways = [0] * n
        ways[0] = 1
        for i in range(m):
            for j in range(1, n):
                ways[j] += ways[j-1]
                print(ways)
        return ways[n-1]


print(Solution().uniquePaths(3, 4))