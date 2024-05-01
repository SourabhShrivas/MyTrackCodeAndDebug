# Q5. Write a program to put all the common elements (in 2 lists)
# in another list and print it using function.


def Common(l1: list, l2: list):
    result = []
    for i in l1:
        if i in l2:
            result.append(i)
    return result


l1 = [34, 11, 91, 59, 33, 22]
l2 = [78, 14, 23, 34, 11]

print(Common(l1, l2))
