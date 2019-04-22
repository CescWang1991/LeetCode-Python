# 058. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        for i in reversed(range(len(s))):
            if s[i] == " ":
                # 注意最后的字符是空格，如果count = 0，则继续遍历
                if not count:
                    continue
                else:
                    break
            count += 1

        return count