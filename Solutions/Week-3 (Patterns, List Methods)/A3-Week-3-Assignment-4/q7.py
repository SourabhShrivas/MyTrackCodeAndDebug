# Q7. Create a function findLargest that accepts an List of
# Integers and returns the largest number from the list.


def findLargest(l):
    length_list = len(l)
    largets_num = 0

    for i in range(0, length_list):
        if l[i] > largets_num:
            largets_num = l[i]
    print(largets_num)


my_list = [34, 11, 91, 59, 33, 22, 11111]
findLargest(my_list)
