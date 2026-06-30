class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-n for n in nums] 
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        removed = []

        heapq.heappush(self.nums, -(val))

        for _ in range(self.k):
            removed.append(heapq.heappop(self.nums))
        
        res = -removed[-1]

        for r in removed:
            heapq.heappush(self.nums, r)
        
        return res