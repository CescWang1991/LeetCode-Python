package triangle
// 120. Triangle

func minimumTotal(triangle [][]int) int {
	return oneDimensionDP(triangle)
}

func twoDimensionDP(triangle [][]int) int {
	if len(triangle) == 1 {
		return triangle[0][0]
	}
	// init dp matrix
	dp := make([][]int, len(triangle))
	for i:= 0; i< len(triangle); i++ {
		dp[i] = make([]int, len(triangle[i]))
	}
	dp[len(triangle)-1] =  triangle[len(triangle)-1]
	// dp processing
	for i:= len(triangle)-2; i>=0; i-- {
		for j:= len(triangle[i])-1;j>=0; j-- {
			if dp[i+1][j] <= dp[i+1][j+1] {
				dp[i][j] = dp[i+1][j] + triangle[i][j]
			}else {
				dp[i][j] += dp[i+1][j+1] + triangle[i][j]
			}
		}
	}
	return dp[0][0]
}

func oneDimensionDP(triangle [][]int) int {
	dp := make([]int, len(triangle[len(triangle)-1])+1)
	for i:= len(triangle)-1; i>=0; i-- {
		for j:= 0; j< len(triangle[i]); j++ {
			if dp[j] < dp[j+1] {
				dp[j] = dp[j] +  triangle[i][j]
			} else {
				dp[j] = dp[j+1] +  triangle[i][j]
			}
		}
	}
	return dp[0]
}