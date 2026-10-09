class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        pending = []
        available = []

        for i, (eq_time, pro_time) in enumerate(tasks):
            heapq.heappush(pending, (eq_time, pro_time, i))
        
        curr_time = 0
        order = []

        while pending or available:
            # add all pending processes <= curr_time to available heap
            while pending and pending[0][0] <= curr_time:
                eq_time, pro_time, i = heapq.heappop(pending)
                heapq.heappush(available, (pro_time, i))
            
            # process the process with the shortest pro_time
            if not available:
                curr_time = pending[0][0]
                continue
            
            pro_time, i = heapq.heappop(available)
            curr_time += pro_time
            order.append(i)

        return order