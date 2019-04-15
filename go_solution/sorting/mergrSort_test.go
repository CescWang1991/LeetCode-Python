package sorting

import "testing"

func Test_mergeSort(t *testing.T) {
	nums := []int{4, 5, 3, 1, 7, 1, 6, 9}
	t.Log(mergeSortRecursion(nums))
}

func Test_mergeSortIteration(t *testing.T) {
	numsEven := []int{4, 5, 3, 1, 7, 1, 6, 9}
	mergeSortIteration(numsEven)
	t.Log(numsEven)
	numsOdd := []int{4, 5, 3, 1, 7, 1, 6, }
	mergeSortIteration(numsOdd)
	t.Log(numsOdd)
}

func Test_rotateForward(t *testing.T) {
	nums := []int{4, 5, 1, 3, 7, 1, 6, 9}
	rotateForward(nums, 2, 0)
	t.Log(nums)
}

func Test_mergeInPlace(t *testing.T) {
	nums := []int{4, 5, 3, 1, 7, 1, 6, 9}
	mergeInPlace(nums, 0, 1, 1)
	t.Log(nums)
	mergeInPlace(nums, 2, 3, 1)
	t.Log(nums)
	mergeInPlace(nums, 4, 5, 1)
	t.Log(nums)
	mergeInPlace(nums, 6, 7, 1)
	t.Log(nums)
	mergeInPlace(nums, 0, 2, 2)
	t.Log(nums)
	mergeInPlace(nums, 4, 6, 2)
	t.Log(nums)
	mergeInPlace(nums, 0, 4, 4)
	t.Log(nums)
}
