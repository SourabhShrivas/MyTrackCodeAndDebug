# Q4. Create a function that takes a list of numbers and returns the number
# that's unique.

# unique([3, 3, 3, 7, 3, 3]) ➞ 7
# unique([0, 0, 0.77, 0, 0]) ➞ 0.77
# unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0


# method 1
def unique1(arr):
    result = []
    n = len(arr)
    for i in range(0, n):
        if arr.count(arr[i]) == 1:
            result.append(arr[i])
    return result


print(unique1([3, 3, 3, 7, 3, 3]))
print(unique1([0, 0, 0.77, 0, 0]))
print(unique1([0, 1, 1, 1, 1, 1, 1, 1]))


# method 2 - this is not correct for thsi q as question is to return only unique numberss
def unique_1(arr):
    result = []
    n = len(arr)
    for i in range(0, n):
        if arr[i] not in result:
            result.append(arr[i])
    return result


print(unique_1([3, 3, 3, 7, 3, 3]))
print(unique_1([0, 0, 0.77, 0, 0]))
print(unique_1([0, 1, 1, 1, 1, 1, 1, 1]))
