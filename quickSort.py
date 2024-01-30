def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(less) + equal + quicksort(greater)


# array
arr = [7, 8, 5, 6, 7, 1, 5, 3, 5, 6, 10, 0]
sorted_arr = quicksort(arr)
print("Sortedc Array: ", sorted_arr)