# 155. Min Stack

class MinStack:
    # 设计两个栈，第一个存放元素，第二个按顺序存放最小值
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        # 若push的值小于栈顶，则push x到最小值栈顶
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
        # 否则将栈中的最小值加入栈顶
        else:
            self.min.append(self.getMin())

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack or self.min:
            return None
        # 将两个栈顶同时推出，维持两个栈元素个数相同
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]