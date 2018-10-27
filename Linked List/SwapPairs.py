# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            node = head.next
            head.next = self.swapPairs(head.next.next)
            node.next = head
            return node
        else:
            return head