# 310. Minimum Height Trees

class Solution:
    # 一层一层的褪去叶节点，最后剩下的一个或两个节点就是我们要求的最小高度树的根节点
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        connects = dict()       # connects记录每一个节点连接的边个数
        if not edges:
            return [i for i in range(n)]
        for edge in edges:
            connects[edge[0]] = connects.get(edge[0], 0) + 1
            connects[edge[1]] = connects.get(edge[1], 0) + 1
        while edges and len(edges) > 1:
            i = 0
            src = dict((k, v) for k, v in connects.items() if v == 1)   # 将所有边个数为1的节点放入src中
            while i < len(edges):           # 如果一条边的其中一个点属于src，则将这条边删除，并将这个点从connects中删除，
                                            # 并且另一个点的value减一，直到edges没有边或只有一条边。
                if src.get(edges[i][0]):
                    connects[edges[i][1]] -= 1
                    del connects[edges[i][0]]
                    del edges[i]
                elif src.get(edges[i][1]):
                    connects[edges[i][0]] -= 1
                    del connects[edges[i][1]]
                    del edges[i]
                else:
                    i += 1
        return list(connects.keys())