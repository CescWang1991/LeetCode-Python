# 121. Best Time to Buy and Sell Stock
# 122. Best Time to Buy and Sell Stock II：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 123. Best Time to Buy and Sell Stock III：你不能同时参与多笔交易（你最多可以完成两笔交易）。
# 188. Best Time to Buy and Sell Stock IV：你不能同时参与多笔交易（你最多可以完成k笔交易）。

class Solution:
    # 121. 维持一个最小价格和最大利润，每次循环更新利润的最大值(max(当前价格-最小价格, 利润))和价格的最小值
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(prices[i], minPrice)

        return profit

    # 122. 每当后一个prices大于前一个时，就将差值加到profit里面。
    def maxProfitMulti(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        for i in range(len(prices) - 1):
            profit += max(prices[i+1] - prices[i], 0)

        return profit

    # 123. 维持一个maxLeft数组，记录数组前i项的最大利润(一次交易)，方法与121相同；
    # 同时维持一个maxRight数组，记录数组后i项的最大利润(一次交易)，方法与121相反，保存一个最大价格，从后往前遍历。
    # 最后从0开始循环遍历，i为断点值，两次交易的利润为left[i] + right[i]
    def maxProfitTwice(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        maxLeft = [0] * len(prices)
        maxRight = [0] * len(prices)

        minPrice = prices[0]
        for i in range(1, len(prices)):
            maxLeft[i] = max(prices[i] - minPrice, maxLeft[i-1])
            minPrice = min(minPrice, prices[i])

        maxPrice = prices[len(prices)-1]
        for i in reversed(range(len(prices)-1)):
            maxRight[i] = max(maxPrice - prices[i], maxRight[i+1])
            maxPrice = max(maxPrice, prices[i])

        profit = 0
        for i in range(len(prices)):
            profit = max(profit, maxLeft[i] + maxRight[i])

        return profit

    # 我们定义local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。
    # 然后我们定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。
    # local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
    # global[i][j] = max(local[i][j], global[i - 1][j])
    def maxProfitK(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        # 当k大于prices的个数时，我们可以当作122来做
        if k > len(prices):
            return self.maxProfitMulti(prices)
        # 因为local[i][j]只依赖local[i-1][j], global[i][j]只依赖global[i - 1][j])，我们可以把空间压缩到i
        local = [0] * (k+1)
        globa = [0] * (k+1)
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            # 注意需要从后往前遍历，因为local[i][j]依赖global[i-1][j-1]，所以local[i]要比global[j-1]先更新
            for j in reversed(range(1, k+1)):
                local[j] = max(globa[j-1] + max(diff, 0), local[j] + diff)
                globa[j] = max(globa[j], local[j])

        return globa[k]