package sorting

func quickSort(nums []int) {
	if len(nums) <= 1 {
		return
	}
	left, right := 0, len(nums)-1
	pivot := partition(nums, left, right)
	partition(nums, left, pivot-1)
	partition(nums, pivot+1, right)
}

func partition(nums []int, left, right int) (pivot int) {
	base := nums[left]
	i, j := left, right
	for i < j {
		// 从右到左，找到第一个比base小的元素
		for i < j && nums[j] > base {
			j--
		}
		// 把找到的元素移动到i的位置
		if i < j {
			nums[i] = nums[j]
			i++
		}
		// 从左到右，找到第一个比base大的元素
		for i < j && nums[i] < base {
			i++
		}
		// 把找到的元素移动到j的位置
		if i < j {
			nums[j] = nums[i]
			j--
		}
	}
	nums[i] = base
	return i
}
