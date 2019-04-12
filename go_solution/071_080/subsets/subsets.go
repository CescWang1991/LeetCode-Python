package subsets

// 78. Subsets
// 方法一: 位操作+格雷码
func subsetsWithBitOp(nums []int) [][]int {
	codes := grayCode(len(nums))
	var rlt [][]int
	for _, v := range codes {
		var item []int = make([]int, 0)
		for i := 0; i < len(nums); i++ {
			if (v>>uint(i))&1 == 1 {
				item = append(item, nums[i])
			}
		}
		rlt = append(rlt, item)
	}
	return rlt
}

func grayCode(n int) []int {
	if n == 0 {
		return []int{}
	}
	var rlt []int
	for i := 0; i < (1 << uint(n)); i++ {
		rlt = append(rlt, i^(i>>1))
	}
	return rlt
}

//--------------------------------

// 方法二： 递归+回溯
func subsetsWithBackTrack(nums []int) [][]int {
	rlt := make([][]int,0)
	rlt, _ = backtrack(rlt,[]int{}, nums,0)
	return rlt
}

func backtrack(rlt [][]int, tmp []int, nums []int, start int) ([][]int, []int) {
	ready := make([]int,len(tmp))
	copy(ready, tmp)
	rlt = append(rlt, ready)
	for i := start; i < len(nums); i++ {
		tmp = append(tmp, nums[i])
		rlt, tmp = backtrack(rlt, tmp, nums, i+1)
		tmp = tmp[:len(tmp)-1]
	}
	return rlt, tmp
}
