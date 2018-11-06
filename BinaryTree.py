# 定义二叉树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insertleft(self, value):
        self.left = TreeNode(value)
        self.left.parent = self
        return self.left

    def insertright(self, value):
        self.right = TreeNode(value)
        self.right.parent = self
        return self.right

    def show(self):
        print(self.val)


def preorder(node):
    if node.val:
        node.show()
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)


# 中序遍历函数
def inorder(node):
    if node.val:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)


# 后序遍历函数
def postorder(node):
    if node.val:
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        node.show()


# 宽度优先遍历
def breadthFirstSearch(node):
    queue = []
    if node.val:
        print(node.val)
        queue.append(node)

    while queue:
        node = queue[0]
        if node.left:
            print(node.left.val)
            queue.append(node.left)

        if node.right:
            print(node.right.val)
            queue.append(node.right)

        del queue[0]


# build tree
node1 = TreeNode(3)                 # Layer 1

node2 = node1.insertleft(2)         # Layer 2
node3 = node1.insertright(5)

node4 = node2.insertleft(1)         # Layer 3
node5 = node2.insertright(7)
node6 = node3.insertleft(None)
node7 = node3.insertright(8)