package rotateList

import "testing"

func TestLen(t *testing.T) {
	head := genList([]int{1,2,3,4,5,6,7})
	t.Logf("%v", head)
	t.Log(listLen(head))
	t.Logf("%v", head)
}

func TestGen(t *testing.T) {
	nums := []int{1,2,3,4}
	head := genList(nums)
	for head != nil{
		t.Log(head.Val)
		head = head.Next
	}
}

func genList(nums []int) *ListNode {
	dummy := &ListNode{
		Next:&ListNode{},
	}
	head := dummy.Next
	var prev *ListNode
	for _, v:= range nums {
		if head == nil {
			head = &ListNode{
				Val:v,
			}
		}else {
			head.Val = v

		}
		if prev != nil {
			prev.Next = head
		}
		prev = head
		head = head.Next
	}
	return dummy.Next
}

