# 251. Flatten 2D Vector

# Implement an iterator to flatten a 2d vector.
#
# For example,
# Given 2d vector = [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

class Vector2D:

    def __init__(self, vectors):
        self.vector = []
        for v in vectors:
            self.vector += v
        self.index = -1
        self.length = len(self.vector)

    def next(self):
        self.index += 1
        return self.vector[self.index]

    def hasNext(self):
        return self.index < self.length