package threeSumClosest

import "sort"

// 16. 3Sum Closest
// 思路：和 3Sum 相似的思路
func threeSumClosest(nums []int, target int) int {
	if len(nums) == 3 {
		return nums[0] + nums[1] + nums[2]
	}
	var (
		rlt   []int
		delta int64 = 1<<63 - 1
		perv        = 0
	)
	sort.Ints(nums)
	for idx, v := range nums {
		if len(rlt) != 0 && v == perv {
			continue
		}
		l, r := idx+1, len(nums)-1
		for l < r {
			if calDelta(nums[l]+nums[r]+v, target) < delta {
				rlt = []int{nums[l] + nums[r] + v}
				delta = calDelta(nums[l]+nums[r]+v, target)
				perv = v
			} else if nums[l]+nums[r]+v > target {
				r--
			} else {
				l++
			}
		}
	}
	return rlt[0]
}

func calDelta(val1 int, val2 int) int64 {
	return abs(int64(val1 - val2))
}

func abs(n int64) int64 {
	y := n >> 63
	return (n ^ y) - y
}
