# 133. Clone Graph

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # 建立一个字典用来保存以克隆的图节点
    def __init__(self):
        self.dict = {}

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        copy = self.dict.get(node.label)
        if copy:    # 由于是无向图，可能存在重复遍历，若点已在dict，直接返回。
            return copy
        copy = UndirectedGraphNode(node.label)
        self.dict[copy.label] = copy
        # 利用深度优先遍历添加邻接点
        for temp in node.neighbors:
            copy.neighbors.append(self.cloneGraph(temp))
        return copy