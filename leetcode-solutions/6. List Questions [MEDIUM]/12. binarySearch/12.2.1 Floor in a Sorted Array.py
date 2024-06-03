"""https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1"""


# based on Lower Bound concept
class Solution:

    def findFloor(self, A, N, X):
        low = 0
        high = N - 1
        lb = N

        while low <= high:
            mid = (low + high) // 2
            if A[mid] >= X:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb - 1  # -1 as this is looking for floor from LB


N = 7  # length of array
X = 5  # target variable
A = [1, 2, 8, 10, 11, 12, 19]  # given array

# N = 7
# X = 0
# A = [1, 2, 8, 10, 11, 12, 19]

N = 65
X = 106
A = [
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
    123,
    124,
    125,
    126,
    127,
    128,
    129,
    130,
]

a = Solution()
print(a.findFloor(A, N, X))
