class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Testing the class locally with inputs and outputs like VS Code
if __name__ == "__main__":
    minStack = MinStack()
    
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    
    print("getMin():", minStack.getMin())  # Output: -3
    
    minStack.pop()
    
    print("top():", minStack.top())        # Output: 0
    print("getMin():", minStack.getMin())  # Output: -2