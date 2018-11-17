# 126. Word Ladder II

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        if endWord not in wordList:
            return res

        if self.distance(beginWord, endWord) == 1:
            return [[beginWord, endWord]]

        for word in wordList:
            if self.distance(beginWord, word) == 1:
                # 在这里使用copy方法，这样在remove word的时候，不会影响到wordList。
                words = wordList.copy()
                words.remove(word)
                post = self.findLadders(word, endWord, words)
                if post:
                    for l in post:
                        res.append([beginWord] + l)

        if res:
            minLen = min(list(map(lambda x:len(x), res)))
            res = list(filter(lambda x:len(x)==minLen, res))

        return res


    def distance(self, w1, w2):
        if len(w1) != len(w2):
            return -1

        dist = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                dist += 1

        return dist


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().findLadders(beginWord, endWord, wordList))