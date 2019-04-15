package longestIncreasingSubsequence

/* 300. Longest Increasing Subsequence
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
*/
func lengthOfLIS(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}
	rlt := 1
	dp := make([]int, len(nums))
	for i := 0; i < len(dp); i++ {
		dp[i] = 1
	}
	for i := 1; i < len(nums); i++ {
		max := 1
		for j := 0; j < i; j++ {
			if dp[j] >= max && nums[i] > nums[j] {
				max = dp[j]
				dp[i] = max + 1
			}
		}
		if dp[i] > rlt {
			rlt = dp[i]
		}
	}
	return rlt
}
