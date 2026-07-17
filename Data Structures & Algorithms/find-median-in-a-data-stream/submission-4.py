class MedianFinder:

    def __init__(self):
        self.lower = [] # max heap
        self.upper = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.lower:
            heapq.heappush(self.lower, -num)
        else:
            # num belongs to lower half
            if num < -self.lower[0]:
                heapq.heappush(self.lower, -num)
                # imbalance
                if len(self.lower) > len(self.upper)+1:
                    heapq.heappush(self.upper, -heapq.heappop(self.lower))
            # num belongs to upper half
            else:
                heapq.heappush(self.upper, num)
                # imbalance
                if len(self.upper) > len(self.lower) + 1:
                    heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        total = len(self.lower) + len(self.upper)
        # odd case
        if total%2:
            if len(self.lower)>len(self.upper):
                return -self.lower[0]
            else:
                return self.upper[0]
        # even case
        else:
            return (-self.lower[0] + self.upper[0]) / 2
            
        