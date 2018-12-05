# 207. Course Schedule
# 210. Course Schedule II

class Solution:
    # 可以利用宽度优先遍历的思想完成。
    # 设置一个count 记录输出的顶点个数，用一个队列记得当前入度为0的结点。从入度为 0 的结点入队。
    # 然后队列不空的时候循环执行，出队，将出队顶点输出，count++，将由此顶点引出的边所指向的顶点的入度都减1，并且将入度变成0的顶点入队，队列为空退出，排序结束。
    def canFinishBFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        # 维持一个 indegree 数组，表示每个顶点的入度
        indegree = [0] * numCourses
        # 构造一个 dict，key为出发点，value为所有从key出发到的点的集合(大大加快运行速度)
        dict = {}
        # 构造邻接表
        for i in range(len(prerequisites)):
            edge = prerequisites[i]
            src = edge[1]
            dst = edge[0]
            if not dict.get(src):
                indegree[dst] += 1
                dict[src] = [dst]
            elif dst not in dict[src]:
                indegree[dst] += 1
                dict[src].append(dst)

        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            course = queue[-1]
            count += 1
            del queue[-1]
            if dict.get(course):
                for i in dict[course]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)

        return count == numCourses

    # 利用深度优先遍历
    def canFinishDFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        # 维持一个outdegree数组，表示每个顶点的出度
        outdegree = [0] * numCourses
        matrix = [[0] * numCourses for i in range(numCourses)]

        for i in range(len(prerequisites)):
            edge = prerequisites[i]
            src = edge[1]
            dst = edge[0]
            if matrix[src][dst] == 0:
                outdegree[src] += 1
            matrix[src][dst] = 1

        stack = []
        for i in range(numCourses):
            if outdegree[i] == 0:
                stack.append(i)

        count = 0
        while stack:
            print(stack, outdegree, matrix)
            course = stack.pop()
            count += 1
            for i in range(numCourses):
                if matrix[i][course] != 0:
                    outdegree[i] -= 1
                    if outdegree[i] == 0:
                        stack.append(i)

        return count == numCourses

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return [i for i in range(numCourses)]

        order = []
        # 构建邻接字典和入度数组
        dict = {}
        indegree = [0] * numCourses

        for edge in prerequisites:
            src = edge[1]
            dst = edge[0]
            if not dict.get(src):
                indegree[dst] += 1
                dict[src] = [dst]
            else:
                indegree[dst] += 1
                dict[src].append(dst)

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue[-1]
            order.append(curr)
            del queue[-1]
            if dict.get(curr):
                for i in dict[curr]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)

        return order if len(order) == numCourses else []