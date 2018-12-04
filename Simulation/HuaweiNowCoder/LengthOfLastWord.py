# 字符串最后一个单词的长度
# 计算字符串最后一个单词的长度，单词以空格隔开。

# 输入描述:
# 一行字符串，非空，长度小于5000。

# 输出描述:
# 整数N，最后一个单词的长度。

def lastLength(s):
    if not s:
        return 0
    n = len(s)
    length = 0
    for i in reversed(range(n)):
        if length == 0 and s[i] == " ":
            continue
        else:
            if s[i] != " ":
                length += 1
            else:
                return length

    return length

while True:
    try:
        s = input()
        print(lastLength(s))
    except:
        break