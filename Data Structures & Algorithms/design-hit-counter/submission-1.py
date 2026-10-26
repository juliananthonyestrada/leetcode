class HitCounter:

    def __init__(self):
        # queue of hits - [1, 1, 2, 5, 6, 6, 7, 10]
        self.q = deque()
        self.WINDOW = 300

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        lower_bound = timestamp - self.WINDOW
        while self.q and self.q[0] <= lower_bound:
            self.q.popleft()
        
        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
