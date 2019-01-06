# 297. Serialize and Deserialize Binary Tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 非递归解法，利用队列queue解决BFS问题
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[null]"
        queue = [root]
        data = []
        while queue:
            curr = queue[0]
            if curr:
                data.append(str(curr.val))
            else:
                data.append("null")
            del queue[0]
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
        return "[" + ",".join(data) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "[null]":
            return None
        data = data[1:-1].split(",")
        root = TreeNode(int(data[0]))
        del data[0]
        queue = [root]
        while queue:
            curr = queue[0]
            del queue[0]
            if curr:
                if data:        # 注意遍历到叶节点时，data为空问题，这时所有叶节点左右子树赋予None
                    curr.left = TreeNode(int(data[0])) if data[0] != "null" else None
                    queue.append(curr.left)
                    del data[0]
                else:
                    curr.left = None
                if data:
                    curr.right = TreeNode(int(data[0])) if data[0] != "null" else None
                    queue.append(curr.right)
                    del data[0]
                else:
                    curr.right = None

        return root

class Codec2:
    # 递归解法，生成树的前序遍历[这里会记录空树]，形成字符串
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        self.serializeTree(root, data)
        return ",".join(data)
    # 对于去序列化，我们先读入第一个字符，以此生成一个根节点，然后再对根节点的左右子节点递归调用去序列化函数即可
    # 注意生成树结点后，要将data从队首删除。
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        root = self.deserializeData(data)
        return root

    def serializeTree(self, root, data):
        if root:
            data.append(str(root.val))
            self.serializeTree(root.left, data)
            self.serializeTree(root.right, data)
        else:
            data.append("null")

    def deserializeData(self, data):
        if data[0] != "null":
            root = TreeNode(int(data[0]))
            del data[0]
            root.left = self.deserializeData(data)
            root.right = self.deserializeData(data)
            return root
        else:
            del data[0]
            return None