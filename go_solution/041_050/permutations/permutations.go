package permutations

// 46. Permutations
// 思路：用递归和回溯
func permute(nums []int) [][]int {
	if len(nums) <= 1 {
		return [][]int{nums}
	}
	rlt := make([][]int, 0)
	permuteCore(nums, 0, &rlt)
	return rlt
}

func permuteCore(nums []int, i int, rlt *[][]int) {
	// stander solution which use recursion
	if i == len(nums)-1 {
		cp := make([]int, len(nums))
		copy(cp, nums)
		*rlt = append(*rlt, cp)
		return
	}
	for j := i; j < len(nums); j++ {
		swap(nums, i, j)
		permuteCore(nums, i+1, rlt)
		swap(nums, i, j)
	}
}

func swap(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}
