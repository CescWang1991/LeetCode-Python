package maximumProductSubarray

// 152. Maximum Product Subarray

func maxProduct(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	max, min := nums[0], nums[0]
	rlt := max
	for i := 1; i < len(nums); i++ {
		if nums[i] > 0 {
			if nums[i]*max > nums[i] {
				max = nums[i] * max
			} else {
				max = nums[i]
			}
			if nums[i]*min < nums[i] {
				min = nums[i] * min
			} else {
				min = nums[i]
			}
		} else {
			tmp := max
			if nums[i]*min > nums[i] {
				max = nums[i] * min
			} else {
				max = nums[i]
			}
			if nums[i]*tmp < nums[i] {
				min = nums[i] * tmp
			} else {
				min = nums[i]
			}
		}
		if rlt < max {
			rlt = max
		}
	}
	return rlt
}
