def knapsack_brute_force(items: list[tuple], capacity: int) -> tuple[list[tuple], int]:
    n = len(items)
    
    max_value = 0
    best_subsets = []

    # Range of (2^n)-1
    for i in range(1 << n):
        cur_weight = 0
        cur_value = 0
        cur_subsets = []

        # Check if the current item, j, is in combination
        # of items we're looking at
        for j in range(n):

            # This looks complex, but all this is doing is checking if
            # the binary representation of j is present in the binary representation
            # of i (which tells us which subset we're looking at)
            if i & (1 << j):
                cur_weight += items[j][1]
                cur_value += items[j][2]
                cur_subsets.append(items[j][0])

        if cur_value > max_value and cur_weight <= capacity:
            max_value = cur_value
            best_subsets = cur_subsets

    return (best_subsets, max_value)

def knapsack_tabulation(items: list[tuple], capacity: int) -> tuple[list[tuple], int]:
    n = len(items)
    table = [[0] * (capacity+1)] * (n+1)

    for w in range(1, capacity+1):
        for i in range(1, n+1):
            _, weight, value = items[i-1]
            # Cannot include current item (no room)
            if weight > w:
                table[i][w] = table[i-1][w]
            # Choose the better option: steal or don't steal
            else:
                table[i][w] = max(table[i-1][w], value + table[i-1][w-weight])

    return table[n][capacity]

# Define the items as a list of tuples (weight, value)
items = [
    ("Tent", 25, 60),
    ("Sleeping Bag", 15, 40),
    ("Cooking Gear", 10, 30),
    ("Food Supplies", 15, 45),
    ("Water Filter", 5, 35),
    ("Clothes", 20, 20),
    ("First Aid Kit", 5, 25),
    ("Flashlight", 3, 15),
    ("Map and Compass", 2, 15)
]

# Define the knapsack's weight capacity
capacity = 50

# print(knapsack_brute_force(items=items, capacity=capacity))
print(knapsack_tabulation(items=items, capacity=capacity))