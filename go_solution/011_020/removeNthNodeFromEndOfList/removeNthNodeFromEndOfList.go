package removeNthNodeFromEndOfList

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	early, later := head, head
	for i := 0; i < n; i++ {
		early = early.Next
	}
	var prev *ListNode
	for early != nil {
		early = early.Next
		prev, later = later, later.Next
	}
	if prev == nil {
		return later.Next
	}
	prev.Next = later.Next
	return head
}
