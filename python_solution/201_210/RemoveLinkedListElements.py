# 203. Remove Linked List Elements

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        if dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next

        return dummy.next