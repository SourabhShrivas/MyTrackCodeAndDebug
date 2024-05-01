"""Q8. Ask a string from user. Print the string with first 2 letters and last 2 letters.
Example string: aeroplane
Output:"""


def func() -> None:
    s = str(input("Enter a string : "))
    if len(s) < 3:
        print("INVALID")
    else:
        print(s[0:2] + s[-2:])


func()
