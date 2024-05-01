# Q1. Create a function countOddEven that accepts an List of Integers and print how
# many even and odd numbers are there.


def countOddEven(lst: list) -> None:
    count_odd = 0
    count_even = 0
    for item in lst:
        if item % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1

    print(f"Total number of even numbers : {count_even}")
    print(f"Total number of odd numbers : {count_odd}")


lst = [34, 11, 91, 59, 33, 22]
countOddEven(lst)
