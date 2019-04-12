package sorting

// 方法一：递归
func mergeSortRecursion(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	mid := len(nums) >> 1
	left := mergeSortRecursion(nums[:mid])
	right := mergeSortRecursion(nums[mid:])
	return merge(left, right)
}

func merge(listOne, listTwo []int) []int {
	var rlt []int
	idxOne, idxTwo := 0, 0
	for idxOne < len(listOne) && idxTwo < len(listTwo) {
		if listOne[idxOne] < listTwo[idxTwo] {
			rlt = append(rlt, listOne[idxOne])
			idxOne++
		} else {
			rlt = append(rlt, listTwo[idxTwo])
			idxTwo++
		}
	}
	// 如果listOne 和 listTwo 长度不一致，处理剩下的元素
	if idxOne < len(listOne) { // listOne 有遗留元素，直接append
		rlt = append(rlt, listOne[idxOne:]...)
	}
	if idxTwo < len(listTwo) { // listTwo 有遗留元素，直接append
		rlt = append(rlt, listTwo[idxTwo:]...)
	}
	return rlt
}
//--------------------------------
// 方法二：非递归
func mergeSortIteration(nums []int) {
	var level uint64
	for len(nums) > 1<<level {
		step := 1 << level
		l, r := 0, step
		for r < len(nums) {
			mergeInPlace(nums, l, r, step)
			l = r + step
			r = l + step
		}
		level++
	}
}

// store merger result in nums directly
func mergeInPlace(nums []int, left, right, step int) {
	lend, rend := step+left, step+right
	if len(nums) < rend {
		rend = len(nums)
	}
	curr, i, j := left, left, right
	for i < lend && j < rend {
		if nums[i] < nums[j] {
			i++
		} else {
			rotateForward(nums, j, curr)
			j++
			i++
		}
		curr++
	}
}

func rotateForward(nums []int, from, to int) {
	if from-to == 1 {
		nums[from], nums[to] = nums[to], nums[from]
	} else {
		val := nums[from]
		nums = append(nums[:to], append([]int{val}, append(nums[to:from], nums[from+1:]...)...)...)
	}
}
