class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cache = {}
        ROWS, COLS = len(grid), len(grid[0])

        def traverse(r, c):

            # out of bounds
            if (not (0 <= r < ROWS)
            or not ( 0 <= c < COLS)):
                return float('inf')

            if (r, c) in cache:
                return cache[(r,c)]

            # at dest
            if (r == ROWS - 1
            and c == COLS - 1):
                return grid[r][c]

            # traversing
            right = grid[r][c] + traverse(r, c+1)
            down = grid[r][c] + traverse(r+1, c)

            cache[(r,c)] = min(right, down)
            return cache[(r,c)]

        return traverse(0, 0)