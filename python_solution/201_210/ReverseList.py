# 206. Reverse List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 运用递归方法(64ms):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # reverseList(head)返回输入的链表反转后的head，那么如果reverseList(head.next)的话
        # 1(head)->2<-3<-4<-5(ans)
        ans = self.reverseList(head.next)
        # 我们此时只需要head.next.next=head，也就是先建立一个双向连接
        # 1(head)<-2<-3<-4<-5(ans)
        head.next.next = head
        # 然后再head.next=None，返回ans即可
        # null<-1(head)<-2<-3<-4<-5(ans)
        head.next = None

        return ans

class Solution2:

    # 运用迭代方法(48ms)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        reverse = None
        while head:
            next = reverse
            reverse = head
            head = head.next
            reverse.next = next

        return reverse