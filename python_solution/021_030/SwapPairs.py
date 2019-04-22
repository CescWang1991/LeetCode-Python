# 024. Swap Nodes in Pairs

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 使用递归算法，交换head与head.next，然后递归调用head.next.next，将后面的节点交换
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