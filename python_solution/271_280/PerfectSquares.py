# 279. Perfect Squares

class Solution:
    # BFS，每个节点连接比他小的平方和，我们用一个队列来记录节点，队列元素为(剩余和，层数，当前平方根)
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = [(n, 0, float('Inf'))]
        while queue:
            curr = queue[0][0]
            layer = queue[0][1]
            last = queue[0][2]      # 优化循环，我们保证路径上的平方根是递减的
            del queue[0]
            import math
            root = min(int(math.sqrt(curr)), last)  # 所以对于当前节点，它的循环满足最大值为剩余和的平方根与当前平方根的最小值
            for i in reversed(range(1, root+1)):
                queue.append((curr - i * i, layer + 1, i))
                if curr - i * i == 0:
                    return layer + 1
        return n

class Solution2:
    # 根据四平方和定理，任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，那么就是说返回结果只有1,2,3或4其中的一个
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 由于一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同
        while n % 4 == 0:
            n = n // 4
        # 如果一个数除以8余7的话，那么肯定是由4个完全平方数组成
        if n % 8 == 7:
            return 4

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3

        import math
        root = int(math.sqrt(n))
        for a in reversed(range(1, root+1)):
            b = int(math.sqrt(n - a*a))
            if a * a + b * b == n:
                return 2 if a > 0 and b > 0 else 1
        return 3

class Solution3:
    # 动态规划，dp[i]初始化为无穷大，假如i+j*j小于n，dp[i+j*j] = min(dp[i] + 1, dp[i+j*j])
    # Leetcode超时
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('Inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(n):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1
        return dp[n]