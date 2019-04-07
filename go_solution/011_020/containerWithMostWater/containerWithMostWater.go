package containerWithMostWater
// 11. Container With Most Water
func maxArea(height []int) int {
	// 从头和尾部开始向内搜索
	// 因为i:=0,j;=len(height)-1时，长度是最长的，所以向内搜索的时候只用考虑高度更高的情况
	i, j := 0, len(height)-1
	rlt := 0
	for i < j {
		rlt = max(rlt, (j-i)*min(height[i], height[j]))
		if height[i] < height[j] {
			i++
		}else {
			j--
		}
	}
	return rlt
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}