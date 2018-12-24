# 156. Binary Tree Upside Down

# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same
# parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left
# leaf nodes. Return the new root.

# Given a binary tree {1,2,3,4,5},
# return the root of the binary tree [4,5,2,#,#,3,1].

#         1                                     4(node)
#       / \                                   /  \
#     2   3    =>      4(node) 1    =>      5     2
#   /  \             /  \   /  \                /  \
# 4    5           5     2(root)3             3    1(root)

class Solution:
    # 把左子树继续颠倒，颠倒完后，原来的那个左孩子的左右孩子指针分别指向原来的根节点以及原来的右兄弟节点即可。
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root
        node = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right     # node.left
        root.left.right = root          # node.right
        root.left = None
        root.right = None
        return node