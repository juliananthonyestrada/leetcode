class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # return true if we can produce a valid topological ordering of size num courses

        def has_cycles():
            path = set()
            visited = set()
            adj = {i:[] for i in range(numCourses)}

            for src, dst in prerequisites:
                adj[src].append(dst)
            
            for src in adj:
                if not dfs(src, visited, adj, path):
                    return False
            return True
            
        def dfs(src, visited, adj, path):
            if src in path:
                return False

            if src in visited:
                return True

            path.add(src)
            visited.add(src)

            for dst in adj[src]:
                if not dfs(dst, visited, adj, path):
                    return False

            path.remove(src)

            return True

        return has_cycles()









