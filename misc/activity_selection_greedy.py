def activity_selection(S: list):
    # Sort by finish time
    S_sorted = sorted(S, key= lambda x: x[0], reverse=True)

    # Previous finish time
    last_finish = float('-inf')

    # Add compatible activities to the subset A
    A = []

    for start, finish in S_sorted:
        # Select this acitivity if it finishes after the previous activity
        if start >= last_finish:
            A.append((start, finish))
            last_finish = finish # Update last finish time for next activity

    return A


S = [(31, 34), (32, 35), (30, 33), (31, 34), (30, 33)]
print(activity_selection(S=S))