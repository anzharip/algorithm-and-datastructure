def spiralTraverse(array):
    # Write your code here.
    result = []
    start_row = 0
    end_row = len(array) - 1
    start_col = 0
    end_col = len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        # col to right
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])
        # row to bottom
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])
        # col to left
        for col in range(end_col - 1, start_col - 1, -1):
            if start_row == end_row:
                break
            result.append(array[end_row][col])
        # row to top
        for row in range(end_row - 1, start_row - 1 + 1, -1):
            if start_col == end_col:
                break
            result.append(array[row][start_col])
        
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1
    
    return result

