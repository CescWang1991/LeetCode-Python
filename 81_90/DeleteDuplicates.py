# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归调用：
# 当前node保留：
# head.next = delete(head.next)
# 当前node删除：
# head.val = delete(head.next).val
# head.next = delete(head.next)

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head

        dict = {}
        while node:
            if node.val not in dict.keys():
                dict[node.val] = 1
            else:
                dict[node.val] += 1
            node = node.next

        if not dict:
            return head
        else:
            return self.delete(head, dict)

    def delete(self, head, dict):
        dummy = ListNode(None)
        dummy.next = head
        if not head.next:
            if dict[head] != 1:
                return None
            else:
                return dummy.next
        else:
            if dict[head.val] != 1:
                nextNode = self.delete(head.next, dict)
                if nextNode:
                    head.val = nextNode.val
                    head.next = nextNode.next
                else:
                    return None
            else:
                head.next = self.delete(head.next, dict)

        return dummy.next