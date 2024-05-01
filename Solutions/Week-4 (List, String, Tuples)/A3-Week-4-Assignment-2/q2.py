# Q2. Make your own list of numbers.
# Ask a start and end position from User.
# Make another dierent list which will contain number
# from start to end position. Use slicing logic


def func(lst: list) -> list:
    start = int(input("Enter start position : "))
    end = int(input("Enter end position : "))

    return lst[start : end + 1]


lst = [10, -5, 8, 3, -1, -9, 7, 2]
print(func(lst))
