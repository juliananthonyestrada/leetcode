class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # read prob carefully -> every path from source must die at destination

        # build a directed adjacency list
        adj = {i : [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
        
        def dfs(node, path):
            if node == destination:
                # we require the path to end at destination
                return len(adj[node]) == 0
            elif node in path:
                return False
            elif len(adj[node]) == 0:
                return False
            
            # from each neighbor can we reach 
            path.add(node)
            res = all([dfs(nghb, path) for nghb in adj[node]])
            path.remove(node)
            return res
        
        return dfs(source, set())
