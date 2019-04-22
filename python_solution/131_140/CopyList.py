# 138. Copy List with Random Pointer

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        self.dict = {}

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        copy = self.dict.get(head)
        if copy:
            return copy
        copy = RandomListNode(head.label)
        self.dict[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.copyRandomList(head.random)

        return copy