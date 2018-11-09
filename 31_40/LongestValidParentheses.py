def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return s

    stack = [("", -1)]
    for i in range(len(s)):
        if not stack:
            stack.append((s[i], i))
        else:
            if s[i] == ")" and stack[-1][0] == "(":
                stack.pop()
            else:
                stack.append((s[i], i))
    stack.append(("", len(s)))
    print(stack)
    l = 0
    for i in range(1, len(stack)):
        if stack[i][1] - stack[i-1][1] - 1 > l:
            l = stack[i][1] - stack[i-1][1] - 1
    return l


s = "(()))())("
longestValidParentheses(s)

