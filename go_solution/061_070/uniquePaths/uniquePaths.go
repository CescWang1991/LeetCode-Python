package uniquePaths

// 62. Unique Paths
// 思路：使用动态规划，转移方程类似 斐波那契数列问题 和 爬楼梯问题
func uniquePaths(m int, n int) int {
	var dp [][]int = [][]int{}
	// init dp matrix
	for i:= 0; i< m; i++ {
		dp = append(dp, make([]int, n))
	}
	dp[0][0] = 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i != 0 && j != 0 {
				dp[i][j] = dp[i][j-1] + dp[i-1][j]
			} else {
				if i == 0 && j == 0 {
					continue
				}else if j != 0 {
					dp[i][j] = dp[i][j-1]
				} else if i != 0 {
					dp[i][j] = dp[i-1][j]
				}
			}
		}
	}
	return dp[m-1][n-1]
}
