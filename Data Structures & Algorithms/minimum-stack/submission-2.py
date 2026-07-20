class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minimum[-1] == val:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        # print(self.stack, self.minimum)
        return self.minimum[-1]
        
