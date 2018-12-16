class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 处理特殊情况，p为空时，返回s是否为空
        if not p:
            return not s
        # 第一个字符匹配，因为此时p不为空，所以s也不能为空
        firstMatch = bool(s) and p[0] in (s[0], '.')

        if len(p) >= 2 and p[1] == '*':
            # 第二个字符是*时，他前面的字母可以出现0次，此时只需要直接把*和前面的字符去掉递归即可
            # 或者把str第一个去掉，剩下的部分再与p匹配
            return self.isMatch(s, p[2:]) or (firstMatch and self.isMatch(s[1:], p))
        else:
            # 与没有*时一样，只要第一个一样，然后去掉首字母后在比较，都相等则匹配
            return firstMatch and self.isMatch(s[1:], p[1:])