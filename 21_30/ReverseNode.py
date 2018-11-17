# 25. Reverse Nodes in k-group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
# multiple of k then left-out nodes in the end should remain as it is.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        while head:
            list = []
            for i in range(0, k):
                if head:
                    list.append(head)
                    head = head.next
                else:
                    list = []
            self.swap(list)

        return dummy.next

    def swap(self, list):
        s = 0
        e = len(list) - 1
        while s < e:
            temp = list[s].val
            list[s].val = list[e].val
            list[e].val = temp
            s += 1
            e -= 1