# 目的地最短步数
# 考虑你从家出发步行去往一处目的地，该目的地恰好离你整数单位步长（大于等于1）。你只能朝向该目的地或者背向该目的地行走，
# 而你行走的必须为单位步长的整数倍，且要求你第N次行走必须走N步。
# 请就给出目的地离你距离，判断你是否可以在有限步内到达该目的地。如果可以到达的话，请计算到达目的地的最短总步数(不能到达则输出-1)。

# 输入描述:
# 1个整数：目的地离你距离T

# 输出描述:
# 1个整数：最短总步数（进行了多少次行走）

# 解体思路：
# 广度优先遍历：从dist=0的点出发，将到达点的dist和step加入到队列当中，然后从队列头开始，检验dist是否和t相等；
# 相等时直接返回step，不相等则把到达点的dist和step加入到队列当中，然后删去队列头

# 答案正确:恭喜！您提交的程序通过了所有的测试用例

def minSteps(t):
    queue = [(0, 0)]
    while queue:
        dist = queue[0][0]
        step = queue[0][1]
        if dist == t:
            return step
        queue.append((dist+step+1, step+1))
        queue.append((dist-step-1, step+1))
        del queue[0]

    return -1

while True:
    try:
        t = int(input())
        print(minSteps(t))
    except:
        break