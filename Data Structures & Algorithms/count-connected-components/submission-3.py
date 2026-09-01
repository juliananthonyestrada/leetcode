class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()

        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def bfs(node):
            q = deque([node])

            while q:
                curr = q.popleft()
                visited.add(curr)

                for nghb in adj[curr]:
                    if nghb not in visited:
                        q.append(nghb)
                        visited.add(nghb)
        
        res = 0
        for node in adj:
            if node in visited:
                continue
            bfs(node)
            res += 1
        
        return res