class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF, ROWS, COLS = 2147483647, len(grid), len(grid[0])
        neighbors = [[0,1], [0,-1], [-1, 0], [1,0]]
        
        visited = set()
        path_len = 0
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if grid[r][c] == INF:
                    grid[r][c] = path_len

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and (nr, nc) not in visited
                        and grid[nr][nc] != -1):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            path_len += 1
            
        


                    