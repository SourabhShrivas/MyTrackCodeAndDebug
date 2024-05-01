# Q4. Make a list of your own. Calculate
# the length of that list without using len() function.

my_list = [1, 2, 3, 4, 5, 6, 15]
length_list = len(my_list)
count = 0

for i in range(1, length_list):
    count += 1
print(count)
