package sortList

import "testing"

func Test_sortList(t *testing.T) {
	head := genList([]int{3,4,1,6,2,7,9,8,0,5})
	rlt := sortList(head)
	for rlt != nil {
		t.Log(rlt.Val)
		rlt = rlt.Next
	}
}

func Test_addNode(t *testing.T) {
	head := genList([]int{0,1,2,3,4})
	source := genList([]int{5,6,7,8,9,})
	rlt := addNode(head, source, 3)
	for rlt != nil {
		t.Log(rlt.Val)
		rlt = rlt.Next
	}
	for head != nil {
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
