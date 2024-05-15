"""https://www.naukri.com/code360/problems/insertion-sort_624381"""

""""""


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
    return arr


arr = [28, 2, 13, 4, 1, 3, 6, 28]
print(insertionSort(arr))
"""
TC - n(n+1)/2 ~ O(n^2) (sum of n natural number )
SC - O(1)

"""
