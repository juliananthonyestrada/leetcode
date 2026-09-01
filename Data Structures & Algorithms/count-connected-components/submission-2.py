class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()

        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            visited.add(node)
            for nghb in adj[node]:
                if nghb not in visited:
                    visited.add(nghb)
                    dfs(nghb)
        
        res = 0
        for node in adj:
            if node in visited:
                continue
            dfs(node)
            res += 1
        
        return res