class MyQueue:

    def __init__(self):
        self.stack = []
        self.first = None

    def push(self, x: int) -> None:
        if not self.stack:
            self.first = x
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 1:
            self.first = self.peek()
            self.stack = []
            return self.first
        else:
            self.first = self.peek()
            self.stack = self.stack[1:]
            return self.first

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()