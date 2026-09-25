import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # node : [(weights of nghb, nghb)]
        adj = {i : [] for i in range(n)}

        for u, v, w in edges:
            adj[u].append((w, v))
        
        # node -> shortest dist to reach node
        shortest_distance = {}

        # weight to reach node, node
        min_heap = [(0, src)]

        # while there are valid nodes to process
        while min_heap:
            curr_wght, curr_node = heapq.heappop(min_heap)
            # first time we reach a node is guaranteed to be shortest - never rewrite with a more expensive path 
            if curr_node in shortest_distance:
                    continue
            shortest_distance[curr_node] = curr_wght

            for nghb_wght, nghb in adj[curr_node]:
                if nghb in shortest_distance:
                    continue
                heapq.heappush(min_heap, (nghb_wght + curr_wght, nghb))

        # fill in missing nodes
        for i in range(n):
            if i not in shortest_distance:
                shortest_distance[i] = -1
         
        return shortest_distance