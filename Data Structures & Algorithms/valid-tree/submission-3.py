class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: return True
        if len(edges) != n-1: return False
        
        adj = {i:[] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        def acyclic(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nghb in adj[node]:
                if nghb == parent:
                    continue
                elif not acyclic(nghb, node):
                    return False

            return True
    
        return acyclic(0, None) and len(visited) == n
        
        
        
            










        # do i need path as an arg ??