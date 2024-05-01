# Q3. Make a list of your own. Count how many numbers are divisible by 5.

my_list = [1, 2, 3, 4, 5, 6, 15]
length_list = len(my_list)
result_list = []

for i in range(1, length_list):
    if my_list[i] % 5 == 0:
        result_list.append(my_list[i])

print(result_list)
