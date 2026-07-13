class Solution:
    
    def isValidRow(self, board, row):
            valid_numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

            # given a row, check each column to ensure validity
            seen = set()
            for c in range(9):
                if board[row][c] == ".":
                    continue
                # we return false when we see an invalid number or a repeated number
                elif board[row][c] not in valid_numbers or board[row][c] in seen:
                    return False
                # add the valid, unseen number to the seen
                else:
                    seen.add(board[row][c])
            # this row is valid
            return True

    def isValidCol(self, board, col):
        valid_numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

        # given a col, check each row to ensure validity
        seen = set()
        for r in range(9):
            if board[r][col] == ".":
                continue
            # we return false when we see an invalid number or a repeated number
            elif board[r][col] not in valid_numbers or board[r][col] in seen:
                return False
            # add the valid, unseen number to the seen
            else:
                seen.add(board[r][col])
        # this col is valid
        return True
    
    def isValidSquare(self, board, row, col):
        valid_numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

        seen = set()
        # given a top left starting point we know where the boundary points are for both rows and cols
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if board[r][c] == ".":
                    continue
                elif board[r][c] not in valid_numbers or board[r][c] in seen:
                    return False
            # add the valid, unseen number to the seen
                else:
                    seen.add(board[r][c])
        # this square is valid
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for x in range(9):
            if not self.isValidRow(board, x):
                return False
            if not self.isValidCol(board, x):
                return False
        
        corners = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
            ]

        for c in corners:
            if not self.isValidSquare(board, c[0], c[1]):
                return False

        return True