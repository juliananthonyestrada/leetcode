class MyStack:

    def __init__(self):
        self.main = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        # ensure the placeholder queue is empty
        self.temp = []
        # take all elements except the last one
        self.temp = self.main[0:-1]
        self.main = [self.main[-1]]
        # swap names
        self.temp, self.main = self.main, self.temp
        # return deleted element - now it is in temp
        return self.temp[0]

    def top(self) -> int:
        return self.main[-1]

    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()