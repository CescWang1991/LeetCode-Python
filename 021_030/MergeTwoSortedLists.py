# 021. Merge Two Sorted Lists
# 023. Merge k Sorted Lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curr = ListNode(None)
        dummy.next = curr
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next.next

    # 推排序，将每个链表的头节点假如队列，按堆排序方法排序，将最小值节点加入结果，然后最小值所在的链表指向下一个节点
    # 调整堆并继续迭代，直到数组为空。
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        dummy = ListNode(None)
        curr = ListNode(None)
        dummy.next = curr
        heap = []
        # 注意数组中的元素为空
        for i in range(len(lists)):
            if lists[i]:
                heap.append(lists[i])
        # 将数组堆排序(省略)
        heap = sorted(heap, key=lambda x: x.val)
        while heap:
            curr.next = heap[0]
            curr = curr.next
            heap[0] = heap[0].next
            if not heap[0]:
                del heap[0]
                # 调整堆(省略)
            heap = sorted(heap, key=lambda x: x.val)

        return dummy.next.next