def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    mid = 0
    iterations = 0
    result = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
            result = arr[mid] if result is None or arr[mid] < result else result
        else:
            return (iterations, arr[mid])

    if low < len(arr):
        result = arr[low] if result is None or arr[low] < result else result

    return (iterations, result)


arr = [2.2, 3.7, 4.5, 10, 40, 41.2, 41.3, 41.5, 45.3, 47.6, 49.8]
x = 4.7
iterations, result = binary_search(arr, x)
print(f"Number of iterations: {iterations}")
if result is not None:
    print(f"Smallest element greater than or equal to {x} is {result}")
else:
    print(f"No element greater than or equal to {x} found")
