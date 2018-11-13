# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummyLess, dummyLarge = ListNode(None)
        less = dummyLess
        large = dummyLarge
        while head:
            if head.val < x:
                less.next = head
                less = head
            else:
                large.next = head
                large = head
            head = head.next

        less.next = dummyLarge.next
        large.next = None

        return dummyLess.next
