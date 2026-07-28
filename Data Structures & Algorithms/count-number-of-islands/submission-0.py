class Solution:
    # key insight: go out and search for the water surrounding this island and return
    # any time we return that means we found an island so we increment
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rbound, cbound = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 \
            or r == rbound or c == cbound \
            or grid[r][c] == "#" or grid[r][c] == '0':
                return 
            
            grid[r][c] = "#"

            dfs(r+1,c)
            dfs(r, c+1)
            dfs(r-1,c)
            dfs(r, c-1)

        for r in range(rbound):
            for c in range(cbound):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1

        return islands