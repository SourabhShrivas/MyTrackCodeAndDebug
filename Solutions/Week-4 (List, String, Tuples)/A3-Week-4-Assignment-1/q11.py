# Q11. Write a python program which prints all the values
# whose count is greater than 3. (Make sure to make a list with at least 15 numbers)


def func(lst: list):
    temp_list = []
    for item in lst:
        if lst.count(item) > 3:
            if item not in temp_list:
                temp_list.append(item)
    print(temp_list)


lst = [1, 2, 3, 43, 2, 2, 2, 2, 2, 3, 3, 3, 1, 2, 3, 43, 2]
func(lst)

# print(lst.count(lst()))
