class MyStack:

    def __init__(self):
        self.main = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        deleted = None        
        # take all elements except the last one
        deleted = self.main[-1]
        self.main = self.main[0:-1]
        # return deleted element 
        return deleted

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