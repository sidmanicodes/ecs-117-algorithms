def max_subarray(arr, start=0, end=None):
    if not end:
        end = len(arr)

    if end - start == 1:
        return (start, end, arr[start])

    m = (start + end) // 2
    l_i, l_j, max_l = max_subarray(arr=arr, start=start, end=m)
    r_i, r_j, max_r = max_subarray(arr=arr, start=m, end=end)
    x_i, x_j, max_x = max_crossing_sum(arr=arr, start=start, end=end, m=m)
    if max_l > max_r and max_l > max_x:
        return (l_i, l_j, max_l)
    elif max_r > max_l and max_r > max_x:
        return (r_i, r_j, max_r)
    return (x_i, x_j, max_x)

def max_crossing_sum(arr, start, end, m):
    max_sum_left = float('-inf')
    left_sum = 0
    max_left_index = m
    
    # Iterate over the left half of the array
    for i in range(m, start - 1, -1):
        left_sum += arr[i]

        # If the current left sum is greater than the maximum 
        # left sum, increase the size of the left subarray
        if left_sum >= max_sum_left:
            max_sum_left = left_sum
            max_left_index = i
    
    max_sum_right = float('-inf')
    right_sum = 0
    max_right_index = m + 1

    # Iterate over right half of the subarray
    for i in range(m+1, end):
        right_sum += arr[i]
        if right_sum >= max_sum_right:
            max_sum_right = right_sum
            max_right_index = i

    return (max_left_index, max_right_index, max_sum_left+max_sum_right)

arr = [1, 4, 3, 4, 2, 1]
print(max_subarray(arr))