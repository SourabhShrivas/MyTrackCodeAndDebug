# Q2. Create a function sumCountOddEven that accepts an
# List of Integers and calculate sum of even and odd numbers.


def sumOddEven(lst: list) -> None:
    sum_odd = 0
    sum_even = 0
    for item in lst:
        if item % 2 == 0:
            sum_even = sum_even + item
        else:
            sum_odd = sum_odd + item

    print(f"Sum of even numbers : {sum_even}")
    print(f"Sum of odd numbers : {sum_odd}")


lst = [34, 11, 91, 59, 33, 22]
sumOddEven(lst)
