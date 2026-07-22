class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimum = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.minimum)
            if val < self.minimum:
                self.minimum = val

    def pop(self) -> None:
        #print(self.minimum, self.stack)
        elem = self.stack.pop()
        if elem < 0:
            self.minimum = self.minimum - elem
        #print(self.minimum, self.stack)

    def top(self) -> int:
        #print(self.minimum, self.stack)
        # return self.minimum + self.stack[-1]

        top = self.stack[-1]
        if top > 0:
            return top + self.minimum
        else:
            return self.minimum

    def getMin(self) -> int:
        return self.minimum
        
