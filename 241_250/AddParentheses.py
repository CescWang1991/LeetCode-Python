# 241. Different Ways to Add Parentheses

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # 分治法，以每个运算符号为界，将字符串分为left和right，递归调用函数返回left和right形成的数组，采用笛卡儿积对左右
        # 数组的元素运算，将结果加入res数组。
        if not input:
            return []
        if input.count("+") == 0 and input.count("-") == 0 and input.count("*") == 0:
            return [int(input)]

        res = []
        operators = ["+", "-", "*"]
        for i in range(len(input)):
            if input[i] in operators:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                if input[i] == "+":
                    for l in left:
                        for r in right:
                            res.append(l + r)
                elif input[i] == "-":
                    for l in left:
                        for r in right:
                            res.append(l - r)
                elif input[i] == "*":
                    for l in left:
                        for r in right:
                            res.append(l * r)

        return res