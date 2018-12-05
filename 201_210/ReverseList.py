# 206. Reverse List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 运用递归方法(916ms)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        prev = self.reverseList(head.next)
        dummy.next = prev
        while prev:
            prev = prev.next
        prev = head
        head.next = None

        return dummy.next

    # 运用迭代方法(52ms)
    def reverseListIter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(None)
        while head:
            next = dummy.next
            dummy.next = head
            head = head.next
            dummy.next.next = next

        return dummy.next