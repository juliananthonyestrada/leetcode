class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        def zeroize(row, col, matrix):
            for r in range(ROWS):
                matrix[r][col] = 0

            for c in range(COLS):
                matrix[row][c] = 0

            return matrix

        positions = set()
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    positions.add((row, col))
        
        for row, col in positions:
            matrix = zeroize(row, col, matrix)
        
        
