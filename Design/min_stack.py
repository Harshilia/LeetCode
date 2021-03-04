class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int):
        min_number = self.getMin()
        if min_number == None or x < min_number:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min_number))

    def pop(self):
        self.stack.pop()[0]

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
