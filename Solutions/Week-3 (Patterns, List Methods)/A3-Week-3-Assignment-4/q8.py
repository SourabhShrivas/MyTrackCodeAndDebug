# Q8. Create a function findSmallest that accepts an List of
# Integers and returns the smallest number from the list.


def findSmallest(l):
    length_list = len(l)
    largets_num = l[0]

    for i in range(0, length_list):
        if l[i] < largets_num:
            largets_num = l[i]
    print(largets_num)


my_list = [34, 11, 91, 59, 33, 22, 11111, 0]
findSmallest(my_list)
