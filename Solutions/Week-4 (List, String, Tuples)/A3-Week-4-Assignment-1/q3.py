# Q3. Write a Python function that takes two
# lists and returns True if they have at least one common element.


def fun(my_list1, my_list2):
    # Flag = False

    # max_length = len(my_list1)
    max_list = []
    min_list = []

    if len(my_list2) >= len(my_list1):
        max_list = my_list2
        min_list = my_list1
    else:
        max_list = my_list1
        min_list = my_list2

    for index in range(0, len(max_list)):
        if max_list[index] in min_list:
            return True
        else:
            return False


def isCommon(l1: list, l2: list):
    for i in l1:
        if i in l2:
            return True
    return False


# my_list1 = [34, 11, 91, 59, 33, 22]
# my_list2 = [78, 14, 23]

my_list1 = [34, 11, 91, 59, 33, 22]
my_list2 = [78, 14, 23]

# print(fun(my_list1, my_list2))
print(isCommon(my_list1, my_list2))
