# Q3. Make a function named printWords which accepts an integer n from the user. Print the number as words.


def wordNumber(n: int):
    result = ""
    if n == 1:
        result = "One"
    elif n == 2:
        result = "Two"
    elif n == 3:
        result = "Three"
    elif n == 4:
        result = "Four"
    elif n == 5:
        result = "Five"
    elif n == 6:
        result = "Six"
    elif n == 7:
        result = "Seven"
    elif n == 8:
        result = "Eight"
    elif n == 9:
        result = "Nine"
    elif n == 10:
        result = "Ten"
    elif n == 0:
        return "Zero"
    else:
        result = ""
    return result


def reverse(n):
    reversed_num = 0
    num = n
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10
    return reversed_num


def printWords(n=int(input("Enter a number : "))):
    num = n
    reversed_num = reverse(n)
    print(reversed_num)

    while reversed_num > 0:
        last_digit = reversed_num % 10
        # print(last_digit, end=" ")
        word = wordNumber(last_digit)
        print(word, end=" ")
        reversed_num = reversed_num // 10


printWords()
