class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def initList(nums):
    dummy = ListNode(None)
    if not nums:
        return dummy

    p = dummy
    for num in nums:
        p.next = ListNode(num)
        p = p.next

    return dummy.next


def printList(head):
    if not head:
        return None

    while head:
        print(head.val)
        head = head.next


# Reverse a singly linked list.
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
def ReverLinkList(head):
    '''
    :param head: ListNode
    :return: ListNode
    '''
    if not head:
        return None

    post = None
    while head:
        p = head
        head = head.next
        p.next = post
        post = p

    return post


nums = [1, 2, 3, 4, 5]
printList(ReverLinkList(initList(nums)))
