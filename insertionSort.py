def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        # swap elements to find the correct position for the current value
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value


# Example array
my_list = [6, 43, 6, 5, 2, 3, 45, 9, 0, 1]
insertion_sort(my_list)
print("Sorted Array: ", my_list)
