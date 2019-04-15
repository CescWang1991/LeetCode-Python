package productOfArrayExceptSelf

// 238. Product of Array Except Self
func productExceptSelf(nums []int) []int {
	var rlt = make([]int, len(nums))
	for i, tmp := 0, 1; i < len(nums); i++ {
		rlt[i] = tmp
		if nums[i] == 1 {
			continue
		}
		if nums[i] == -1 {
			tmp = -tmp
		}else {
			tmp *= nums[i]
		}
	}
	for i, tmp := len(nums)-1, 1; i >= 0; i-- {
		rlt[i] *= tmp
		if nums[i] ==1 {
			continue
		}
		if nums[i] == -1 {
			tmp = -tmp
		}else{
			tmp *= nums[i]
		}
	}
	return rlt
}
