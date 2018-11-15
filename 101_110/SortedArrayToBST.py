# 108. Convert Sorted Array to Binary Search Tree
# 109. Convert Sorted List to Binary Search Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 以数组的中点作为跟节点，将数组分为左右两边，递归调用生成左右子树
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        n = len(nums)
        root = TreeNode(nums[n//2])
        if nums[:n//2]:
            root.left = self.sortedArrayToBST(nums[:n//2])
        if nums[(n//2+1):]:
            root.right = self.sortedArrayToBST(nums[(n//2+1):])

        return root

    # 按照中序遍历的思路，应该先生成左子树，然后是根节点，最后的右子树。
    # 先计算链表的长度，然后将中点作为根节点，然后用递归的方法进行中序遍历。这里的辅助函数以链表的头尾节点位置作为输入。
    # 定义node位global变量，每当被遍历时生成节点时，指向node的next。
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        size = 0
        global node
        node = head

        while head:
            head = head.next
            size += 1

        return self.inorderHelper(0, size-1)

    def inorderHelper(self, s, e):
        global node
        if s > e:
            return None

        mid = (s+e)//2
        left = self.inorderHelper(s, mid-1)

        root = TreeNode(node.val)
        node = node.next
        root.left = left

        right = self.inorderHelper(mid+1, e)
        root.right = right

        return root