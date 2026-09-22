class NumMatrix:
    # im implemented this whole thing without realizing that it isnt O(1)
    # this is linear time O(r2-r1) - O(n)
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_grid = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix_grid[r][c] = self.prefix_grid[r][c-1] + matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = 0
        for row in range(row1 + 1, row2 + 2):
            row_sum = self.prefix_grid[row][col2 + 1] - self.prefix_grid[row][col1]
            total_sum += row_sum
        return total_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


