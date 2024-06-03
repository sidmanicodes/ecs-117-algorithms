def merge_sort_array(arr):
    """
    This function performs a merge sort on the passed array
    This implementation is NOT in-place
    """
    def merge(left, right):
        """
        This is a sub-function to merge the individual sorted left
        and right subarrays
        """
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # Base case
    if len(arr) < 2:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    sorted_left = merge_sort_array(left)
    sorted_right = merge_sort_array(right)

    return merge(sorted_left, sorted_right)

if __name__ == '__main__':
    my_arr = [5, 1, 4, 2]
    print(f"Before: {my_arr} | After: {merge_sort_array(my_arr)}")