class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1

        seen = set()
        length = 1
        q = deque()
        q.append((0,0))
        directions = [(1,1), (1,-1), (-1, 1), (-1,-1), (0,1), (1,0), (0,-1), (-1,0)]

        while q:
            # add 8 directions for each cell in the q
            for _ in range(len(q)):
                r, c = q.popleft()
                seen.add((r,c))
                  
                if r == rows-1 and c == cols-1 and grid[r][c] != 1:
                    return length

                for dr, dc in directions:
                    # out of bounds
                    if (r+dr < 0 or c+dc < 0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == 1 or (r+dr,c+dc) in seen):
                        continue    
                    q.append((r+dr, c+dc))
            
            length += 1
    
        return -1 