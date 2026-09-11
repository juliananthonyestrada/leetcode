class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        res = set()
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def pacific(r, c, prev) -> bool:
            if r < 0 or c < 0:
                return True

            if (r == ROWS or c == COLS or (r, c) in visited_pacific or heights[r][c] > prev):
                return False

            visited_pacific.add((r, c))

            return any([pacific(r + dr, c + dc, heights[r][c]) for dr, dc in neighbors])

        def atlantic(r, c, prev):
            if r == ROWS or c == COLS:
                return True

            if (r < 0 or c < 0 or (r, c) in visited_atlantic or heights[r][c] > prev):
                return False

            visited_atlantic.add((r, c))

            return any([atlantic(r + dr, c + dc, heights[r][c]) for dr, dc in neighbors])

        for r in range(ROWS):
            for c in range(COLS):
                visited_pacific = set()
                visited_atlantic = set()
                atl, pac = atlantic(r, c, float("inf")), pacific(r, c, float("inf"))
                if atl and pac:
                    res.add((r, c))

        return list(res)
