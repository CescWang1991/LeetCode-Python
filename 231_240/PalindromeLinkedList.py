# 234. Palindrome Linked List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 如果时间复杂度为O(n)，空间复杂度为O(1)，需要翻转链表（见#206. Reverse List）
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        # 运用快慢指针，找到链表的中点
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        slow.next = None
        # 从中点开始翻转链表的后半部分
        reverse = None
        while curr:
            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next

        while head and reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next

        return True