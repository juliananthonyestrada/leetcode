class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(word_idx, row, col) -> bool:
            if word_idx == len(word):
                return True

            if (0 <= row < ROWS 
                and 0 <= col < COLS 
                and (row, col) not in path 
                and board[row][col] == word[word_idx]):

                path.add((row, col))
                result = (
                    dfs(word_idx + 1, row, col+1)
                    or dfs(word_idx + 1, row, col-1)
                    or dfs(word_idx + 1, row-1, col)
                    or dfs(word_idx + 1, row+1, col)
                )
                path.remove((row, col))
                return result
            else:
                return False

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(0, row, col):
                        return True
        return False