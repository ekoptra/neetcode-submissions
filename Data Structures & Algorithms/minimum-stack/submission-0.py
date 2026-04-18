class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        idx_val = len(self.stack) - 1
        before_min = None

        if idx_val == 0:
            before_min = val + 1 
        else:
            before_min = self.min_stack[idx_val - 1]

        self.min_stack.append(min(val, before_min))
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[len(self.stack) - 1]
