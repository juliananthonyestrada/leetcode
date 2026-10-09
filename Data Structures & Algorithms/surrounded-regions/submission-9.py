class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        # flip the problem
        # instead of starting at each O position and check if it is surrounded
        # iterate over all border positions and mark all cells which can NEVER be surrounded

        def dfs(row: int, col: int) -> None:
            if (not (0 <= row < ROWS)
            or not (0 <= col < COLS)
            or board[row][col] != "O"):
                return
            
            board[row][col] = "cant be surrounded"

            for dr, dc in directions:
                dfs(row + dr, col + dc)


        for row in range(ROWS):
            seen = set()
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][COLS-1] == "O":
                dfs(row, COLS-1)

        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0, col)
            if board[ROWS-1][col] == "O":
                dfs(ROWS-1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "cant be surrounded":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"

