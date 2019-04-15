package rotateList

// 61. Rotate List

type ListNode struct {
	Val  int
	Next *ListNode
}

// 思路：首先要知道list的长度，然后利用一前一后等距指针找到倒数第k+1个节点
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k == 0 {
		return head
	}

	total := listLen(head)
	k = k % total
	if k == 0 {
		return head
	}

	early := head
	later := head

	for ; k > 0; k-- {
		early = early.Next
	}

	for ; early.Next != nil; early = early.Next {
		later = later.Next
	}

	early.Next = head

	newHead := later.Next
	later.Next = nil

	return newHead
}

func listLen(head *ListNode) int {
	i := 0
	for head != nil {
		i += 1
		head = head.Next
	}
	return i
}
