class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        DIMENSIONS = 9
        valid_entries = { "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        
        # validate rows
        for row in range(DIMENSIONS):
            seen = set()
            for col in range(DIMENSIONS):
                if board[row][col] == ".":
                    continue
                elif board[row][col] not in valid_entries or board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # validate columns
        for col in range(DIMENSIONS):
            seen = set()
            for row in range(DIMENSIONS):
                if board[row][col] == ".":
                    continue
                elif board[row][col] not in valid_entries or board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # validates boxes by iterating over corners
        for row in range(0, DIMENSIONS, 3):
            for col in range(0, DIMENSIONS, 3):
                seen = set()
                # check the box
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] not in valid_entries or board[r][c] in seen:
                            return False
                        seen.add(board[r][c])

        return True