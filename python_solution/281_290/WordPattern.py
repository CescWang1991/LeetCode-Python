# 290. Word Pattern

class Solution:
    # 与#205. Isomorphic Strings相似，用双字典来对应pattern与str中对应位置的字符
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(" ")
        p = dict()
        s = dict()
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            if not p.get(pattern[i]) and not s.get(str[i]):
                p[pattern[i]] = str[i]
                s[str[i]] = pattern[i]
            elif p.get(pattern[i]) and s.get(str[i]):
                if p[pattern[i]] == str[i] and s[str[i]] == pattern[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True

class Solution2:
    # 运用一个字典来解决
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word = dict()
        str = str.split(" ")
        for i in range(len(pattern)):
            if not word.get(pattern[i]):        # 若字符不在哈希表中，首先检查单词是否再哈希表中
                if str[i] in word.values():     # 若单词在哈希表中，则有另外的字符对应该单词，返回False
                    return False
                else:
                    word[pattern[i]] = str[i]
            else:
                if word[pattern[i]] != str[i]:
                    return False
        return True

# 291. Word Pattern II

# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
#
# Example 1:
#
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
# Example 2:
#
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
# Example 3:
#
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false
# Notes:
# You may assume both pattern and str contains only lowercase letters.

class Solution3:
    # 运用基于深度优先搜索的回溯算法
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        map = dict()
        return self.dfs(pattern, str, map)
    # 函数dfs返回基于当前pattern，str与哈希表的匹配结果
    def dfs(self, pattern, str, map):
        print(pattern, str, map)
        if not pattern and not str:
            return True
        if len(pattern) > len(str) or (not pattern and str) or (pattern and not str):
            return False
        p = pattern[0]
        for i in range(1, len(str)+1):      # 循环遍历取当前字符串前i位的不同情况，若出现不符合的情况，则直接continue，若
                                            # 符合，则递归调用后面的字符，字符串以及更新的哈希表
            s = str[:i]
            temp = map.copy()               # 注意对当前的map进行copy，因为哈希表是地址传递
            if not temp.get(p):             # 当前字符不在哈希表中，首先检查单词是否再哈希表中
                if s not in temp.values():
                    temp[p] = s
                    if self.dfs(pattern[1:], str[i:], temp):
                        return True
            else:                           # 当前字符在哈希表中
                if temp[p] == s:
                    if self.dfs(pattern[1:], str[i:], temp):
                        return True
        return False