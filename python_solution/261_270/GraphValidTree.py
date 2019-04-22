# 261. Graph Valid Tree

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function
# to check whether these edges make up a valid tree.

# For example:
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Hint:
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are
# connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the
# same as [1, 0] and thus will not appear together in edges.

class Solution:
    # 运用并查集，对于根节点，其集合为-1，若是联通的图，只有一个点的集合是负数。同时，对于cycle，edge的src和dst会返回同一个集合。
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: list[tuple[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:     # 所有node标记0到n-1.通过观察可以知道要把所有node连起来并且没有重复的edge的size必须是n-1!
            return False
        self.nums = [-1 for i in range(n)]
        for edge in edges:
            x = self.find(edge[0])      # 返回src的集合
            y = self.find(edge[1])      # 返回dst的集合
            if x == y:                  # 两者相同则存在cycle
                return False
            self.nums[edge[1]] = x      # Union操作，将一条边的dst并到它的src所在的集合
            print(self.nums)
        return True

    def find(self, index):              # Find操作，返回点所在的集合
        if self.nums[index] == -1:
            return index
        else:
            return self.find(self.nums[index])