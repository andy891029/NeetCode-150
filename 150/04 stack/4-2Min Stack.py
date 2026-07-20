
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1],val))
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
       
min_stack = MinStack()

min_stack.push(1)
min_stack.push(2)
min_stack.push(0)
print(min_stack.stack)
print(min_stack.getMin())  # 預期 0
min_stack.pop()
print(min_stack.top())     # 預期 2
print(min_stack.getMin())  # 預期 1