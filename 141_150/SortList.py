# 148. Sort List
# 归并排序

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        # 快慢指针，这里我们希望指向中点前一个点，所以fast初始为head.next
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        dummy = self.merge(self.sortList(head), self.sortList(fast))

        return dummy

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