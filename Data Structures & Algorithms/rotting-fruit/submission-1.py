class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        minutes = 0
        healthy = 0
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1,0), (0,1), (-1,0), (0,-1)]

        # seed the queue with all initially rotten oranges
        # and count fresh ones so we know when we're done
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    healthy += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # stop early if no fresh oranges remain
        while q and healthy > 0:
            # process one full "minute" — all currently rotten oranges spread simultaneously
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2  # mutating grid doubles as visited tracking
                    healthy -= 1
                    q.append((nr, nc))
            minutes += 1

        # if fresh oranges remain they were unreachable (isolated by empty cells)
        return minutes if healthy == 0 else -1