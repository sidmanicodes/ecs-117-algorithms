from mat_print import pretty_print_matr

def sequence_alignment(seq1, seq2, gap_cost, match_score, mismatch_cost):
    m, n = len(seq1), len(seq2)
    table = [[(0, None) for _ in range(n+1)] for _ in range(m+1)]

    # Initialize table
    for i in range(m):
        # We make deletions along the first column, because we are transforming seq1[0:m]
        # into nothing
        table[i][0] = (-gap_cost * i, "up") # Deletion means we insert a gap in sequence 2
    for j in range(n):
        # We make insertions along the first row, because we are inserting seq2[0:n] 
        # into nothing
        table[0][j] = (-gap_cost * j, "left") # Insertion means we insert a gap into sequence 1
    
    # Fill table
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Cases 1 + 3: either a match or mimatch (meaning we require substitution)
            match_case = (
                table[i-1][j-1][0] + (match_score if seq1[i-1] == seq2[j-1] else -mismatch_cost), 
                "diag"
            )
            # Case 2: insertion or deletion, meaning we require a gap
            insert_case = (table[i][j-1][0] - gap_cost, "left")
            delete_case = (table[i-1][j][0] - gap_cost, "up")

            # Determine the maximum score
            max_score = max(match_case[0], insert_case[0], delete_case[0])

            if max_score == match_case[0]: table[i][j] = match_case
            elif max_score == insert_case[0]: table[i][j] = insert_case
            else: table[i][j] = delete_case

    # Create alignment strings
    seq1_aligned = ""
    seq2_aligned = ""

    i, j = m, n

    while i > 0 or j > 0:
        if table[i][j][1] == "diag":
            seq1_aligned = seq1[i-1] + seq1_aligned
            seq2_aligned = seq2[j-1] + seq2_aligned
            i -= 1
            j -= 1
        elif table[i][j][1] == "up":
            seq1_aligned = seq1[i-1] + seq1_aligned
            seq2_aligned = "_" + seq2_aligned
            i -= 1
        elif table[i][j][1] == "left":
            seq1_aligned = "_" + seq1_aligned
            seq2_aligned = seq2[j-1] + seq2_aligned
            j -= 1

    return (seq1_aligned, seq2_aligned)

# Example usage
seq1 = "AFGT"
seq2 = "ACGT"
aligned_seq1, aligned_seq2 = sequence_alignment(seq1=seq1, seq2=seq2, gap_cost=1, match_score=1, mismatch_cost=3)
print("Sequence 1 Aligned:", aligned_seq1)
print("Sequence 2 Aligned:", aligned_seq2)
