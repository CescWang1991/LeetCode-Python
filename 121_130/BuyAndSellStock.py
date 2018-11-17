# 121. Best Time to Buy and Sell Stock
# 122. Best Time to Buy and Sell Stock II：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

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

nums= [7, 1, 5, 3, 6, 4]
print(Solution().maxProfitTwice(nums))