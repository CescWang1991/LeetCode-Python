# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        queue = []
        first = []
        dummy = ListNode(None)
        dummy.next = head
        while head:
            queue.append(head.val)
            if len(queue) == k + 1:
                head.val = queue[0]
                del queue[0]
            else:
                first.append(head)
            head = head.next

        # 当k大于链表长度n时，k = k % n，以新的k值重新运行一遍
        if len(queue) != 0 and len(queue) <= k:
            k = k % len(queue)
            dummy.next = self.rotateRight(first[0], k)
            first = []

        if first:
            for i in range(len(first)):
                first[i].val = queue[i]

        return dummy.next