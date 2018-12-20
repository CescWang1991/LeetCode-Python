# 068. Text Justification

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return ["" * maxWidth]
        res = [words[0]]
        space = []      # 记录当前行space的位置
        curLen = maxWidth - len(words[0])
        for i in range(1, len(words)):
            if curLen > len(words[i]):          # 向当前行添加该word
                space.append(len(res[-1]))
                res[-1] += " " + words[i]
                curLen -= (1+len(words[i]))
            else:                               # 添加新的一行，先处理最后一行
                if res[-1].count(" ") == 0:     # 最后一行无空格，即仅有一个单词，补足空格
                    print(res[-1], curLen)
                    res[-1] += " "* curLen
                else:                           # 向空格处添加均匀的空格
                    totalSpace = curLen
                    numSpace = len(space)
                    for pos in reversed(space):
                        curSpace = totalSpace // numSpace   # 当前的位置添加的空格数
                        res[-1] = res[-1][:pos] + (' ' * curSpace) + res[-1][pos:]
                        totalSpace -= curSpace
                        numSpace -= 1
                    space = []      # 处理完毕后space置为空
                res.append(words[i])
                curLen = maxWidth - len(words[i])
        res[-1] += " " * curLen

        return res