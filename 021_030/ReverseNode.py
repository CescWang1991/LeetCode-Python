# 025. Reverse Nodes in k-group

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
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
            if length == k:
                break
        if length < k:
            return head

        # 对head的前k位翻转(参见#206)，这里将reverse设为k位后面的排序链表，然后在其前面依次插入head。
        reverse = self.reverseKGroup(node, k)
        for i in range(k):
            next = reverse
            reverse = head
            head = head.next
            reverse.next = next