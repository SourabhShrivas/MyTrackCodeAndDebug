"""
Floor/Ceil in Sorted Array
https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401
https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1
"""


def getFloorAndCeil(a, n, x):
    floor = -1
    ceil = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return x, x
        elif a[mid] > x:
            ceil = a[mid]
            high = mid - 1
        else:
            floor = a[mid]
            low = mid + 1
    return floor, ceil


n = 6
x = 8
# a = [3, 4, 4, 7, 8, 10]
a = [3, 4, 4, 7, 8, 10]
print(getFloorAndCeil(a, n, x))

# def getFloorAndCeil(a, n, x):
#     # Write your code here.
#     # n = len(arr)
#     l = 0
#     h = n - 1
#     lb = n
#     # floor = n
#     # ceil = n

#     while l <= h:
#         m = (l + h) // 2
#         if a[m] >= x:
#             lb = m
#             # floor = arr[m]
#             h = m - 1
#         else:
#             l = m + 1

#     l = 0
#     h = n - 1
#     ub = n
#     while l <= h:
#         m = (l + h) // 2
#         if a[m] > x:
#             ub = m
#             # ceil = arr[m]
#             h = m - 1
#         else:
#             l = m + 1

#     return [a[lb], a[ub]]
