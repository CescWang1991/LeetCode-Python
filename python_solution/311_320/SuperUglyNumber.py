# 313. Super Ugly Number

class Solution:
    # 参见# 264. Ugly Number II
    # 利用动态规划，复杂度O(nk)，dp[i]是第i个超级丑数，dp[i]为dp[j] * primes[k] > dp[i-1]的最小值，其中j < i
    # 我们可以用一个idx数组来保存当前的位置，然后我们从每个子链中取出一个数，找出其中最小值，然后更新idx数组对应位置
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [float('Inf')] * n
        dp[0] = 1
        idx = [0] * len(primes)
        for i in range(n):
            # 举例：dp[4] = dp[2] * primes[0]，这时候我们需要将idx[0] + 1 = 3，因为dp的前三位与primes[0]的乘积已经出现在
            # 之前的dp中，这样在后面的遍历中，我们需要用dp[3] * primes[0]，这样可以保证dp[idx[j]] * primes[j] > dp[i-1]
            for j in range(len(primes)):
                dp[i] = min(dp[i], dp[idx[j]] * primes[j])
            for j in range(len(primes)):
                if dp[i] == dp[idx[j]] * primes[j]:
                    idx[j] += 1
        return dp[n-1]