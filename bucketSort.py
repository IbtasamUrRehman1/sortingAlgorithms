def bucketSort(arr):
    max_value = max(arr)
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    for num in arr:
        index = int(num * num_buckets / (max_value + 1))
        buckets[index].append(num)
    return sorted([num for bucket in buckets for num in bucket])

# Example
arr = [0.23, 0.65, 0.12, 0.78, 0.48, 0.91, 0.53]
sorted_arr = bucketSort(arr)
print("Sorted array is :", sorted_arr)