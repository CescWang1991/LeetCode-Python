# 删除链表中的节点

# 在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
# 参考：# 237. Delete Node in a Linked List

class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

class Solution:
    def deleteNode(self, head, node):
        if not head or not head.next:
            return None
        if node.next:   # 删除非尾节点
            node.val = node.next.val
            node.next = node.next.next
        else:           # 删除尾节点
            node = head
            while node.next.next:
                node = node.next
            node.next = None
        return head