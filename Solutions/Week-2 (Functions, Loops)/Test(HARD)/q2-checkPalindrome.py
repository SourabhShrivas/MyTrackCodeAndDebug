# Q2. Make a function named checkPalindrome which accepts an
# integer n from the user. Return True or False if the number is palindrome or not.
def reverse(n):
    reversed_num = 0
    num = n
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10
    return reversed_num


def checkPalindrome(n=int(input("Enter a number : "))):
    print(n)
    print(reverse(n))
    if reverse(n) == n:
        print("Number is Palindrom")
    else:
        print("Number is not Palindrom")


checkPalindrome()
