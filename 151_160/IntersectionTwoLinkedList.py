# 160. Intersection of Two Linked List
# 1.找到两个链表长度差n后较长的链表先走n步
# 2,然后两个指针同时向前走，如果两个指针相等，则该点为交点的入口
# 3.如果遍历完指针仍然不相等，则说明无焦点。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        while p1:
            headA = headA.next
            p1 = p1.next
        while p2:
            headB = headB.next
            p2 = p2.next
        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None