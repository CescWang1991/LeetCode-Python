# 147. Insertion Sort List
# 归并排序(LeetCode超时)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        mid = self.getMiddle(head)
        left = head
        right = mid.next
        mid.next = None

        return self.merge(self.sortList(left), self.sortList(right))

    def getMiddle(self, head):
        if not head or head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        head = ListNode(0)
        dummy = head
        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        if left:
            head.next = left
        if right:
            head.next = right

        return dummy.next