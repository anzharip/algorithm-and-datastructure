def searchInSortedMatrix(matrix, target):
    # Write your code here.
    ptr_row = 0
    ptr_col = len(matrix[0]) - 1
    while ptr_row > -1 and ptr_col > -1 and ptr_row < len(matrix) and ptr_col < len(matrix[0]):
        if target > matrix[ptr_row][ptr_col]:
            ptr_row += 1
        elif target < matrix[ptr_row][ptr_col]:
            ptr_col -= 1
        else:
            return [ptr_row, ptr_col]

    return [-1, -1]
