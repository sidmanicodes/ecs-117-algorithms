def insertion_sort(arr):
    # Destructure array (for printing purposes -- not part of the algorithm)
    new_arr = [*arr]

    # n iterations 
    for i in range(1, len(new_arr)):
        tmp = new_arr[i]

        # End of the 'sorted part' of the array is one less than i
        j = i - 1

        # As long as j doesn't go out-of-bounds AND the current value in the 
        # sorted part of the list is greater than the tmp, we should 'shift'
        # the values over to the right
        while j >= 0 and new_arr[j] > tmp:
            # Copy (shift) value to the right
            new_arr[j+1] = new_arr[j]
            j -= 1

        # We decremented j right before we exited the while loop, so we want to
        # replace the j+1 index with the tmp
        new_arr[j+1] = tmp
    return new_arr

unsorted_arr = [8, 2, 4, 1, 3]
sorted_arr = insertion_sort(unsorted_arr)
print(f"Unsorted = {unsorted_arr} --> Sorted = {sorted_arr}")
