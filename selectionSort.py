def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example unsorted array
my_list = [64,35,1,0,2,3,]
selectionSort(my_list)
print("Sorted List: ", my_list)