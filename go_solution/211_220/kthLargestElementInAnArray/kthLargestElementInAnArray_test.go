package kthLargestElementInAnArray

import "testing"

type TestCase struct {
	nums []int
	k int
	expect int
}

func Test_findKthLargest(t *testing.T) {
	tcs := []TestCase{
		{[]int{3,2,1,5,6,4}, 2, 5},
		{[]int{3,2,3,1,2,4,5,5,6}, 4, 4},
	}
	for _, tc := range tcs {
		out := findKthLargest(tc.nums, tc.k)
		if tc.expect != findKthLargest(tc.nums, tc.k) {
			t.Fatalf("nums: %v, k: %v, expect %v but got %v", tc.nums, tc.k, tc.expect, out)
		}
	}
}
