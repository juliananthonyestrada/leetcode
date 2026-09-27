class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matrix = matrix

        self.prefix_grid = [[0] * (cols+1) for _ in range(rows+1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                self.prefix_grid[r][c] = (
                    self.matrix[r-1][c-1] +
                    self.prefix_grid[r-1][c] + 
                    self.prefix_grid[r][c-1] -
                    self.prefix_grid[r-1][c-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return (
            self.prefix_grid[row2+1][col2+1]      # bottom-right
            - self.prefix_grid[row1][col2+1]       # remove top part
            - self.prefix_grid[row2+1][col1]       # remove left part
            + self.prefix_grid[row1][col1]) 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
'''
(r1, c1) to (r2, c2)
 2 , 3       4 , 4

[3,0,1,4,2]
[5,6,3,2,1]
[1,2,0,1,5]
[4,1,0,1,7]
[1,0,3,0,5]

[00, 00, 00, 00, 00, 00] 
[00, 03, 03, 04, 08, 00]
[00, 08, 14, 18, 24, 00] 
[00, 09, 17, 21, 28, 00] 
[00, 13, 22, 26, 34, 00]
[00, 00, 00, 00, 00, 00]
'''
