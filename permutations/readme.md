# Today I Learned: Permutations
# Problem Statement
Write a function that takes in an array of unique integers and then returns an array of all unordered permutations. 

# Sample Input
```
array = [1, 2, 3]
```

# Sample Result

```
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
```

# Code #1

```python
def get_permutations(array):
    permutations = []
    helper(0, array, permutations)
    return permutations


def helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(list(array))
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            helper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

```

# Notes
* Assumption: if the input array is empty, return empty array. 
* Try thinking of permutations as a graph. 
* TODO: try the iterative approach. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image