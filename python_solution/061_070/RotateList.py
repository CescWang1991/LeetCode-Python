# 061. Rotate List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 第一次遍历，将第k个节点之后的节点值换成i-k个节点(向右平移k位)，同时记录前k个节点。注意k大于链表长度的情况。
    # 然后按顺序将后k个节点的值赋予前k个节点。
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
            queue.append(head.val)      # 维持一个长度为k的queue，将节点值按顺序放入，最后queue保存后k个节点的值
            if len(queue) == k + 1:     # 第i个节点值换成第i-k个节点值
                head.val = queue[0]
                del queue[0]
            else:                       # first保存前k个节点
                first.append(head)
            head = head.next

        # 当k大于链表长度n时，k = k % n，以新的k值重新运行一遍
        if len(queue) != 0 and len(queue) <= k:
            k = k % len(queue)
            dummy.next = self.rotateRight(first[0], k)
            first = []
        # 将后k个节点的值赋给前k个节点
        if first:
            for i in range(len(first)):
                first[i].val = queue[i]

        return dummy.next