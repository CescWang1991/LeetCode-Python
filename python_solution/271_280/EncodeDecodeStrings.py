# 271. Encode and Decode Strings

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
# decoded back to the original list of strings.
# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:

# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }

# So Machine 1 does:
# string encoded_string = encode(strs);
# and Machine 2 does:
# vector<string> strs2 = decode(encoded_string);
#
# strs2 in Machine 2 should be the same as strs in Machine 1.
# Implement the encode and decode methods.
# Note:
#
# The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized
# enough to work on any possible characters.
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

class Solution:
    # 选择一个特殊字符"|"作为分隔符，前面记录字符串长度，后面记录字符串，形式为“2|ab3|abc|4abcd”
    def encode(self, strs):
        """
        :type strs: list[str]
        :rtype: str
        """
        ans = ""
        for s in strs:
            ans += str(len(s)) + "|" + s
        return ans

    def decode(self, s):
        """
        :type s: str
        :rtype: list[str]
        """
        count = False       # count表示当前字符是否为字符串，True表示当前字符为字符串长度，用num计数，否则将加入res的末尾字符串中
        num = ""            # 加入字符串长度是为了区别当前元素"|"代表原字符串还是分隔符
        res = []
        for i in range(len(s)):
            if not count:
                if num == "":       # num为0，表示以遍历完一个字符串，从而转而开始计数
                    count = True
                    num += s[i]
                else:
                    res[-1] += s[i]
                    num -= 1
                    if num == 0:
                        num = ""
            else:
                if s[i] == "|":     # 遭遇分隔符，从而开始构造字符串，当"|"为字符串元素时，不在这一if语句中执行
                    count = False
                    res.append("")
                    num = int(num)
                else:
                    num += s[i]
        return res