# Today I Learned: Longest Palindromic Substring
# Problem Statement
Write a function that takes in a string, and returns its longest palindromic subsctring. 

# Sample Input
```
string = "qazaasdffdsaawsx"
```

# Sample Result

```
"aasdffdsaa"
```

# Code #1

```python
def longest_palindromic_substring(string):
    cur_longest = [0, 1]
    for idx in range(1, len(string)):
        odd = get_longest_palindrome(string, idx - 1, idx + 1)
        even = get_longest_palindrome(string, idx - 1, idx)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        cur_longest = max(longest, cur_longest, key=lambda x: x[1] - x[0])
    return string[cur_longest[0]:cur_longest[1]]


def get_longest_palindrome(string, idx_l, idx_r):
    while idx_l > -1 and idx_r < len(string):
        if string[idx_l] != string[idx_r]:
            break
        idx_l -= 1
        idx_r += 1
    return [idx_l + 1, idx_r]

```

# Notes
* Imagine the palindrome problem as seeing the substring in a mirror. 
* The mirror could lie in between the character ("abba") or on a character itself("aba"). 
* Naive approach: generate all possible combination of substring from len 2 to len of string, then apply check_palindrome function. 

# Credits
* Algoexpert for the problem statement
* XKCD for the cover image