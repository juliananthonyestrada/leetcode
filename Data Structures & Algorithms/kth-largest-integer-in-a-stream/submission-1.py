class KthLargest:
    import heapq
    # key insight: we only care about k largest, so we dont need to store more than k elements
    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.size = 0
        self.nums = []
        heapq.heapify(self.nums)
        
        for n in nums:
            heapq.heappush(self.nums, n)
            self.size += 1
            if self.size > self.k:
                heapq.heappop(self.nums)
                self.size -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self.size += 1
        if self.size > self.k:
            heapq.heappop(self.nums)
            self.size -= 1
        
        return self.nums[0]
    