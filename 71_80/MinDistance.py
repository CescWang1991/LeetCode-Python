# Dynamic Programming:
# set a two-dim array costs, costs[i][j] means the min cost between first i chars of word1 and first j chars of word2
# if ith char of word1 is equals jth char of word2, then costs[i][j] = costs[i-1][j-1]
# else costs[i][j] = 1 + min(costs[i-1][j-1] + costs[i-1][j] + costs[i][j-1])

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        costs = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(m+1):
            costs[0][i] = i
        for j in range(n+1):
            costs[j][0] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    costs[j+1][i+1] = costs[j][i]
                else:
                    costs[j+1][i+1] = 1 + min(costs[j][i+1], costs[j+1][i], costs[j][i])

        return costs[n][m]


print(Solution().minDistance("dsdfsaf", "fdsfdg"))