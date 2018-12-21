# 82. Remove Duplicates from Sorted List II
# 83. Remove Duplicates from Sorted List

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
# 082解题(60ms)
class Solution2:
    def deleteDuplicates(self, head):
        dummy = ListNode(None)
        dummy.next = head
        cur = head
        dict = {}
        while cur:          # 第一次遍历，统计链表中各元素出现的次数
            val = cur.val
            dict[val] = dict.get(val, 0) + 1
            cur = cur.next
        cur = dummy
        while cur.next:     # 第二次遍历，删除出现一次以上的元素
            if dict[cur.next.val] > 1:      # 若next元素被删除，则指针不动
                cur.next = cur.next.next
            else:                           # 反之则右移一位
                cur = cur.next
        return dummy.next

# 083的解题
class Solution3:
    def deleteDuplicates(self, head):
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
