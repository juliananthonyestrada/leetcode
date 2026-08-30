class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        path, visited = set(), set()

        adj = {i:[] for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].append(dst)

        def dfs(src, path) -> bool:
            if src in path:
                return False
            
            if src in visited:
                return True
            
            path.add(src)
            visited.add(src)

            for nghb in adj[src]:
                if not dfs(nghb, path):
                    return False

            path.remove(src)
            return True
        
        for src in adj:
            if not dfs(src, path):
                return False
        
        return True

        
        

