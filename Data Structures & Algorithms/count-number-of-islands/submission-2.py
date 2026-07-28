class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            # reached water
            if (row < 0 or col < 0 
            or row == ROWS or col == COLS
            or grid[row][col] == "0" 
            or grid[row][col] == "#"):
                return 
            
            # mark the current node as seen - prevents infinitely recursing back and forth 
            grid[row][col] = "#"

            # keep searching
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row, col+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res += 1
        
        return res