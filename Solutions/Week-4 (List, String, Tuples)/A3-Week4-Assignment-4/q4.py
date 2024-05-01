# Q4. Write a Python program to reverse a tuple.


def reverseTuple(tpl: tuple) -> None:
    lst = list(tpl)
    reverse_list = []
    n = len(lst)
    for index in range(-1, -(n + 1), -1):
        reverse_list.append(lst[index])
    print(tuple(reverse_list))


reverseTuple((1, 3, 4, 5, 6, 7))
