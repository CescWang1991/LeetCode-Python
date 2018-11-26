# 30. Substring with Concatenation of All Words
# 此方法只适用于words不重复

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
        wl = len(words[0])
        for shift in range(wl):
            begin = shift
            dict = {}
            for curr in range(shift, len(s), wl):
                print(s[curr:curr+wl], dict, begin)
                # 当前遍历到的单词不在words中，直接清空dict，并且将begin index指向下一个遍历的curr
                if s[curr:curr+wl] not in words:
                    dict = {}
                    begin = curr + wl
                else:
                    # 如果当前子串不在dict中，我们将其添加，并比较字典与words的长度。
                    if not dict.get(s[curr:curr+wl]):
                        dict[s[curr:curr+wl]] = curr
                        # 此时从begin到curr+wl的子串符合条件，我们将begin加入res。
                        # 并且在字典中删去s[begin:begin+wl]，begin换成begin+wl
                        if len(dict) == len(words):
                            res.append(begin)
                            del dict[s[begin:begin+wl]]
                            begin = begin + wl
                    # 如果s[curr:curr+wl]存在于字典中，该子串之前出现的位置在dict[s[curr:curr+wl]]
                    # 我们将它之前的单词从del删除(包括)，然后dict[s[curr:curr+wl]]=curr，begin
                    else:
                        temp = begin
                        begin = dict[s[curr:curr+wl]] + wl
                        for i in range(temp, dict[s[curr:curr+wl]], wl):
                            del dict[s[i:i+wl]]
                        dict[s[curr:curr + wl]] = curr

        return res


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(Solution().findSubstring(s, words))