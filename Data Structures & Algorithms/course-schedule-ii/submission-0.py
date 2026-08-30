class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].append(dst)

        path, visited = set(), set()
        ordering = []

        def dfs(node, ordering, path):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            visited.add(node)

            for nghb in adj[node]:
                if not dfs(nghb, ordering, path):
                    return False
            
            ordering.append(node)
            path.remove(node)
            return True

        for node in adj:
            if not dfs(node, ordering, path):
                return []
        
        return ordering