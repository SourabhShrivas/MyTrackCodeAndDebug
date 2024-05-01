"""Q1. Write a function in Python that counts the number of digits in a
 given string using ASCII codes.
Input: "Room 101"Output: 3"""


# method 1
def func1() -> None:
    s = str(input("Enter string: "))
    count_digit = 0

    for ch in s:
        if ch.isdigit():
            count_digit = count_digit + 1

    print(f"number of difit in entered string is : {count_digit}")


# func1()


# method 2
def func2() -> None:
    s = str(input("Enter string: "))
    count_digit = 0

    for ch in s:
        ascii_code = ord(ch)
        if ascii_code >= 48 and ascii_code < 57:
            count_digit = count_digit + 1

    print(f"number of difit in entered string is : {count_digit}")


func2()
