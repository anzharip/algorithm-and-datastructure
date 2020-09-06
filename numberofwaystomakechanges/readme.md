# Today I Learned: Number of Ways to Make Coin Changes
# Problem Statement

Given an array of unique positive integers representing coin denominations and a single positive integer n representing a target amount of money, implement a function that returns the number of ways to make change for that target amount. 

# Sample Input & Output

```
n = 6
denominations = [1, 5]
```

# Sample Output
```
2 # 1x coin 5 + 5x coin 1 and 6 x coin 1
```

# Code #1

```python
def number_of_ways_to_make_changes(n, denominations):
    ways = [0] * (n + 1)
    ways[0] = 1

    for denom in denominations:
        for amount in range(1, n + 1):
            if amount >= denom:
                ways[amount] += ways[amount - denom]

    return ways[n]

```

# Notes
* Assumption: if n is 0, means there is 0 coin combination available. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image