# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        i = 0
        while i < n:
            if tokens[i] in ["+", "-", "*", "/"]:
                first = int(tokens[i-2])
                second = int(tokens[i-1])
                res = 0
                if tokens[i] == "+":
                    res = first + second
                elif tokens[i] == "-":
                    res = first - second
                elif tokens[i] == "*":
                    res = first * second
                elif tokens[i] == "/":
                    res = int(first / second)
                tokens[i - 2] = str(res)
                del tokens[i]
                del tokens[i-1]
                print(tokens)
                i -= 1
                n = len(tokens)
            else:
                i += 1
        return int(tokens[0])

    def evalStack(self, tokens):
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second = int(stack[-1])
                stack.pop()
                first = int(stack[-1])
                stack.pop()
                res = 0
                if token == "+":
                    res = first + second
                elif token == "-":
                    res = first - second
                elif token == "*":
                    res = first * second
                elif token == "/":
                    res = int(first / second)
                stack.append(res)
            else:
                stack.append(token)
        return int(stack[-1])


print(Solution().evalStack(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))