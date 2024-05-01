# Q1. Make a list of your own. Print the whole list in reverse using
# FOR loop and WHILE loop

my_list = [1, 2, 3, 4, 5, 6]
length_list = len(my_list)
reverse_list = []

# for loop
# for i in range(length_list - 1, 0 - 1, -1):
#     reverse_list.append(my_list[i])
#   print(reverse_list)

# while loop
loop_counter = length_list - 1
while loop_counter >= 0:
    reverse_list.append(my_list[loop_counter])
    loop_counter = loop_counter - 1
print(reverse_list)
