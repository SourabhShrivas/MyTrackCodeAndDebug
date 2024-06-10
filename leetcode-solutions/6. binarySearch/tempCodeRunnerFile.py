def func(arr, target):
    n = len(arr)
    l = 0
    h = n - 1
    ub = n

    while l <= h:
        mid = (l + h) // 2
        if arr[mid] > target:
            ub = mid
            high = mid - 1
        else:
            l = mid + 1
    return ub


arr = [4, 6, 7, 7, 7, 8, 10, 10, 14, 19]
target = 6
print(func(arr, target))