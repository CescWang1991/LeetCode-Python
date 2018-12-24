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
            if not dict.keys() or len(dict.keys()) == 1:
                dict[s[i]] = [i]
            elif s[i] in dict.keys():
                dict[s[i]].append(i)
            else:   # 当前元素为第三元素，s[i-1]为保留的元素，还有一个元素从map删除
                delete = ""
                for k, v in dict.items():
                    if k != s[i-1]:
                        delete = k
                        break
                del dict[delete]
                # 对于保留元素，其index必须连续，我们将index从后往前遍历，保留连续的坐标
                index = dict[s[i-1]]
                shift = 1
                for j in reversed(range(len(index))):
                    if index[j] != i - shift:
                        dict[s[i-1]] = index[i+1:]
                        break
                    shift += 1
                dict[s[i]] = [i]    # 添加新元素
            length = sum(list(map(lambda x:len(x), dict.values()))) # 长度是value的长度和
            maxLen = max(maxLen, length)

        return maxLen