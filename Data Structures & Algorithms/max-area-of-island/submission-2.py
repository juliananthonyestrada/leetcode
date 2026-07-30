class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0
        seen = set()

        # traverse the grid looking for islands
        # once we are at an island -> compute the area

        def compute_area(r, c):
            
            if (r < 0 or c < 0
                or r == len(grid) or c == len(grid[0])
                or grid[r][c] == 0 or
                (r,c) in seen):
                return 0

            seen.add((r,c))
            
            return 1 + compute_area(r+1, c) + compute_area(r-1, c) + compute_area(r, c-1) + compute_area(r, c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, compute_area(r, c))
                
        return area
            
