while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        dp = [[0, 0] for i in range(n)]
        res = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i] = [nums[i], nums[i]]
                elif i < j:
                    dp[i][1] = min(dp[i][1], nums[j])
                    dp[i][0] = dp[i][0] + nums[j]
                else:
                    continue
                res = max(res, dp[i][0] * dp[i][1])
                print(dp)
        print(res)
    except:
        break