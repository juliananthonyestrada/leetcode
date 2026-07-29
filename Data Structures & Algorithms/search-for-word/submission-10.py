class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        positions = set()
        ROWS, COLS = len(board), len(board[0])
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    positions.add((row,col))
            
        def dfs(row, col, idx):
            if idx == len(word):
                return True
            elif (0 <= row < ROWS and 0 <= col < COLS and board[row][col] == word[idx] and not seen[row][col]):  
                idx += 1
                seen[row][col] = True
                res = (dfs(row-1, col, idx)
                     or dfs(row, col-1, idx)
                     or dfs(row+1, col, idx)
                     or dfs(row, col+1, idx))
                seen[row][col] = False
                return res
            else:
                return False

        return any(dfs(r,c,0) for r, c in positions)