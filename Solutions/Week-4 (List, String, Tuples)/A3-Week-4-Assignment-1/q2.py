# Q2. Write a function to remove duplicates from a list and print them.


def remove_duplilcate(my_list: list):
    result = []
    for index in range(0, len(my_list)):
        if my_list[index] not in result:
            result.append(my_list[index])
    return result


my_list = [1, 2, 3, 4, 2, 3, 4, 1, 5, 6, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9]
print(remove_duplilcate(my_list))
