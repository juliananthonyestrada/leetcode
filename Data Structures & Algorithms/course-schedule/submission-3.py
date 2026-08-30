class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        path, visited = set(), set()

        adj = {i:[] for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].append(dst)

        def has_cycle(src, path) -> bool:
            if src in path:
                return True
            
            if src in visited:
                return False
            
            path.add(src)
            visited.add(src)

            for nghb in adj[src]:
                if has_cycle(nghb, path):
                    return True

            path.remove(src)
            return False
        
        for src in adj:
            if has_cycle(src, path):
                return False
        
        return True

        
        

