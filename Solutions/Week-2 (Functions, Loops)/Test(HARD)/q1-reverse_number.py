# Q1. Make a function named reverse which accepts an integer n from the user.
# Reverse the number passed as a parameter and return the reverse number. Do not use STRINGS.


def reverse(n=int(input("Enter a number : "))):
    reversed_num = 0
    num = n
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10
    return reversed_num


print(reverse())
