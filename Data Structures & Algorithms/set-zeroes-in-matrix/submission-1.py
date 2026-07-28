class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    rows[row] = True
                    cols[col] = True
        
        for row in range(ROWS):
            for col in range(COLS):
                if rows[row] or cols[col]:
                    matrix[row][col] = 0