package sorting

import "testing"

func Test_quickSort(t *testing.T) {
	nums := []int{4,5,3,1,7,1,6,9,}
	quickSort(nums)
	t.Log(nums)
}
