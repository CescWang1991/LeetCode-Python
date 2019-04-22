# P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），则称其为“最大的”。
# 求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）

# 第一行输入点集的个数 N， 接下来 N 行，每行两个数字代表点的 X 轴和 Y 轴。

# 输出“最大的” 点集合， 按照 X 轴从小到大的方式输出，每行两个数字分别代表点的 X 轴和 Y轴。

# n = int(input("n = "))
# points = []
# for i in range(n):
#     [x, y] = list(map(int, input().split()))
#     points.append((x, y))


def findMaxPoints(points):
    """
    :type n: int
    :type points: list[tuple]
    :rtype: list[tuple]
    """
    if not points:
        return []

    points.sort(reverse=True)
    res = []
    max = 0

    for point in points:
        if point[1] > max:
            max = point[1]
            res.append(point)

    return res

points = [
    (298498081,747278511),
    (427131847,460128162),
    (939984059,817455089),
    (911902081,683024728),
    (474941318,6933274),
    (140954425,607811211),
    (336122540,629431445),
    (208240456,458323237),
    (646203300,469339106),
    (106410694,436340495)]

for p in findMaxPoints(points):
    print(p[0], p[1])