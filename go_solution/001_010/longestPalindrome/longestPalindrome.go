package longestPalindrome
// 005. Longest Palindromic Substring
func longestPalindrome(s string) string {
	// can use dp to solve
	// dp[i][j] is a boolean indicates if s[i:j] is a Palindrome string
	// dp[i][j] == dp[i-1][j-1] && (s[i]== s[j])
	if len(s) == 0 {
		return s
	}

	maxIdx := [2]int{0, 0} // record i and j for max result
	// init the dp matrix
	dp := make([][]bool, len(s))
	for i:= 0; i<len(s); i++ {
		dp[i] = make([]bool, len(s))
	}

	for j:= 0; j<len(s); j++ {
		dp[j][j]= true // single charater is always a palindromic sub string
		for i:=0; i< j; i++ {
			dp[i][j]=(s[j]==s[i]&&(j-i<2||j>0&&dp[i+1][j-1]))
			if(dp[i][j]) {
				if j-i > maxIdx[1] - maxIdx[0] {
					maxIdx[0] = i
					maxIdx[1] = j
				}
			}
		}
	}
	return s[maxIdx[0]:maxIdx[1]+1]
}