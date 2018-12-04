# 数字比较

# 牛牛很喜欢对数字进行比较，但是对于3 > 2这种非常睿智的比较不感兴趣。上了高中之后，学习了数字的幂，他十分喜欢这种数字表示方法，比如xy。
# 由此，他想出了一种十分奇妙的数字比较方法，给出两个数字x和y，请你比较xy和yx的大小，如果前者大于后者，输出">"，小于则输出"<"，等于则输出"="。

# 输入描述:
# 两个数字x和y。
# 满足1 <= x,y <= 10^9

# 输出描述:
# 一个字符，">"，"<"或者"="。

# 解答：比较指数问题，化为对数求解，左右同时取对数，ylogx和xlogy比大小。

import math

def numComp(x, y):
    loga = y * math.log(x)
    logb = x * math.log(y)
    if loga > logb:
        return ">"
    elif loga < logb:
        return "<"
    else:
        return "="

while True:
    try:
        line = input().split()
        n1 = int(line[0])
        n2 = int(line[1])
        print(numComp(n1, n2))
    except:
        break