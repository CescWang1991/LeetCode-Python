package sortColor

// 75. Sort Colors
// use quick sort
func sortColors(nums []int)  {
	quickSort(nums,0, len(nums)-1)
}

func quickSort(nums []int, l int, r int) {
	if l < r {
		pivot := partition(nums, l, r)
		quickSort(nums, l, pivot-1)
		quickSort(nums, pivot+1, r)
	}
}

func partition(nums []int, l int, r int) (pivot int) {
	base := nums[l] // always choose the leftmost element as the base
	i, j := l, r
	for i < j {
		// form right to left, to find the element less than base
		for j > i && nums[j]>= base{ // skip if nums[j] is greater than base
			j--
		}
		if j > i {
			nums[i] = nums[j] // for the first round, nums[j] is actually put in position l
			i++
		}
		// form left to right, to find the element greater than base
		for i< j && nums[i]< base{
			i++
		}
		if i < j {
			nums[j] = nums[i]
			j--
		}
	}
	nums[i] = base
	return i
}