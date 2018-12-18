# 30. Substring with Concatenation of All Words

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []

        res = []
        wordDict = {}
        # 建立word字典，记录每一个word出现的次数
        for word in words:
            wordDict[word] = wordDict.get(word, 0) + 1

        length = len(words[0])
        for shift in range(length):
            begin = shift
            # 初始化一个word窗口字典，记录begin与当前指针之间的窗口中word的情况
            dict = {}
            for word in wordDict.keys():
                dict[word] = 0
            for curr in range(shift, len(s), length):
                currWord = s[curr:curr + length]
                # 当前遍历到的单词不在words中，将dict中所有的value为0，并且将begin index指向下一个遍历的curr
                if dict.get(currWord) == None:
                    for k in dict.keys():
                        dict[k] = 0
                    begin = curr + length
                # 当前遍历到的单词在words中，我们将dict中相应的value加一，然后比较两个dict
                else:
                    dict[currWord] += 1
                    # 此时从begin到curr+length的子串符合条件，我们将begin加入res。
                    # 并且在字典中将s[begin:begin+length]的value减一，begin换成begin+length。
                    if dict == wordDict:
                        res.append(begin)
                        dict[s[begin:begin + length]] -= 1
                        begin = begin + length
                    # 如果当前窗口的currWord次数大于wordDict中，那么条件不符合
                    elif dict[currWord] > wordDict[currWord]:
                        # 我们从begin开始遍历直到该单词之前出现的位置，将begin置于该位置+length
                        # 然后将遍历到的单词在dict中减一
                        temp = begin
                        for i in range(temp, curr, length):
                            dict[s[i:i+length]] -= 1
                            if s[i:i+length] == currWord:
                                begin = i + length
                                break
        return res