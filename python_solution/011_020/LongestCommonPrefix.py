# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = []
        i = 0
        while i < len(strs[0]):
            s = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or s != strs[j][i]:
                    return "".join(prefix)
            prefix.append(s)
            i += 1

        return "".join(prefix)


class Solution2:
    def longestCommonPrefix(self, strs):
        res = ""
        if len(strs) == 0:
            return ""
        # zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
        for each in zip(*strs):
            if len(set(each)) == 1:  # 利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res