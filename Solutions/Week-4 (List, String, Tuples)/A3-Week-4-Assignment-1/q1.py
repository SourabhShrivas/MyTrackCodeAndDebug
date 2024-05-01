# Q1. Make a list of your own. Make two more empty list like odd and
# even. Put all the even numbers from original list to even and odd numbers to
# odd and print both lists. (Don’t remove anything from original one).

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []

n = len(my_list)
for index in range(0, n):
    if my_list[index] % 2 == 0:
        even.append(my_list[index])
    else:
        odd.append(my_list[index])

print(f"Original list is :{my_list}")
print(f"Odd number list is : {odd}")
print(f"Even number list is : {even}")
