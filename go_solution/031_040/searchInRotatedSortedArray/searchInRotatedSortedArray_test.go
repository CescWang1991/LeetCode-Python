package searchInRotatedSortedArray

import "testing"

type TestCase struct {
	nums []int
	target int
	expect int
}
func Test_search(t *testing.T) {
	tcs := []TestCase{
		{[]int{4,5,6,7,0,1,2}, 0, 4},
		{[]int{4,5,6,7,0,1,2}, 3, -1},
		{[]int{3,1}, 1, 1},
	}
	for _, tc := range tcs{
		out := search(tc.nums, tc.target)
		if tc.expect != out {
			t.Fatalf("nums: %v, targt: %v, expect %v but got %v", tc.nums, tc.target, tc.expect, out)
		}
	}
}
