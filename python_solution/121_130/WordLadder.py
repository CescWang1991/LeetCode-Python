# 126. Word Ladder II
# 127. Word Ladder

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        # 建立字典，key为wordList中的每个单词
        res = []
        dict = {}
        for word in wordList:
            if word not in dict.keys():
                dict[word] = 0

        n = len(beginWord)
        minLayer = float('Inf')
        queue = [(beginWord, 1, [beginWord])]

        while queue:
            beginWord = queue[0][0]
            layer = queue[0][1]
            list = queue[0][2]
            if beginWord in dict.keys():
                del dict[beginWord]
            # 遍历单词中的每一位，从a-z替代，如果replaced在wordList中，则加入队列，并从list删除，layer是辅助层数, list是辅助队列；
            # 遍历完当前单词后，将其从队列中删除(pop头部)
            if layer < minLayer:
                for bit in range(n):
                    curr = beginWord
                    for code in range(97, 123):
                        replcaced = curr[:bit] + chr(code) + curr[bit+1:]
                        if replcaced == endWord:
                            res.append(list + [endWord])
                            minLayer = min(minLayer, layer+1)
                        if replcaced in dict.keys():
                            queue.append((replcaced, layer +1, list + [replcaced]))
                del queue[0]
            else:
                break

        return res


    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        # 建立字典，key为wordList中的每个单词
        dict = {}
        for word in wordList:
            if word not in dict.keys():
                dict[word] = 0

        n = len(beginWord)
        queue = [(beginWord, 1)]

        while queue:
            beginWord = queue[0][0]
            layer = queue[0][1]
            if beginWord in dict.keys():
                del dict[beginWord]
            # 遍历单词中的每一位，从a-z替代，如果replaced在wordList中，则加入队列，并从list删除，layer是辅助层数；
            # 遍历完当前单词后，将其从队列中删除(pop头部)
            for bit in range(n):
                curr = beginWord
                for code in range(97, 123):
                    replcaced = curr[:bit] + chr(code) + curr[bit+1:]
                    if replcaced == endWord:
                        return layer + 1
                    if replcaced in dict.keys():
                        queue.append((replcaced, layer+1))
            del queue[0]

        return 0