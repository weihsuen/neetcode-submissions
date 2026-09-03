class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            prev = self.minStack.pop()
            self.minStack.append(prev)
            self.minStack.append(min(prev, val))

        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top


    def getMin(self) -> int:
        prev = self.minStack.pop()
        self.minStack.append(prev)
        return prev
        
