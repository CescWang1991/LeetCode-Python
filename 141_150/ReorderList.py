# 143. Reorder List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        dummy = ListNode(None)
        dummy.next = head
        while head and head.next and stack:
            if head != stack[-1] and head.next != stack[-1]:
                next = head.next
                head.next = stack[-1]
                head.next.next = next
                stack.pop()
                head = next
            else:
                if head.next != stack[-1]:
                    head.next = None
                else:
                    head.next.next = None
                break

        return dummy.next

class Solution2:
    # 运用快慢指针，找到链表中点，将后半部分链表翻转，同时中点的next指向空。
    # 从head开始，向每个节点后面添加翻转的链表相应的节点。
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        stack = []
        curr = slow.next
        slow.next = None
        while curr:
            stack.append(curr)
            curr = curr.next
        while head and stack:
            post = head.next
            head.next = stack.pop()
            head.next.next = post
            head = head.next.next
        return