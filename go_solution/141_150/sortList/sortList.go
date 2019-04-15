package sortList

// 148. Sort List

type ListNode struct {
	Val  int
	Next *ListNode
}

// solution form leetcode discussion, do merge sort with out recursion
func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	var dummyHeadOne *ListNode = &ListNode{}
	var dummyHeadTwo *ListNode = &ListNode{}
	var dummySortedHead *ListNode = &ListNode{}
	var dummySortedLast *ListNode = dummySortedHead
	var unvisitedNode *ListNode = head

	var listLength, level uint = 0, 0
	for unvisitedNode != nil && unvisitedNode.Next != nil {
		unvisitedNode = addNode(dummyHeadOne, unvisitedNode, 1<<level)
		unvisitedNode = addNode(dummyHeadTwo, unvisitedNode, 1<<level)
		newHead, newTail := merge(dummyHeadOne.Next, dummyHeadTwo.Next)
		dummySortedLast.Next = newHead // this also modify dummySortedHead.Next
		dummySortedLast = newTail
		listLength += 2
	}
	if unvisitedNode != nil {
		dummySortedLast.Next = unvisitedNode
		listLength++
	}
	level++

	for listLength > 1<<level {
		dummySortedLast = dummySortedHead
		unvisitedNode = dummySortedHead.Next
		for unvisitedNode != nil {
			unvisitedNode = addNode(dummyHeadOne, unvisitedNode, 1<<level)
			unvisitedNode = addNode(dummyHeadTwo, unvisitedNode, 1<<level)
			newHead, newTail := merge(dummyHeadOne.Next, dummyHeadTwo.Next)
			dummySortedLast.Next = newHead // this actually modify dummySortedHead.Next
			dummySortedLast = newTail
		}
		level++
	}

	return dummySortedHead.Next
}

/* merge listOne and listTwo.
Save the sorted list head into rst.newHead
Save the last node of the sorted list into rst.newTail
*/
func merge(listOne, listTwo *ListNode) (*ListNode, *ListNode) {
	var dummyHead = &ListNode{}
	var lastNode = dummyHead
	for listOne != nil && listTwo != nil {
		if listOne.Val < listTwo.Val {
			lastNode.Next = listOne
			listOne = listOne.Next
		} else {
			lastNode.Next = listTwo
			listTwo = listTwo.Next
		}
		lastNode = lastNode.Next
	}

	for listOne != nil {
		lastNode.Next = listOne
		listOne = listOne.Next
		lastNode = lastNode.Next
	}
	for listTwo != nil {
		lastNode.Next = listTwo
		listTwo = listTwo.Next
		lastNode = lastNode.Next
	}
	return dummyHead.Next, lastNode
}

// add at max #"count" nodes into "head" from "source"
// return the new position of source after adding.
func addNode(head *ListNode, source *ListNode, count int) *ListNode {
	for count > 0 && source != nil {
		head.Next = source
		head = head.Next
		source = source.Next
		count--
	}
	head.Next = nil
	return source
}
