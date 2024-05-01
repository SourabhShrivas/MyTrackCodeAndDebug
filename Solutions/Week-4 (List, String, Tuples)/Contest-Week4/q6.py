"""
Q6. Make a password strength function. It will accept a string from user. 
Return True if it is a strong password.Strong password has these characteristics.
Minimum 8 character
Minimum 1 uppercase alphabet
Minimum 1 lowercase alphabet
Contains at least 1 special symbol (any symbol)
Minimum 1 digit
"""


def func(str: str) -> bool:
    flag = False

    if len(str) < 8:
        flag = False
    else:
        for ch in str:
            ascii_code = ord(ch)
            if (
                (ascii_code <= 65 and ascii_code <= 90)
                and (ascii_code <= 97 and ascii_code <= 122)
                and (ascii_code <= 48 and ascii_code <= 57)
            ):
                flag = True
            else:
                flag = False
    return flag


# str = "asdf"
#  will return false

str = "Abcdefgh1"
#  will return True

print(func(str))
