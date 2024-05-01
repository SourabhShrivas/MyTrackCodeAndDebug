# Q4. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements
# of the original list but in reverse order. Using slicing logic.


def func(lst, n):
    # lst = input("Enter a list  : ")
    # n = int(input("Enter a number : "))
    n1 = len(lst)
    return lst[-1 : -n - 1 : -1]


lst = [10, -5, 8, 3, -1, -9, 7, 2]
n = 4
# print(lst[4:])
print(func(lst, n))

# lst = [10, -5, 8, 3, -1, -9, 7, 2]
# print(lst[0:5:])
