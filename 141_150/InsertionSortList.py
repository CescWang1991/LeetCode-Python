# 147. Insertion Sort List
# 插入排序

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            # 当前值大于下一个值，将下一个值插入到当前值之前的链表中
            if curr.val > curr.next.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next
                temp = curr.next
                # 将curr.next暂时删除
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                curr = curr.next
        return dummy.next