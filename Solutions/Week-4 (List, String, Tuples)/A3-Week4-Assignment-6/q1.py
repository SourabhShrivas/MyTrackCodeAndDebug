"""Q1. Ask a string from user.
 If the length of string is odd, 
 then change all the capital letters to small and vice versa, 
 but if the length of string is even, 
reverse the string. Do this using a function and return the output"""


def func() -> str:
    string = str(input("Enter the string : "))
    result = ""

    if len(string) % 2 == 0:
        result = string[::-1]
    else:
        for ch in string:
            ascii_code = ord(ch)
            if ascii_code >= 65 and ascii_code <= 90:
                result = result + ch.lower()
            elif ascii_code >= 97 and ascii_code <= 120:
                result = result + ch.upper()

    return result


print(func())
