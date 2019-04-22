# 135. Candy

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        candy = [1] * len(ratings)

        # 从左向右遍历，如果i项的rating大于i-1项，则i项的candy为i-1项加1。
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
        # 完成上述步骤后，从右向左遍历，如果i-1项的rating大于i项，则i-1项的rating为candy[i-1]与candy[i]+1的最大值
        for i in reversed(range(1, len(ratings))):
            if ratings[i-1] > ratings[i]:
                candy[i-1] = max(candy[i-1], candy[i] + 1)

        return sum(candy)