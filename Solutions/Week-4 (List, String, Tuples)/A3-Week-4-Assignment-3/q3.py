# Q3. Create a function findLargest that accepts an
# List of Integers and returns the largest number from the list.


def findLargest(lst: list) -> int:
    max_num = lst[0]
    for item in lst:
        if item > max_num:
            max_num = item

    return max_num


lst = [34, 11, 91, 59, 33, 22]
print(findLargest(lst))
