# 269.  Alien Dictionary

# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You
# receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this
# new language. Derive the order of letters in this language.

# Input: ["wrt", "wrf", "er", "ett", "rftt"]
# Output: "wertf"

# Input: ["z", "x"]
# Output: "zx"

# Input:["z", "x", "z"]
# Output: ""
# Explanation: The order is invalid, so return "".

class Solution:
    # 有向图拓普排序问题，根据所给的单词顺序给出字母间的指向，最后将出现的所有字母拓普排序
    def alienOrder(self, words):
        """
        :type s: list[str]
        :rtype: str
        """
        length = len(words[0])
        pairs = []
        chars = set()
        chars.add(words[0][0])
        # 对于所有单词的第一个字母，只要相邻的不同，就确定一条有向边
        for i in range(1, len(words)):
            length = max(len(words[i-1]), len(words[i]))
            chars.add(words[i][0])
            if words[i-1][0] != words[i][0]:
                pairs.append([words[i-1][0], words[i][0]])
        bit = 1
        # 对于之后的第i个字母，只有相邻的单词前i-1项都相同并且第i项不同，才确定一条有向边
        while bit < length:
            if len(words[0]) > bit:
                chars.add(words[0][bit])
            for i in range(1, len(words)):
                if len(words[i]) > bit:
                    chars.add(words[i][bit])
                    if len(words[i-1]) > bit and words[i-1][:bit] == words[i][:bit] and words[i-1][bit] != words[i][bit]:
                        pairs.append([words[i-1][bit], words[i][bit]])
            bit += 1
        print(pairs)
        # 现在我们对chars中的字母(顶点)。根据pairs(有向边)拓普排序，参见#207. Course Schedule和#210. Course Schedule II
        indegree = {}   # 构建入度字典
        edges = {}      # 构建邻接字典
        for elem in chars:
            indegree[elem] = 0
        for pair in pairs:
            indegree[pair[1]] += 1
            if not edges.get(pair[0]):
                edges[pair[0]] = [pair[1]]
            else:
                edges[pair[0]].append(pair[1])
        queue = []      # 将入度为0的点加入队列
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)
        order = []
        while queue:
            curr = queue[0]                  # 取队首元素
            order.append(curr)
            del queue[0]
            if edges.get(curr):
                for elem in edges[curr]:    # 与当前元素相连的点的入度均减一
                    indegree[elem] -= 1
                    if indegree[elem] == 0: # 若元素的入度为0，则加入队列
                        queue.append(elem)
        return order if len(order) == len(chars) else []