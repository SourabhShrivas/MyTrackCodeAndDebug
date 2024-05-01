# Q5. Create a function that takes a list of positive and negative numbers.
# Return a list where the first element is the count of positive numbers and the second element is the sum of negative numbers.
# If given an empty list, return an empty list: []


def sum_neg(arr):
    result = []
    count_positive = 0
    sum_negative = 0
    n = len(arr)

    if len(arr) == 0:
        return result

    for i in range(0, n):
        if arr[i] > 0:
            count_positive = count_positive + 1
        else:
            sum_negative = sum_negative + arr[i]

    result.append(count_positive)
    result.append(sum_negative)

    return result


# print(sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]))
print(sum_neg([91, -4, 80, -73, -28]))
# print(sum_neg([]))
# print(-77 + (-90) + (-85))
