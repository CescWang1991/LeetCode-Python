# 第一题：鸡蛋掉落

class Solution:
    def minSteps(self, k, n):
        dp = [[0] * (n+1) for i in range(k+1)]
        for i in range(1, k+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] + 1
                if dp[k][j] >= n:
                    return j
        return 0

while True:
    try:
        line = list(input().split(","))
        k, n = int(line[0]), int(line[1])
        print(Solution().minSteps(k, n))
    except:
        break