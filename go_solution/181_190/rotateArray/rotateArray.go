package rotateArray

// 189. Rotate Array
// 思路：通过一个额外的slice来调换元素
func rotateExtraSpace(nums []int, k int)  {
	n := k % len(nums)
	r := nums[len(nums)-n:]
	l := nums[:len(nums)-n]
	r = append(r, l...)
	for i, v := range r {
		nums[i] = v
	}
}

// 思路：通过swap来移动元素
func rotateInPlace(nums []int, k int)  {
	nlen := len(nums)
	if nlen <= 1 {
		return
	}

	k = k % nlen
	if k == 0 {
		return
	}

	for i := 0; i < k; i++ {
		for j := nlen - 1; j > 0; j-- {
			nums[j], nums[j-1] = nums[j-1], nums[j]
		}
	}
}