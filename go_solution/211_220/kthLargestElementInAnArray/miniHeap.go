package kthLargestElementInAnArray

import "container/heap"

type MiniIntKHeap struct {
	data []int
	limit int
}

func (h MiniIntKHeap) Len() int           { return len(h.data) }
func (h MiniIntKHeap) Less(i, j int) bool { return h.data[i] < h.data[j] }
func (h MiniIntKHeap) Swap(i, j int)      { h.data[i], h.data[j] = h.data[j], h.data[i] }

// Push and Pop use pointer receivers because they modify the slice's length,
// not just its contents.
func (h *MiniIntKHeap) Push(x interface{}) {
	val := x.(int)
	if len(h.data) == h.limit {
		if val > h.Peek() {
			heap.Pop(h)
			heap.Push(h, val)
		}
	}else {
		h.data = append(h.data, x.(int))
	}
}

// Pop should remove and return element Len() - 1.
func (h *MiniIntKHeap) Pop() interface{} {
	var x int
	h.data, x = h.data[0 : len(h.data)-1], h.data[len(h.data)-1]
	return x
}

func (h *MiniIntKHeap) Peek() int {
	return h.data[0]
}

func NewMiniIntKHeap(k int) *MiniIntKHeap {
	return &MiniIntKHeap{
		data: make([]int,0),
		limit:k,
	}
}
