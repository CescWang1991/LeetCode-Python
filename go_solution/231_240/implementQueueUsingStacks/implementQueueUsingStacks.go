package implementQueueUsingStacks

// 232. Implement Queue using Stacks
type Stack struct {
	data []int
}

func NewStack() *Stack {
	return &Stack{
		data: make([]int, 0),
	}
}

func (s *Stack) Push(i int) {
	s.data = append(s.data, i)
}

func (s *Stack) Pop() int {
	if len(s.data) == 0 {
		return 0
	}
	rlt := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return rlt
}

func (s *Stack) Len() int {
	return len(s.data)
}

func (s *Stack) Top() int {
	if len(s.data) == 0 {
		return 0
	}
	return s.data[len(s.data)-1]
}

type MyQueue struct {
	in  *Stack
	out *Stack
}

/** Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{
		in:  NewStack(),
		out: NewStack(),
	}
}

/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int) {
	this.in.Push(x)
}

/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	if this.out.Len() > 0 {
		return this.out.Pop()
	}
	for this.in.Len() > 0 {
		this.out.Push(this.in.Pop())
	}
	return this.out.Pop()
}

/** Get the front element. */
func (this *MyQueue) Peek() int {
	if this.out.Len() > 0 {
		return this.out.Top()
	}
	for this.in.Len() > 0 {
		this.out.Push(this.in.Pop())
	}
	return this.out.Top()
}

/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
	return this.in.Len()+this.out.Len() == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
