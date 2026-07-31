class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1: return -1

        seen = set()
        q = deque()
        q.append((0,0))
        length = 1
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (1,0), (-1,0), (0,-1)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                # completed path ?
                if r == rows-1 and c == cols-1 and grid[r][c] != 1:
                    return length
                
                # add neighbors
                for dr, dc in neighbors:
                    nr, nc = r+dr, c+dc

                    if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in seen or grid[nr][nc] == 1:
                        continue
                    
                    seen.add((nr,nc))
                    q.append((nr,nc))
                
            length += 1
        
        return -1