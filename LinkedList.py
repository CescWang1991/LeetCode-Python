# 定义链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 初始化链表
def initList(nums):
    dummy = ListNode(None)
    if not nums:
        return dummy

    p = dummy
    for num in nums:
        p.next = ListNode(num)
        p = p.next

    return dummy.next

# 打印链表
def printList(head):
    if not head:
        return None

    while head:
        print(head.val)
        head = head.next

# LeetCode 206
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

# LeetCode 25
# Reverse Nodes in k-group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
# multiple of k then left-out nodes in the end should remain as it is.
