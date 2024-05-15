"""https://www.naukri.com/code360/problems/bubble-sort_624380"""

"""Adjustcent swap"""

"""
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted. 
It is called "bubble" sort because smaller elements "bubble" to the top of the list with each pass.
"""

from typing import List


def bubbleSort(arr: List[int], n: int):
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:  # change > to < if need to sort in decending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


n = 7
arr = [2, 13, 4, 1, 3, 6, 28]
print(bubbleSort(arr, n))

'''Time complexity of Bubble Sort:Best case: O(n) when the list is already sorted. This is because it requires only one pass through the list to check if it is sorted.
Worst case and average case: O(n^2) where n is the number of elements in the list. This is because in the worst and average cases, the algorithm requires multiple passes through the list, and each pass compares and potentially swaps every pair of elements.
TC  - O(n^2)

Space complexity:
O(1)
Bubble sort is an in-place sorting algorithm, meaning it does not require any extra space other than the input array itself. Therefore, its space complexity is O(1), indicating constant space usage regardless of the size of the input."""
'''
