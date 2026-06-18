class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row first and then the column

        low_row, low_col, high_row, high_col = 0, 0, len(matrix)-1, len(matrix[0])-1

        while low_row < high_row:
            mid_row = (low_row + high_row) // 2
            # smallest element of this row is larger than target
            if matrix[mid_row][0] > target:
                # the target is not in this row and any after it 
                high_row = mid_row - 1
            # the largest number of this row is less than the target
            elif matrix[mid_row][-1] < target:
                # the target is not in this row and any before it 
                low_row = mid_row + 1
            # the target is somehere in this row
            else:
                # low_row always holds the row in which the target is in 
                low_row = mid_row
                break

        # now we check in the row
        while low_col <= high_col:
            mid_col = (low_col + high_col) // 2
            # current value is larger than target
            if matrix[low_row][mid_col] > target:
                # search smaller
                high_col = mid_col - 1
            # current value is less than target
            elif matrix[low_row][mid_col] < target:
                # search larger
                low_col = mid_col + 1
            # element found
            else:
                return True
        # not found
        return False
