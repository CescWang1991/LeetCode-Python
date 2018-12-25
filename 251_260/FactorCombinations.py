# 254. Factor Combinations

# Numbers can be regarded as product of its factors. For example,
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.

# input: 12; output:
# [ [2, 6],
#   [2, 2, 3],
#   [3, 4]]

# input: 32; output:
# [ [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]]

class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.dfs(n, flag=True)

    def dfs(self, n, flag):     # flag用来标识当前是否为第一层dfs。
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [] if flag else [[n]]     # 如果为第一层，对于素数，我们返回空，否则我们将本身加入到res中
        import math
        root = int(math.sqrt(n))
        for i in range(2, root+1):
            if n % i == 0:
                post = self.dfs(n // i, False)
                if post:
                    for item in post:
                        if i <= item[0]:
                            res.append([i] + item)
        return res