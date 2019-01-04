# 282. Expression Add Operators

class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.target = target
        for i in range(1, len(num)+1):
            self.dfs(num[i:], str(num[:i]), int(num[:i]), int(num[:i]), res)
            if num[0] == "0":
                break
        return res
    # dfs算法，prev表示前面的所有运算的结果，curr指上一个数字(用于乘法优先级)，expr是前面的运算表达式
    def dfs(self, num, expr, prev, curr, res):
        """
        :type num: str
        :type expr: str
        :type prev: int
        :type res: list[str]
        :rtype:
        """
        if len(num) == 0 and prev == self.target:
            res.append(expr)
            return
        for i in range(1, len(num)+1):
            post = int(num[:i])
            self.dfs(num[i:], expr + "+" + str(post), prev + post, post, res)
            self.dfs(num[i:], expr + "-" + str(post), prev - post, -post, res)
            # 针对乘法运算，由于乘法运算优先级高于加减法，我们需要上一个数字curr(上一个运算为加法为正，减法为负，乘法为prev)
            # 然后用(prev - curr) + curr * post表示运算结果
            ans = (prev - curr) + curr * post
            self.dfs(num[i:], expr + "*" + str(post), ans , ans, res)
            if num[0] == "0":       # 针对num开头是0的情况，此时只需要遍历第一个0，其余的可能都被舍弃
                break
        return