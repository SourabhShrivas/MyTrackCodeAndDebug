"""
Q2. Keep asking characters from user until he presses q on the keyboard. 
Change all the capital letters to small, and all the small letters to capital. 
(Don’t use swapcase() )
"""


def func():
    result_string = ""
    user_input = " "

    while ord(user_input) != ord("q"):
        user_input = input("Enter a Character : ")
        ascii_code = ord(user_input)
        if ascii_code >= 65 and ascii_code <= 90:
            result_string = result_string + chr(ascii_code).lower()
        elif ascii_code >= 97 and ascii_code <= 122:
            result_string = result_string + chr(ascii_code).upper()
        else:
            result_string = result_string + chr(ascii_code)

    return result_string


print(func())
# print(chr(65))
