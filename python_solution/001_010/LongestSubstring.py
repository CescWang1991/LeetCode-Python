# 003. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans = 0
        last = -1
        dict = {}
        for i in range(len(s)):
            # 不能使用 if dict.get(s[i])，当value为0时，默认为False。
            if dict.get(s[i]) != None:
                # 最后出现的字符为last和前一个重复字符的最大者
                last = max(last, dict[s[i]])
            dict[s[i]] = i
            ans = max(ans, i - last)
        return ans