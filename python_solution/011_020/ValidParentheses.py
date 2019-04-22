# 020. Valid Parentheses

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        paren = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if stack and stack[-1] == paren[s[i]]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False