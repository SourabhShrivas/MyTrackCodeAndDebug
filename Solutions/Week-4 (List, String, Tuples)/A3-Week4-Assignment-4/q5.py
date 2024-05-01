"""
Q5. Write a Python program to check if a string has at least one
letter and one number. If it has at least one
letter and one number then print YES else print NO.
"""


def checkString(s: str) -> None:
    is_number = False
    is_alpha = False

    for ch in s:
        ascii_code = ord(ch)
        if (ascii_code >= 65 and ascii_code <= 90) or (
            ascii_code >= 97 and ascii_code <= 122
        ):
            is_alpha = True

        elif ascii_code >= 48 and ascii_code <= 57:
            is_number = True

    if is_alpha == True and is_number == True:
        print("Yes")
    else:
        print("No")


s = "*%$^$^#$#^($^)9"
checkString(s)
