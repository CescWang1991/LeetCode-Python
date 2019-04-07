package trappingRainWater

func trap(height []int) int {
	var l, r = 0, len(height) - 1
	water := 0
	lMax, rMax := 0, 0
	for l < r {
		if height[l] < height[r] {
			if height[l] < lMax {
				water += lMax - height[l]
			} else {
				lMax = height[l]
			}
			l++
		} else {
			if height[r] < rMax {
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
	water, i := 0, 0
	for i < len(height) {
		if stack.Len() == 0 || height[i] <= height[stack.Peek()] {
			stack.Push(i)
			i++
		} else {
			t := stack.Pop()
			if stack.Len() == 0 {
				continue
			}
			distance := i - stack.Peek() - 1
			wall := min(height[i], height[stack.Peek()])
			water += distance * (wall - height[t])
		}
	}
	return water
}

type Stack struct {
	data []int
}

func NewStack() *Stack {
	return &Stack{
		data: make([]int, 0),
	}
}

func (s *Stack) Push(val int) {
	s.data = append(s.data, val)
}

func (s *Stack) Pop() int {
	val := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return val
}

func (s *Stack) Peek() int {
	return s.data[len(s.data)-1]
}

func (s *Stack) Len() int {
	return len(s.data)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
