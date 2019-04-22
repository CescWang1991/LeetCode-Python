# 输入一个字符串，求出该字符串包含的字符集合

# 输入描述:
#         每组数据输入一个字符串，字符串最大长度为100，且只包含字母，不可能为空串，区分大小写。

# 输出描述:
#         每组数据一行，按字符串原有的字符顺序，输出字符集合，即重复出现并靠后的字母不输出。

def stringSet(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s

    pos = 0
    dict = {}
    for c in s:
        if c not in dict.keys():
            dict[c] = pos
            pos += 1

    length = len(dict)
    s = ["0"] * length
    for k, v in dict.items():
        s[v] = k

    return "".join(s)

while True:
    try:
        s = input()
        print(stringSet(s))
    except:
        break