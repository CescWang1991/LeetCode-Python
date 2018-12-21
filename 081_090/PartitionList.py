# 086. Partition List

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

        dummyLess, dummyLarge = ListNode(None)  # 构造两个链表，分别存放小于和大于x的节点
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
        # 将它们进行拼接
        less.next = dummyLarge.next
        large.next = None

        return dummyLess.next