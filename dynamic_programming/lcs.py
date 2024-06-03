def lcs(x: str, y: str) -> list[str]:
    # Create table
    m = len(x)
    n = len(y)
    table = [[(0, None) for _ in range(n+1)] for _ in range(m+1)]

    # Iterate over table and fill in matches
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i][j] = (table[i-1][j-1][0] + 1, "diag")
            else:
                table[i][j] = max(
                    (table[i-1][j][0], "up"), 
                    (table[i][j-1][0], "left")
                )

    # Find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if table[i][j][1] == "diag":
            lcs.insert(0, x[i-1])
            i -= 1
            j -= 1
        elif table[i][j][1] == "up":
            i -= 1
        elif table[i][j][1] == "left":
            j -= 1

    return "".join(lcs)

x = "abrab"
y = "acchbrab"
print(lcs(x=x, y=y))