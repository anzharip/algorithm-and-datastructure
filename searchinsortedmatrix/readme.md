# Today I Learned: Searching Inside a Sorted Matrix
# Problem Statement
Write a function that takes in a sorted matrix of unique integers and a target integer, and returns an array of row and column indices of the target integer. Return [-1, -1] if the target integer is not found. The matrix could have a different height and width. 

# Sample Input
```
matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004],
        ]
target = 44
```

# Sample Result

```
[3, 3]
```

# Code #1

```python
def search_in_sorted_matrix(matrix, target):
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

```

# Notes
* Try starting the search from the top-right corner of the matrix, then increment or decrement the row or column indices appropriately. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image