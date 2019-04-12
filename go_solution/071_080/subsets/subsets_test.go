package subsets

import (
	"fmt"
	"testing"
)

func Test_subsetsWithBitOp(t *testing.T) {
	nums := []int{1,2,3}
	t.Log(subsetsWithBitOp(nums))
}

func Test_subsetsWithBackTrack(t *testing.T) {
	nums := []int{1,2,3}
	t.Log(subsetsWithBackTrack(nums))
}

func Test_modify(t *testing.T) {
	tmp := make([]int,0)
	tmp = append(tmp, 1)
	fmt.Printf("outer %p %v cap: %v\n", tmp, tmp, cap(tmp))
	modify(tmp)
	fmt.Printf("outer %p %v %v cap: %v\n", tmp, tmp, tmp[:cap(tmp)], cap(tmp))
}

func modify(tmp []int) {
	fmt.Printf("inner %p %v cap: %v\n", tmp, tmp, cap(tmp))
	tmp = append(tmp, 10)
	fmt.Printf("inner %p %v cap: %v\n", tmp, tmp, cap(tmp))
}