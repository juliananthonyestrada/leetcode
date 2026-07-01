class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # rotation = transpose & reverse rows

        def transpose(matrix: List[List[int]]) -> None:
            rows, cols = len(matrix), len(matrix[0])

            for row in range(rows):
                for col in range(row, cols):
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                

        def reverse(matrix: List[list[int]]) -> None:
            for row in range(len(matrix)):
                matrix[row].reverse()
                print(matrix[row])
        
        transpose(matrix)
        reverse(matrix)