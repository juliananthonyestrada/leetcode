class Node:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        visited = Node(url)
        self.curr.next = visited
        visited.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        walked = 0
        while walked < steps and self.curr.prev and self.curr != self.homepage:
            self.curr = self.curr.prev
            walked += 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        walked = 0
        while walked < steps and self.curr.next:
            self.curr = self.curr.next
            walked += 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)