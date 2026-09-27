class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        rank = [1] * (n+1)
        parent = [i for i in range(n+1)]

        def find(node) -> int:
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2) -> bool:
            parent1, parent2 = find(node1), find(node2)

            # already connected
            if parent1 == parent2:
                return False
            # not connected - lets connect them
            else:
                if rank[parent1] < rank[parent2]:
                    parent[parent1] = parent2
                    rank[parent2] += rank[parent1]
                else:
                    parent[parent2] = parent1
                    rank[parent1] += rank[parent2]

            return True
            
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
                
