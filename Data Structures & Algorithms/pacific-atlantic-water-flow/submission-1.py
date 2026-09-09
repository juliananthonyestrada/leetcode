class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        res = []
        
        def reached_pacific(r, c, prev):
            if r < 0 or c < 0:
                return True
            
            if (r == ROWS or c == COLS
                or (r,c) in visited_pacific
                or heights[r][c] > prev):
                return False
            
            visited_pacific.add((r,c))

            return any([
                reached_pacific(r+1, c, heights[r][c]),
                reached_pacific(r, c+1, heights[r][c]),
                reached_pacific(r-1, c, heights[r][c]),
                reached_pacific(r, c-1, heights[r][c])
            ])
        
        def reached_atlantic(r, c, prev):
            if r == ROWS or c == COLS:
                return True
            
            if (r < 0 or c < 0
                or (r,c) in visited_atlantic
                or heights[r][c] > prev):
                return False
            
            visited_atlantic.add((r,c))

            return any([
                reached_atlantic(r+1, c, heights[r][c]),
                reached_atlantic(r, c+1, heights[r][c]),
                reached_atlantic(r-1, c, heights[r][c]),
                reached_atlantic(r, c-1, heights[r][c])
            ])
        
        for r in range(ROWS):
            for c in range(COLS):
                visited_pacific = set()
                visited_atlantic = set()
                if reached_pacific(r,c, float('inf')) and reached_atlantic(r,c, float('inf')):
                    res.append([r,c])
        
        return res