package threeSum

import "sort"
// 15. 3Sum
// 思路： 遍历 nums, 每个num都尝试作为第一个数字，再用二分查找来确定剩下两个数字
func threeSum(nums []int) [][]int {
	var (
		rlt  = [][]int{}
		prev =0
	)
	sort.Ints(nums)
	for idx, v := range nums {
		if len(rlt) != 0 && v == prev { // v== prev allow use skip the same previous element
			continue
		}
		l, r := idx+1, len(nums)-1
		for l < r {
			if nums[l] + nums[r] + v == 0 {
				rlt = append(rlt, []int{v, nums[l], nums[r]})
				prev = v
				for l+1 < r && nums[l] == nums[l+1] {
					// move next to the right-most same number
					l++
				}
				for r-1 > l && nums[r] == nums[r-1] {
					// move back to the left-most same number
					r--
				}
				l++
				r--
			}else if nums[l] + nums[r] + v > 0 {
				r = r -1
			} else {
				l = l +1
			}
		}
	}
	return rlt
}