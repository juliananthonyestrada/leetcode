class MedianFinder:
    import heapq
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)
        heapq.heappush(self.maxheap, -num)

    def findMedian(self) -> float:
        l = len(self.minheap)
        mincopy = self.minheap.copy()
        maxcopy = self.maxheap.copy()

        mid = l // 2
    
        if l % 2 == 1:
            for _ in range(mid):
                heapq.heappop(mincopy)
            return mincopy[0] / 1
        else:
            for _ in range(mid-1):
                heapq.heappop(mincopy)
                heapq.heappop(maxcopy)
            return (mincopy[0] + (-maxcopy[0])) / 2



    # maintain 2 heaps a min heap and a max heap 
    # add num simply pushes it to each heap
    # to find median 
    # if odd length -> pop n/2 from each and return 
    # if even length -> pop n//2-1 from each and return avg 