package rotateArray

import (
	"testing"
)

func Test_rotateExtraSpace(t *testing.T) {
	nums := []int{1,2,3,4,5,6,7,8,9}
	rotateExtraSpace(nums, 3)
	t.Log(nums)
}
