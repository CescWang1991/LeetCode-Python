# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。

# 运用python中的列表与字符串转换工具
class Solution1:
    def replaceSpace(self, s):
        lists = list(s.split(" "))
        s = "%20".join(lists)
        return s

# 由于替换空格后，字符串长度需要增大。先扫描空格个数，计算字符串应有的长度，从后向前一个个字符复制（需要两个指针）。
# 这样避免了替换空格后，需要移动的操作。
class Solution2:
    def replaceSpace(self, s):
        n = len(s)
        numSpace = 0
        for i in range(n):
            if s[i] == ' ':
                numSpace += 1
        p1 = len(s) - 1
        p2 = len(s) - 1 + 2 * numSpace
        t = [" " for i in range(len(s) + 2 * numSpace)]
        while p2 >= 0:
            if s[p1] == ' ':
                t[p2 - 2: p2 + 1] = ['%', '2', '0']
                p2 -= 3
            else:
                t[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return "".join(t)