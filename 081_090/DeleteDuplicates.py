# 82. Remove Duplicates from Sorted List II
# 83. Remove Duplicates from Sorted List
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
        # 用hash table存放链表中值出现的次数
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
        # head是尾节点时
        if not head.next:
            if dict[head] != 1:
                return None
            else:
                return dummy.next
        else:
            # 删除head：
            # head.val = delete(head.next).val
            # head.next = delete(head.next)
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

    def removeDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(None)
        dummy.next = head

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next
