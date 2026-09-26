import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # min cost to connect x signals Prims algorithm for finding a min spanning tree (MST)

        # I want to represent points as a graph where each point connects to each other point

        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((distance, j))

        # (distance, node)
        min_heap = [(0, 0)]
        visited = set()
        min_cost = 0

        while len(visited) < n:
            curr_distance, curr_node = heapq.heappop(min_heap)

            if curr_node in visited:
                continue
            visited.add(curr_node)
            min_cost += curr_distance

            for weight, nghb in adj[curr_node]:
                if nghb not in visited:
                    heapq.heappush(min_heap, (weight, nghb))

        return min_cost


