class NumMatrix:
    # what if at each cell (r,c) we store the sum of the quadriltaral formed from 0 to r and 0 to c
    # we must use inclusion exclusion
    
    def __init__(self, matrix: List[List[int]]):
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.prefix_grid = [[0] * (self.COLS+1) for _ in range(self.ROWS+1)]

        for row in range(1, self.ROWS+1):
            for col in range(1, self.COLS+1):
                self.prefix_grid[row][col] = (matrix[row-1][col-1]
                                           + self.prefix_grid[row][col-1]
                                           + self.prefix_grid[row-1][col]
                                           - self.prefix_grid[row-1][col-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_grid[row2 + 1][col2 + 1]
        above = self.prefix_grid[row1][col2 + 1]
        left = self.prefix_grid[row2 + 1][col1]
        overlap = self.prefix_grid[row1][col1]
        return total - above - left + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)