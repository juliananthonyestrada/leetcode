import heapq
from collections import deque 

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        # build adj list
        adj = {i : [] for i in range(n)}
        for i, edge in enumerate(edges):
            src, dst = edge
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))

        max_heap = [(-1, start_node)]
        visited = set()

        while max_heap:
            curr_prob, curr_node = heapq.heappop(max_heap)
            visited.add(curr_node)

            if curr_node == end_node:
                return -curr_prob

            for nghb, nghb_weight in adj[curr_node]:
                if nghb not in visited:
                    heapq.heappush(max_heap, (nghb_weight * curr_prob, nghb))
        
        return 0
