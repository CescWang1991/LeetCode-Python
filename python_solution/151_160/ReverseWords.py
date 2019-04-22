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


# 186. Reverse Words in a String II

# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

# The input string does not contain leading or trailing spaces and the words are always separated by a single space.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Could you do it in-place without allocating extra space?

class Solution2:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(reversed(s))      # 翻转字符串，再将每个单词翻转，python的str无法更改，用list代替
        i = j = 0
        while i < len(s) and j < len(s):
            if j == len(s) - 1:     # 处理最后的一个单词
                s[i:j+1] = self.reverseOneWord(s[i:j+1])
                break
            elif s[j] != " ":
                j += 1
            elif s[j] == " ":
                print(s[i:j])
                s[i:j] = self.reverseOneWord(s[i:j])
                j += 1
                i = j
        return "".join(s)

    def reverseOneWord(self, word):
        for i in range(len(word)//2):
            word[i], word[len(word)-1-i] = word[len(word)-1-i], word[i]
        return word