def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0] * (n + 1)
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if amount >= denom:
                ways[amount] += ways[amount - denom]

    return ways[n]

