# 243. Shortest Word Distance [https://blog.csdn.net/jmspan/article/details/51082268]

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution:
    # 从左到右扫描，记录word1和word2的最新位置，比较两个最新位置的距离与最短距离。时间复杂度O(n)
    def shortestDistance(self, words, word1, word2):
        if not words:
            return 0
        pos1, pos2 = -1, -1
        dist = len(words) - 1
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
                if pos2 != -1:
                    dist = min(dist, pos1 - pos2)
            if words[i] == word2:
                pos2 = i
                if pos1 != -1:
                    dist = min(dist, pos2 - pos1)

        return dist

# 244. Shortest Word Distance II [https://blog.csdn.net/qq508618087/article/details/50887452]

# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your
# method will be called repeatedly many times with different parameters. How would you optimize it?

# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 
# and word2 and return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class WordDistance:
    # 先记录每个单词在数组中的位置，然后对两个单词的所有位置顺序扫描。
    def __init__(self, words):
        self.words = words
        self.dict = self.buildDict(words)

    def buildDict(self, words):
        dict = {}
        for i in range(len(words)):
            if not dict.get(words[i]):
                dict[words[i]] = [i]
            else:
                dict[words[i]].append(i)
        return dict

    def shortestDistance(self, word1, word2):
        pos1 = self.dict[word1]
        pos2 = self.dict[word2]
        dist = len(self.words) - 1
        i, j = 0, 0
        while i < len(pos1) and j < len(pos2):
            if pos1[i] < pos2[j]:
                dist = min(dist, pos2[j] - pos1[i])
                i += 1
            else:
                dist = min(dist, pos1[i] - pos2[j])
                j += 1
        return dist

# 245. Shortest Word Distance III [https://blog.csdn.net/xinqrs01/article/details/54312839]

# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = "makes", word2 = "makes", return 3.

# Note:
# You may assume word1 and word2 are both in the list.

class Solution3:
    # 对于word1==word2的情形单独处理，只需要将pos2赋值给pos1，pos2更新为i即可。
    def shortestDistance(self, words, word1, word2):
        if not words:
            return 0
        pos1, pos2 = -1, -1
        dist = len(words) - 1
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = pos2 if word1 == word2 else i
            if words[i] == word2:
                pos2 = i
            dist = min(dist, abs(pos1 - pos2))

        return dist