# 256. Paint House

# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of
# painting each house with a certain color is different. You have to paint all the houses such that no two adjacent
# houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0]
# is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so
# on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.

class Solution:
    # dp[i][j]表示刷到第i个房子用颜色j的最小花费(j = 0, 1, 2)。
    # dp[i][j] = costs[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])。
    # 如果当前的房子要用红色刷，那么上一个房子只能用绿色或蓝色来刷，那么我们要求刷到当前房子，且当前房子用红色刷的最小花
    # 费就等于当前房子用红色刷的钱加上刷到上一个房子用绿色和刷到上一个房子用蓝色的较小值，这样当我们算到最后一个房子时，
    # 我们只要取出三个累计花费的最小值即可。
    def minCost(self, costs):
        """
        :type costs: list[list[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        for i in range(1, len(costs)):      # dp[i][j]表示刷到第i个房子用颜色j的最小花费(j = 0, 1, 2)。这里我们可以用costs代替dp。
            # dp[i][j] = costs[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])。由于j只有三种，我们可以分开计算。
            costs[i][0] = costs[i][0] + min(costs[i-1][1], costs[i-1][2])
            costs[i][1] = costs[i][1] + min(costs[i-1][0], costs[i-1][2])
            costs[i][2] = costs[i][2] + min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])


# 265. Paint House II

# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with
# a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0]
# is the cost of painting house 0 with color 0; costs[1][2]is the cost of painting house 1 with color 2, and so on...
# Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Follow up:
# Could you solve it in O(nk) runtime?

class Solution2:
    def minCosts(self, costs):
        """
        :type costs: list[list[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        for i in range(1, len(costs)):
            min1 = min(costs[i-1])        # 找到第i个房子costs的最小值以及颜色的index
            index = costs[i-1].index(min1)
            min2 = min(costs[i-1][:index] + costs[i-1][index+1:])     # 找到第二小的值
            # 除了index颜色的costs，其余的均要用到min1，costs[i][index]则要用到min2，这里的min1，min2对应上一题的min，即
            # 前i-1个房子粉刷，最后一个房子不用j颜色的最小花费
            for j in range(len(costs[i])):
                if j != index:
                    costs[i][j] += min1
                else:
                    costs[i][j] += min2
        return min(costs[-1])