import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # what if we maintain a dictionary that has the least time to get from any node to any other node ?

        # src : (time taken to reach dst from src, dst)
        adj = {i : [] for i in range(1, n+1)}

        for src, dst, time in times:
            adj[src].append((time, dst))
        
        # we start from k and we want to reach all n nodes in the least time possible 
        signal_received = set()

        # (least time to reach node, node)
        min_heap = [(0, k)]
        time = 0

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)        

            if curr_node in signal_received:
                continue
            signal_received.add(curr_node)
            time = curr_time

            for nghb_time, nghb in adj[curr_node]:
                if nghb not in signal_received:
                    heapq.heappush(min_heap, (curr_time + nghb_time, nghb))

        return time if len(signal_received) == n else -1


    