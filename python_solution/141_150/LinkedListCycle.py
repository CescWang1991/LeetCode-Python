# Linked List Cycle
# Linked List Cycle II

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 快慢指针，慢指针每次走一步，快指针每次走两步，当快指针和慢指针相同时，则证明有环。
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

class Solution2(object):
    # 相遇时的位置(m)再前进x步，正好是y的整倍数即整圈。
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast and slow:
                    if slow == fast:    # 先比较，因为循环点可能是0，此时slow和fast相同。
                        return slow
                    slow = slow.next
                    fast = fast.next

        return None