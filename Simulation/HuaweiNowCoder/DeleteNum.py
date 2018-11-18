# 有一个数组a[N]顺序存放0~N-1，要求每隔两个数删掉一个数，到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。
# 以8个数(N=7)为例:｛0，1，2，3，4，5，6，7｝，0->1->2(删除)->3->4->5(删除)->6->7->0(删除),如此循环直到最后一个数被删除。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNums(head):
    if not head:
        return None

    dummy = ListNode(None)
    dummy.next = head
    count = 0
    while head:
        # 不删除head.next，如果head.next不为空，则head = head.next；为空，则head为链表尾部，head设为链表头节点。
        if count == 0:
            if head.next:
                head = head.next
            else:
                head = dummy.next
            count += 1
        # 删除head.next。
        elif count == 1:
            # head.next不为空，删除head.next，next指针指向head.next.next，若更新后的head.next为空，则head指向头节点。
            if head.next:
                head.next = head.next.next
                if head.next:
                    head = head.next
                else:
                    head = dummy.next
            # head.next为空，则当前节点为尾节点，我们删除链表的头节点，将head设为头节点的next；
            # 当头节点的next为空时，即链表仅有一个头节点，这时返回节点值，就是我们要的结果。
            else:
                if dummy.next.next:
                    dummy.next = dummy.next.next
                    head = dummy.next
                else:
                    return dummy.next.val
            count = 0

    return dummy.next.val

while True:
    try:
        n = int(input())
        dummy = ListNode(None)
        if n:
            head = ListNode(0)
            dummy.next = head
            for i in range(1,n):
                head.next = ListNode(i)
                head = head.next
        print(deleteNums(dummy.next))
    except:
        break