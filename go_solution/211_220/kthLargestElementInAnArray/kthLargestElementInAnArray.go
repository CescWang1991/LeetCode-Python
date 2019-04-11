package kthLargestElementInAnArray

import "container/heap"

// 215. Kth Largest Element in an Array
// 思路：使用大小为K的小顶heap去记录所有元素
func findKthLargest(nums []int, k int) int {
	return findKthLargestWithSort(nums, k)
}

func findKthLargestWithMiniHeap(nums []int, k int) int {
	h := NewMiniIntKHeap(k)
	for _, v := range nums {
		heap.Push(h, v)
	}
	return heap.Pop(h).(int)
}

func findKthLargestWithSort(nums []int, k int) int {
	expectedIdx := len(nums) - k
	left, right, pivotIdx, pivotVal := divideByPivot(nums, 0)
	for pivotIdx != expectedIdx {
		if pivotIdx < expectedIdx {
			left, right, pivotIdx, pivotVal = divideByPivot(right, pivotIdx + 1)
		} else {
			left, right, pivotIdx, pivotVal = divideByPivot(left, pivotIdx - len(left))
		}
	}
	return pivotVal
}

func divideByPivot(nums []int, startIdx int) ([]int,[]int, int, int) {
	pivot := nums[0]
	left, right := []int{}, []int{}
	for i:=1;i<len(nums);i++ {
		if nums[i] > pivot {
			right = append(right, nums[i])
		} else {
			left = append(left, nums[i])
		}
	}

	pivotIdx := startIdx + len(nums) - len(right) - 1
	// fmt.Printf("divide by pivot for nums: %v returned (%v, %v, %v, %v)\n", nums, left, right, pivotIdx, pivot)
	return left, right, pivotIdx, pivot

}

