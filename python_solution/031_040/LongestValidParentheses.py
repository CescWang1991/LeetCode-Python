# 32. longest Valid Parentheses

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return s

    stack = list()
    stack.append(-1)
    longest = 0
    for i in range(len(s)):
        # 当遇到"("时，将它的index加入到stack中。
        if s[i] == "(":
            stack.append(i)
        # 当遇到")"时，将栈顶index取出，如果stack为空，将它的index加入堆栈。
        elif s[i] == ")":
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                longest = max(longest, i - stack[-1])
    return longest


s = "(()))())("
longestValidParentheses(s)

