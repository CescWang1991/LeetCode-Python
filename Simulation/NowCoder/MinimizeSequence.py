# 序列最小化

# 有一个长度为N的序列。一开始，这个序列是1, 2, 3,... n - 1, n的一个排列。
# 对这个序列，可以进行如下的操作：
# 每次选择序列中k个连续的数字，然后用这k个数字中最小的数字替换这k个数字中的每个数字。
# 我们希望进行了若干次操作后，序列中的每个数字都相等。请你找出需要操作的最少次数。

# 输入描述:
# 第一行：两个数字n, k，含义如题，满足2 <= k <= n <= 10^5；
# 第二行：n个数字，是1, 2, 3,...n的一个排列。
#
# 输出描述:
# 一个整数，表示最少的次数。

def minSeq(n, k):
    time, temp = 0, 0
    while n >= k:
        sum = n // k
        temp = n % k
        time += sum
        n = sum + temp
    return time + 1 if temp else time

while True:
    try:
        line = input().split()
        n = int(line[0])
        k = int(line[1])
        print(minSeq(n, k))
    except:
        break