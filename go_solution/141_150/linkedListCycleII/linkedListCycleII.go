package linkedListCycleII

// 142. Linked List Cycle II
type ListNode struct {
	Val  int
	Next *ListNode
}
// 思路： 使用快慢指针
func detectCycle(head *ListNode) *ListNode {
	fast, slow := head, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
		if fast == slow { // 检测列表到有环
			for head != slow { // 慢指针和head按相同步长前进，碰到一起的地方就是环的起点
				head = head.Next
				slow = slow.Next
			}
			return head
		}
	}
	return nil
}
