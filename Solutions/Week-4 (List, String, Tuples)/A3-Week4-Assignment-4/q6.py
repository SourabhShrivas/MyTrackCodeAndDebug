"""Q6. Write a python program to ask a string from user.
 Then count the number of vowels and number of consonants in that string."""


def func() -> None:
    s = str(input("Enter a String : "))
    countvovels = 0
    for ch in s:
        if ch.lower() in ["a", "e", "i", "o", "u"]:
            countvovels += 1
    print(f"number of vowels in entered string : {countvovels}")


func()
