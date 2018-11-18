# 写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入）

def convert(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    d = 0
    l = len(s)
    for i in range(l):
        if s[i] == "A":
            d += 10 * 16 ** (l - i - 1)
        elif s[i] == "B":
            d += 11 * 16 ** (l - i - 1)
        elif s[i] == "C":
            d += 12 * 16 ** (l - i - 1)
        elif s[i] == "D":
            d += 13 * 16 ** (l - i - 1)
        elif s[i] == "E":
            d += 14 * 16 ** (l - i - 1)
        elif s[i] == "F":
            d += 15 * 16 ** (l - i - 1)
        elif s[i].isdigit():
            d += int(s[i]) * 16 ** (l - i - 1)
    return str(d)

while True:
    try:
        s = input()
        if s:
            print(convert(s))
    except:
        break