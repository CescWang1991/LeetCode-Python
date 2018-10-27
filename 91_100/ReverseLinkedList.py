# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pos = 1
        dummy = ListNode(None)
        prev = ListNode(None)
        prev.next = head
        dummy.next = prev
        while pos < m:
            if not prev.next:
                return dummy.next
            else:
                prev = prev.next
                pos += 1

        stack = []
        curr = prev
        while pos >= m and pos <= n:
            stack.append(curr.next.val)
            curr = curr.next
            pos += 1

        while stack:
            prev.next.val = stack[-1]
            stack.pop()
            prev = prev.next

        prev.next = curr.next

        return dummy.next.next