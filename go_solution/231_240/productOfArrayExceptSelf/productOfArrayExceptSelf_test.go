package productOfArrayExceptSelf

import "testing"

func Test_productOfArrayExceptSelf(t *testing.T) {
	nums := []int{-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1}
	t.Log(productExceptSelf(nums))
}
