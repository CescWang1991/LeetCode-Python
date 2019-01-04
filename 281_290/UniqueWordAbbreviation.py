# 288. Unique Word Abbreviation 独特的单词缩写

# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
# a) it                      --> it    (no abbreviation)
#      1
# b) d|o|g                   --> d1g
#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's
# abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Example:
#
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true

class Solution:
    # 建立一个字典，保存每个缩写所对应的word列表
    def ValidWordAbbr(self, words):
        """
        :param words:
        :return:
        """
        self.words = dict()
        for word in words:
            abbr = word[0] + str(len(word[1:-1])) + word[-1] if len(word[1:-1]) != 0 else word
            if not self.words.get(abbr):
                self.words[abbr] = [word]
            else:
                self.words[abbr].append(word)
        return

    def isUnique(self, word):
        abbr = word[0] + str(len(word[1:-1])) + word[-1] if len(word[1:-1]) != 0 else word
        if not self.words.get(abbr):        # 缩写不存在dict中，如cart，返回True
            return True
        # 缩写存在，但对应的word只有一个且就是自己，返回True
        elif len(self.words[abbr]) == 1 and word in self.words[abbr]:
            return True
        else:
            return False