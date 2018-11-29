# K点游戏
# 小招喵某日闲来无事，想验一下自己的人品，于是给自己定了一个游戏规则：
# 这个游戏有三个因素：N，K，W
# 游戏开始的时候小招喵有0点，之后如果发现自己手上的点不足K点，就随机从1到W的整数中抽取一个（包含1和W），抽到哪个数字的概率都是相同的。
# 重复上述过程，直到小招喵获得了K或者大于K点，就停止获取新的点，这时候小招喵手上的点小于等于N的概率是多少？

# 输入：N = 5， K = 1， W = 5
# 输出：1.00000
# 说明：开始有0点，不足1点，从[1,5]中随机取一个整数（一共5个数字，所以每个数字取到的概率都是1/5），获得后得分无论如何都大于了1点，停止，概率为1

# 输入：N = 6， K = 1， W = 10
# 输出：0.60000
# 说明：开始有0点，不足1点，从[1,10]中随机取一个整数（一共10个数字，所以每个数字取到的概率都是1/10），获得后有6/10的概率小于6点，且满足大于1点的条件，概率为0.6

# dynamic programming: dp[i]表示和为i的概率，dp[i] = prob(dp[i-1]+...+dp[i-w]) if i-w >= 0

def getProb(n, k, w):
    dict = {}
    total = 0
    for i in range(1, w+1):
        for j in range(k, n+1):
            sum = j - i
            if sum in range(k):
                if not dict.get(sum):
                   dict[sum] = 1
                else:
                   dict[sum] += 1
    dp = setProb(k, w)
    for key, value in dict.items():
        total += value * dp[key] * 1.0 / float(w)
    return total

def setProb(k, w):
    prob = 1.0 / float(w)
    dp = [0] * k
    dp[0] = 1
    for i in range(1, k):
        for j in range(1, w):
            dp[i] += prob * dp[i-j] if i >= j else 0
    return dp


while True:
    try:
        line = input().split()
        n, k, w = int(line[0]), int(line[1]), int(line[2])
        print(getProb(n,k,w))
    except:
        break