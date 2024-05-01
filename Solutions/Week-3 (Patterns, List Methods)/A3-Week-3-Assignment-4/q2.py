# Q2. Make a list of your own. Print all the numbers divisible by 3 and 4 in that list.

my_list = [1, 2, 3, 4, 5, 6]
length_list = len(my_list)
result_list = []

for i in range(1, length_list):
    if my_list[i] % 3 == 0 and my_list[i] % 4 == 0:
        result_list.append(my_list[i])

print(result_list)
