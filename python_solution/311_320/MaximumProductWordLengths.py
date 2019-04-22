# 318. Maximum Product of Word Lengths

class Solution:
    # 对于word，我们用二进制表示，a表示末尾，以此类推。
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words or len(words) == 1:
            return 0
        maxLen = 0
        mask = [-1] * len(words)
        for i in range(len(words)):
            mask[i] = self.wordVal(words[i])
            for j in range(i):      # 我们诸葛比较j与i(j<i)，这样我们可以复用mask，节约时间。
                if mask[i] & mask[j] == 0:
                    maxLen = max(maxLen, len(words[i] * len(words[j])))
        return maxLen

    def wordVal(self, word):
        value = 0
        for char in word:
            value |= 1 << (ord(char) - ord("a"))    # 这里用或运算，对于重复元素，不影响结果，非重复元素会将结果对应的位置1
        return value