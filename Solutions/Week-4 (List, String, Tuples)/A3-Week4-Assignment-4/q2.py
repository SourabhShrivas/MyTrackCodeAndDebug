# Q2. Write a Python program to find repeated items in a tuple


def findDuplicate(tpl: tuple) -> None:
    repeted_items = []
    for item in tpl:
        if tpl.count(item) > 1:
            if item not in repeted_items:
                repeted_items.append(item)
    print(f" Repated item are : {repeted_items}")


# tpl = (1, 2, 3, 4, 3)
tpl = (1, 2, 3, 2, 4, 3, 5, 6, 4)
findDuplicate(tpl)


# """
# Write a Python program to find repeated items in a tuple.
# """
# from typing import Tuple


# def findRepeatedElements(t: Tuple):
#     repeated_elements = []
#     for i in range(len(t)):
#         if t[i] in t[i + 1 :] and t[i] not in repeated_elements:
#             repeated_elements.append(t[i])
#     return repeated_elements


# my_tuple = (1, 2, 3, 2, 4, 3, 5, 6, 4)
# repeated = findRepeatedElements(my_tuple)
# if len(repeated) > 0:
#     print(f"Repeated items = {repeated}")
# else:
#     print("No repeated elements found.")
