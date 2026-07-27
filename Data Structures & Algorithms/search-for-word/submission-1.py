class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        positions = []
        ROWS, COLS = len(board), len(board[0])
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    positions.append((r,c))
            
        def dfs(r, c, i, s):
            
            if r < 0 or r == len(board):
                return False
            if c < 0 or c == len(board[0]):
                return False

            if board[r][c] == word[i] and not seen[r][c]:
                s.append(word[i])
                seen[r][c] = True
                if ''.join(s) == word:
                    return True

                if dfs(r-1, c, i+1, s.copy()) or dfs(r, c-1, i+1, s.copy()) or dfs(r+1, c, i+1, s.copy()) or dfs(r, c+1, i+1, s.copy()):
                    return True
                else:
                    seen[r][c] = False
                    return False
            else:
                return False

        if not positions:
            return False

        for pos in positions:
            if dfs(pos[0], pos[1], 0, []):
                return True
        
        return False








