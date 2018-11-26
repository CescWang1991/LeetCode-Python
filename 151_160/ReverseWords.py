# 151. Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        # 翻转字符，并且过滤空字符
        words = list(reversed(words))
        words = list(filter(lambda x: x, words))
        reverse = " ".join(words)
        return reverse