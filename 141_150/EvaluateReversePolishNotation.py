# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        i = 0
        while i < n:        # 遍历tokens，找到运算符，取出运算符前面两个元素，三者计算，将计算结果替换这三个元素。
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
                i -= 1
                n = len(tokens)
            else:
                i += 1
        return int(tokens[0])


class Solution2:
    def evalRPN(self, tokens):
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