# 225. Implement Stack Using Queue
# 232. Implement Queue Using Stack

class MyStack:
    # 使用双队列
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
    # q2为空，则加入到q1中，反之亦然
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if not self.q2:
            self.q1.append(x)
        elif not self.q1:
            self.q2.append(x)
    # 加入q1不为空，则将q1中元素按顺序压入到q2中，并将q1的最后一个元素删除并返回
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            while len(self.q1) >= 2:
                self.q2.append(self.q1[0])
                del self.q1[0]
            top = self.q1[0]
            del self.q1[0]
            return top
        if self.q2:
            while len(self.q2) >= 2:
                self.q1.append(self.q2[0])
                del self.q2[0]
            top = self.q2[0]
            del self.q2[0]
            return top

    # 与pop操作类似，区别在于最后一个元素要压入另一个队列中
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q1:
            while len(self.q1) >= 2:
                self.q2.append(self.q1[0])
                del self.q1[0]
            top = self.q1[0]
            del self.q1[0]
            self.q2.append(top)
            return top
        if self.q2:
            while len(self.q2) >= 2:
                self.q1.append(self.q2[0])
                del self.q2[0]
            top = self.q2[0]
            del self.q2[0]
            self.q1.append(top)
            return top


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.q1 or self.q2:
            return False
        else:
            return True


class MyQueue:
    # 使用双堆栈，一个用来push时存放元素，一个用来pop和peek
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushStack = []
        self.popStack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.pushStack.append(x)
    # pop堆栈空时，将第一个stack中的元素按LIFO顺序推入第二个stack中，这样stack中的元素按逆序进入第二个stack，并将栈顶推出。
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        x = self.popStack.pop()
        return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.pushStack or self.popStack:
            return False
        else:
            return True