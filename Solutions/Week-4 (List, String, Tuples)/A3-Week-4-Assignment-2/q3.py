def func(lst, n):
    # lst = input("Enter a list  : ")
    # n = int(input("Enter a number : "))
    n1 = len(lst)
    return lst[n1 - 3 :]


lst = [10, -5, 8, 3, -1, -9, 7, 2]
n = 3
# print(lst[4:])
print(func(lst, n))
