# 002. Add Two Numbers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 计算头结点的和，将结果赋值给了，并计算carry
        sum = l1.val + l2.val
        ans = sum % 10
        carry = sum // 10
        res = ListNode(ans)
        # 遍历了l1和l2，其中用next是因为在结束时，我们要将l1, l2指向最后一个非null结点，这样可以在后面继续添加1
        l3 = res
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            sum = l1.val + l2.val + carry
            ans = sum % 10
            carry = sum // 10
            l3.next = ListNode(ans)
            l3 = l3.next
        # l1的长度大于l2，直接在l1上修改值
        while l1.next:
            l1 = l1.next
            sum = l1.val + carry
            ans = sum % 10
            carry = sum // 10
            l3.next = ListNode(ans)
            l3 = l3.next
        # l2的长度大于l1，直接在l1上添加结点
        while l2.next:
            l2 = l2.next
            sum = l2.val + carry
            ans = sum % 10
            carry = sum // 10
            l3.next = ListNode(ans)
            l3 = l3.next

        if not l1.next and not l2.next and carry == 1:
            l3.next = ListNode(1)

        return res