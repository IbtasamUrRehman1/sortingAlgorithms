def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0

    # Merge sorted left and right arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements, if any
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example
arr = [64,25,12,22,11]
sorted_arr = merge_sort(arr)
print("Sorted Array: ", sorted_arr)
