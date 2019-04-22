# 320. Generalized Abbreviation

# Write a function to generate the generalized abbreviations of a word.

# Example:

# Given word = "word", return the following list (order does not matter):

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

class Solution:
    # 凡是0的地方都是原来的字母，单独的1还是1，如果是若干个1连在一起的话，就要求出1的个数，用这个数字来替换对应的字母
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: list[str]
        """
        if not word:
            return []
        length = len(word)
        res = [str(length)]
        for i in range(length * length - 1):
            form = '{:0'+str(length)+'b}'
            binary = str(form.format(i))
            count = 0
            abbr = ""
            for j in range(length):
                if binary[j] == "0":
                    if count != 0:
                        abbr += str(count)
                    abbr += word[j]
                    count = 0
                else:
                    count += 1
            if count != 0:
                abbr += str(count)
            res.append(abbr)
        return res