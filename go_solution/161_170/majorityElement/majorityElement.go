package majorityElement

import "sort"

// 169. Majority Element

func majorityElement(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	sort.Ints(nums)
	return nums[len(nums)/2]
}
