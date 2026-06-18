class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row first and then the column

        low_row, low_col, high_row, high_col = 0, 0, len(matrix)-1, len(matrix[0])-1

        # check last element of mid row
        while low_row < high_row:
            mid_row = (low_row + high_row) // 2
            if matrix[mid_row][0] > target:
                high_row = mid_row
            elif matrix[mid_row][-1] < target:
                low_row = mid_row + 1
            else:
                low_row = mid_row
                break

        while low_col <= high_col:
            mid_col = (low_col + high_col) // 2
            if matrix[low_row][mid_col] > target:
                high_col = mid_col - 1
            elif matrix[low_row][mid_col] < target:
                low_col = mid_col + 1
            else:
                return True
    
        return False
