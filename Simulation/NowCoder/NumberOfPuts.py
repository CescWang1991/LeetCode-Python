# 牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
# 牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
# 牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。

# 输入包括两行
# 第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
# 第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。

def numPuts(nums, w):
    n = len(nums)
    if not nums or w <= 0:
        return 0
    if n == 1 and nums[0] > w:
        return 1
    if sum(nums) <= w:
        return 2**n
    return numPuts(nums[1:],w)+numPuts(nums[1:], w-nums[0])

w = 1165911996
nums = [842104736,
        130059605,
        359419358,
        682646280,
        378385685,
        622124412,
        740110626,
        814007758,
        557557315,
        40153082,
        542984016,
        274340808,
        991565332,
        765434204,
        225621097,
        350652062,
        714078666,
        381520025,
        613885618,
        64141537,
        783016950]
print(numPuts(sorted(nums, reverse=True), w))


while True:
    try:
        line = input().split()
        n, w = int(line[0]), int(line[1])
        nums = sorted(list(map(lambda x:int(x), input().split())))
        print(numPuts(nums,w))
    except:
        break