class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        seen = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            # hit water
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                grid[r][c] == 0):
                return 1
            
            if seen[r][c]:
                return 0
                    
            seen[r][c] = True

            # keep searching
            return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c)
        