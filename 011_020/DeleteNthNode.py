# 019. Remove Nth Node From End of List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 运用快慢指针，post先移动n步，然后prev和post移动直到post指向最后一个节点
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        prev, post = dummy, dummy
        for i in range(n):
            post = post.next
        # 这里验证post.next是为了让post能指向最后一个非空节点，这样prev指向被删除节点的前一个节点，方便删除操作
        while post.next:
            prev = prev.next
            post = post.next
        prev.next = prev.next.next

        return dummy.next