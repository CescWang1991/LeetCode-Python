# 301. Remove Invalid Parentheses

class Solution:
    # 递归解法，首先统计了多余的半括号的数量，然后遍历字符串，逐个删去多余的半括号，运用深度优先遍历，当多余的括号均删去
    # 时，判断剩余的字符串是否有效
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: list[str]
        """
        # 我们分别记录需要删除的左括号和右括号的数目
        right = 0
        stack = []
        for p in s:     # 利用堆栈，将左括号压入，遍历到右括号，若栈不为空，将栈顶pop，否则right+1
            if not stack and p == ")":
                right += 1
            elif p == ")":
                stack.pop()
            elif p == "(":
                stack.append(p)
        left = len(stack)
        self.res = []
        self.dfs(s, left, right, 0)
        return self.res

    def dfs(self, s, left, right, start):
        # 参数start用来标记上一层删去的元素的位置，我们从start开始遍历避免重复运算
        if left == right == 0 and self.isValid(s):      # left和right均为0时，s中的左右括号相等，判断是否为有效的str
            self.res.append(s)
        if left > 0:                # 删去左括号，注意连续多个左括号，只遍历第一个即可
            for i in range(start, len(s)):
                if (s[i] == "(" and i == start) or (s[i] == "(" and s[i-1] != "("):
                    self.dfs(s[:i] + s[i+1:], left-1, right, i)
        if right > 0:               # 删去右括号，同理，注意不能用elif，要同时删除
            for i in range(start, len(s)):
                if (s[i] == ")" and i == start) or (s[i] == ")" and s[i-1] != ")"):
                    self.dfs(s[:i] + s[i+1:], left, right-1, i)
        return
    # 参考#20 Valid Parentheses
    def isValid(self, s):
        stack = []
        for p in s:
            if p == "(":
                stack.append("(")
            elif p == ")":
                if not stack:
                    return False
                else:
                    stack.pop()
        return not stack