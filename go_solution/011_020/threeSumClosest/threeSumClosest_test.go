package threeSumClosest

import "testing"

func Test_threeSumClosest(t *testing.T) {
	nums := []int{0,2,1,-3}
	target := 1
	t.Log(threeSumClosest(nums, target))
}
