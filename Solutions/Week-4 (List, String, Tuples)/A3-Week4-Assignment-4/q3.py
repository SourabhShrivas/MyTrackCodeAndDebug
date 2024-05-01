# Q3. Write a Python program to check whether an element exists within a tuple.
# Ask something from user, if that exists in tuple, then print “YES” else print “NO”.


def checkElement(tpl: tuple, num: int) -> None:
    if num in tpl:
        print("yes")
    else:
        print("no")


checkElement((1, 2, 3, 2, 4, 3, 5, 6, 4), 555)


#  methid 2
def elementExistsInTuple(element, t):
    return element in t


my_tuple = (1, 2, 3, 4, 5)

e = int(input("Enter an element = "))

if elementExistsInTuple(e, my_tuple):
    print("YES")
else:
    print("NO")

print(elementExistsInTuple(22222, (1, 2, 3, 2, 4, 3, 5, 6, 4)))
