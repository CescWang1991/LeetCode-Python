package addTwoNumbers

// 002. Add Two Numbers

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	tmp := 0
	head := &ListNode{Val: 0, Next: nil} // dummy node to track the head of the result
	node := head
	for l1 != nil || l2 != nil || tmp != 0 {
		if l1 != nil {
			tmp = tmp + l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			tmp = tmp + l2.Val
			l2 = l2.Next
		}
		node.Next = &ListNode{
			Val:  tmp % 10,
			Next: nil,
		}
		node = node.Next
		tmp = tmp / 10
	}
	return head.Next
}
