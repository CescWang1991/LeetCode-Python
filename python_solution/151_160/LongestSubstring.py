# 159. Longest Substring with At Most Two Distinct Characters

# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

# TFor example, Given s = “eceba”,

# T is "ece" which its length is 3.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s: return 0

        dict = {}
        maxLen = 0
        for i in range(len(s)):
            # map为空，或者当前元素存在重复，或者只有一种字母
            if s[i] in dict.keys():
                dict[s[i]].append(i)
            elif not dict.keys() or len(dict.keys()) == 1:
                dict[s[i]] = [i]
            else:   # 当前元素为第三元素，s[i-1]为保留的元素，还有一个元素从map删除
                delete = ""
                for k, v in dict.items():
                    if k != s[i-1]:
                        delete = k
                        break
                last = dict[delete][-1]     # last元素之后的元素到i之间，都是保留的元素
                del dict[delete]
                dict[s[i-1]] = list(range(last+1, i))
                dict[s[i]] = [i]    # 添加新元素
            length = sum(list(map(lambda x:len(x), dict.values()))) # 长度是value的长度和
            maxLen = max(maxLen, length)

        return maxLen