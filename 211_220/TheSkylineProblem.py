# 218. The Skyline Problem

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        curr, curr_x, curr_h = 0, -1, -1
        length = len(buildings)
        livebld = []
        res = []

        while curr < length or livebld:
            # 如果是最开始处理建筑，或者出现建筑物不连续的情况（即对于上面第4个建筑和第3个建筑分开的情况）
            curr_x = buildings[curr][0] if not livebld else livebld[0][1]  # 最高建筑的结束点
            if curr >= length or buildings[curr][0] > curr_x:
                # 将结束时间小于等于最高建筑结束点的哪些建筑物从优先队列中弹出
                while livebld and livebld[0][1] <= curr_x:
                    del livebld[0]
            else:
                # 如果当前遍历到的建筑物在最高的建筑物结束之前开始，那么处理当前的建筑物
                curr_x = buildings[curr][0]
                while curr < length and buildings[curr][0] == curr_x:   # 处理所有在同一点开始的建筑物
                    livebld.insert(0, [buildings[curr][2], buildings[curr][0]])
                    curr += 1

            curr_h = 0 if not livebld else livebld[0][0]   # 输出最顶端的建筑物的高度
            if not res or res[-1][1] != curr_h:
                res.append([curr_x, curr_h])
            print(res, livebld)

        return res


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
Solution().getSkyline(buildings)