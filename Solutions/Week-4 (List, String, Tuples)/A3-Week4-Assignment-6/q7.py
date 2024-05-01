"""Q7. Write a function which 
accepts a String and another string 
(which will be a single character) as a parameter. Join that 
string along with that character but in reverse."""


def func(s1: str, ch: str) -> str:
    word_lst = s1.split(" ")
    reverse_word_list = []

    for index in range(len(word_lst) - 1, -1, -1):
        reverse_word_list.append(word_lst[index])

    return ch.join(reverse_word_list)


s1 = "humse dsa ho jayega"
ch = "@"
print(func(s1, ch))
