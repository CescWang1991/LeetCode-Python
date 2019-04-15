package trappingRainWater
//
// 思路：
func trapWithTwoPoints(height []int) int {
	l, r := 0, len(height) - 1
	water := 0
	lMax, rMax := 0, 0
	for l < r {
		if height[l] < height[r] {
			if height[l] < lMax {
				// 高度差就是积攒的雨水
				water += lMax - height[l]
			} else {
				lMax = height[l]
			}
			l++
		} else {
			if height[r] < rMax {
				// 高度差就是积攒的雨水
				water += rMax - height[r]
			} else {
				rMax = height[r]
			}
			r--
		}
	}
	return water
}

func trapWithStack(height []int) int {
	stack := NewStack() // stack 里存放的是height的下标
	water, idx := 0, 0
	for idx < len(height) {
		// 如果 stack 里是空，或者还是下坡的情况 直接入栈
		if stack.Len() == 0 || height[idx] <= height[stack.Peek()] {
			stack.Push(idx)
			idx++
			continue
		}
		// 如果栈顶有元素，且不是下坡的情况
		t := stack.Pop()
		if stack.Len() == 0 {
			continue
		}
		distance := idx - stack.Peek() - 1 // 计算宽
		wall := min(height[idx], height[stack.Peek()])
		water += distance * (wall - height[t])
	}
	return water
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
