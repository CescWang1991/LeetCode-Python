package reverseNodesInKGroup

type ListNode struct {
	Val  int
	Next *ListNode
}

// 025. Reverse Nodes in k-Group

func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil { // no need to reverse
		return head
	}
	if k < 2 { // no need to reverse
		return head
	}

	var rlt *ListNode
	nextHead := head
	for i := k; i > 1; i-- {
		nextHead = nextHead.Next
		if nextHead == nil {
			return head
		}
	}
	rlt = nextHead
	current := head
	for nextHead != nil {
		tail := current
		var perv *ListNode = nil
		for j := 0; j < k; j++ {
			next := current.Next
			current.Next = perv
			perv = current
			current = next
			if nextHead != nil {
				nextHead = nextHead.Next
			}
		}
		if nextHead != nil {
			tail.Next = nextHead
		} else {
			tail.Next = current
		}
	}
	return rlt
}
