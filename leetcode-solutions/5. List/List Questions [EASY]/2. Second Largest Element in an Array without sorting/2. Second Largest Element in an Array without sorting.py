"""https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960"""


# BruteFource
def getSecondOrderElements_BF(arr: [int]) -> [int]:
    arr.sort()  # O(nlogn)
    result = []
    second_large_element = arr[-2]  # constent time operations
    second_small_element = arr[1]

    return [second_large_element, second_small_element]


arr = [1, 2, -100, 4.7, 5, 120, 100]  # -100,1,2,4.7,5,100,120
# n = 5,
# arr = [1, 2, 3, 4, 5]
# Output: [4, 2]
print(getSecondOrderElements_BF(arr))
"""
TC - O(nlogn)
SC - O(1)
"""


# Better
def getSecondOrderElements_better(arr: [int]) -> [int]:
    small, ssmall, large, slarge = (
        float("inf"),
        float("inf"),
        float("-inf"),
        float("-inf"),
    )
    n = len(arr)

    for i in range(n):  # O(n)
        small = min(small, arr[i])
        large = max(large, arr[i])

    for i in range(n):  # O(n)
        if arr[i] < ssmall and arr[i] != small:
            ssmall = arr[i]

        if arr[i] > slarge and arr[i] != large:
            slarge = arr[i]
    return [slarge, ssmall]


arr = [1, 2, -100, 4.7, 5, 120, 100]  # -100,1,2,4.7,5,100,120
# n = 5,
# arr = [1, 2, 3, 4, 5]
# Output: [4, 2]
print(getSecondOrderElements_better(arr))
"""
TC -  O(n) + O(n) = O(2n)
SC - O(1)
"""


# Optimal
# Optimal
def getSecondOrderElements_optimal(arr: [int]) -> [int]:
    small, ssmall, large, slarge = (
        float("inf"),
        float("inf"),
        float("-inf"),
        float("-inf"),
    )
    n = len(arr)
    for i in range(n):  # O(n)
        if arr[i] > large:  # 0
            # print(arr[i])  # 1
            slarge = large  # -inf
            large = arr[i]  # 1
        elif arr[i] > slarge and arr[i] != large:
            # print(arr[i])
            slarge = arr[i]

        if arr[i] < small:
            ssmall = small
            small = arr[i]
        elif arr[i] < ssmall and arr[i] != small:
            ssmall = arr[i]

    return [slarge, ssmall]


arr = [1, 2, -100, 4.7, 5, 120, 100]  # -100,1,2,4.7,5,100,120
# n = 5,
# arr = [1, 2, 3, 4, 5]
# Output: [4, 2]
print(getSecondOrderElements_optimal(arr))

"""
TC - O(n)
SC - O(1)
"""
