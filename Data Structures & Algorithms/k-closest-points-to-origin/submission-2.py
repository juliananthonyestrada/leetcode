class Solution:
    import math
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res, heap = [], []
        heapq.heapify(heap)

        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(heap, (-distance, point))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res            

