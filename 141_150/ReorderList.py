# 143. Reorder List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        dummy = ListNode(None)
        dummy.next = head
        while head and head.next and stack:
            if head != stack[-1] and head.next != stack[-1]:
                next = head.next
                head.next = stack[-1]
                head.next.next = next
                stack.pop()
                head = next
            else:
                if head.next != stack[-1]:
                    head.next = None
                else:
                    head.next.next = None
                break

        return dummy.next