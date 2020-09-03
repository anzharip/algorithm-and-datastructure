def longestPalindromicSubstring(string):
    # Write your code here.
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
