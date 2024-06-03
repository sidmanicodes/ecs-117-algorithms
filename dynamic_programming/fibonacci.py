def fib_no_dp(x: int):
    """Non-DP implementation of the Fibonacci sequence"""
    if x == 1 or x == 2:
        return 1
    return fib_no_dp(x-1) + fib_no_dp(x-2)

def fib_memo(x: int, memo={}):
    """Fibonacci sequence that utilizes memoization"""
    # Check if we have already performed the recursive operation
    if x in memo:
        return memo[x]
    
    # Base case
    elif x == 1 or x == 2:
        return 1
    
    # Add recursive operation to the memo and return the result
    memo[x] = fib_memo(x=x-1, memo=memo) + fib_memo(x=x-2, memo=memo)
    return memo[x]

def fib_tab(x: int):
    """Fibonacci sequence that utilizes tabulation"""
    # Create table
    table = [0] * x

    # Fill in the first two numbers of the table
    table[0], table[1] = 1, 1

    # Fill in the rest of the table
    for i in range(2, x):
        table[i] = table[i-1] + table[i-2]

    # Return the last number in the table (the xth Fibonacci number)
    return table[x-1]

print(fib_tab(10))