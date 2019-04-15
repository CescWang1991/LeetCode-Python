package slidingWindowMaximum

/* 239. Sliding Window Maximum
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
*/

func maxSlidingWindow(nums []int, k int) []int {
	if len(nums) == 0 {
		return nums
	}
	window := make([]int, 0) // store index instead of value
	rlt := make([]int, 0)
	for idx, v := range nums {
		if idx >= k && window[0] <= idx-k {
			window = window[1:]
		}
		for len(window) > 0 && nums[window[len(window)-1]] <= v {
			window = window[:len(window)-1]
		}
		window = append(window, idx)
		if idx >= k-1 {
			rlt = append(rlt, nums[window[0]])
		}
	}
	return rlt
}

// 方法二：大顶堆
