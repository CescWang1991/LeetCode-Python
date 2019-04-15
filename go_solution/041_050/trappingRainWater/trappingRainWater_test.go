package trappingRainWater

import "testing"

func Test_Trap(t *testing.T) {
	input := []int{0,1,0,2,1,0,1,3,2,1,2,1}
	t.Log(trapWithStack(input))
}
