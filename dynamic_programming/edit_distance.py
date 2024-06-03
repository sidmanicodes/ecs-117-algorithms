def edit_distance(x: str, y: str, ins_cost: int, del_cost: int, rep_cost: int) -> int:
    m = len(x)
    n = len(y)
    table = [[0] * (n+1)] * (m+1)

    # Initialize 0th column values to be the cost of inserting
    # i elements
    for i in range(m+1):
        table[i][0] = i * del_cost

    # Initialize 0th row values to be the cost of deleting
    # j elements
    for j in range(n+1):
        table[j][0] = j * ins_cost

    # Fill out table
    for j in range(1, m+1):
        for i in range(1, n+1):
            # If the characters are the same, there is no edit distance
            if x[i-1] == y[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min(
                    table[i-1][j] + ins_cost, # Deletion
                    table[i][j-1] + del_cost, # Insertion
                    table[i-1][j-1] + rep_cost # Substitution
                )

    # Return last element in table (the edit distance for the entire subsequences)
    return table[m][n]

x = 'abc'
y = 'axl'
ins_cost = del_cost = rep_cost = 1
print(edit_distance(x=x, y=y, ins_cost=ins_cost, del_cost=del_cost, rep_cost=rep_cost))
    