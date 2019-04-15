package swapNodesInPairs

type ListNode struct {
	Val  int
	Next *ListNode
}

// 024. Swap Nodes in Pairs
func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	prev := &ListNode{
		Next: head,
	}
	rlt := head.Next
	for head != nil && head.Next != nil {
		next := head.Next
		head.Next, next.Next, prev.Next = next.Next, head, next
		prev, head = head, head.Next
	}
	return rlt
}
