class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # build a directed adjacency list
        adj = {i : [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
        
        # count all paths from source to destination
        def dfs(node, path):
            if node == destination:
                return len(adj[node]) == 0
            elif node in path:
                return False
            elif len(adj[node]) == 0:
                return False
            
            path.add(node)
            res = all([dfs(nghb, path) for nghb in adj[node]])
            path.remove(node)
            return res
        
        return dfs(source, set())
