from typing import Tuple

def cut_rod_memo(n: int, p: list[int], memo: dict = {}) -> int:
    # First, check if we have already computed the value
    if n in memo:
        return memo[n]
    
    # Base case for recursion
    if n == 0:
        return 0
    
    max_rev = -float('inf')
    for i in range(1, n+1):
        cur_rev = p[i] + cut_rod_recursive(n=n-i, p=p)
        max_rev = max(max_rev, cur_rev)
        memo[n] = cur_rev

    return max_rev

def cut_rod_recursive(n: int, p: list[int]) -> int:
    # Base case for recursion
    if n == 0:
        return 0
    
    max_rev = -float('inf')
    for i in range(1, n+1):
        cur_rev = p[i-1] + cut_rod_recursive(n=n-i, p=p)
        max_rev = max(max_rev, cur_rev)

    return max_rev


def cut_rod_tab(n: int, p: list[int]) -> Tuple[set, int]:
    # Create a table to store the maximum prices at each length
    r = [0] * (n+1)

    # Iterate over every possible length in the rod
    for i in range(1, n+1):
        max_rev = float('-inf')
        # Try every possible cut, j
        for j in range(1, i+1):
            cur_rev = p[j] + r[i-j]
            if cur_rev > max_rev:
                max_rev = cur_rev
        r[i] = max_rev
    
    return r[n]

prices = [0, 75, 86, 115, 120]
rev = cut_rod_tab(n=len(prices)-1, p=prices)
print(rev)