class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: return True
        
        adj = {i:[] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        path = set()
        def acyclic(node, parent):
            if node in path:
                return False
            
            path.add(node)
            for nghb in adj[node]:
                if nghb == parent:
                    continue
                elif not acyclic(nghb, node):
                    return False
            path.remove(node)

            return True
            
        count = 0
        visited = set()
        def connected(node):
            nonlocal count
            count += 1
            visited.add(node)

            for nghb in adj[node]:
                if nghb not in visited:
                    connected(nghb)
            
            return count == n

        return connected(0) and acyclic(0, None)
        
        
        
            










        # do i need path as an arg ??