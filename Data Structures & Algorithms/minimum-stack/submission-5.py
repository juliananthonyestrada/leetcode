class MinStack:

    def __init__(self):
        self.min_vals = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_vals == [] or (val <= self.min_vals[-1]):
            self.min_vals.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_vals[-1]:
            self.min_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
