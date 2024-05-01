# Q7. Keep asking numbers from user
# until the user enters 0. Then display the average of all numbers.

# Method 1
# i = 1
# m = 1
# sum = 0
# count = 1
# avg = 0
# while i <= m:
#     n = int(input(f"Enther a number (enter 0 to finish):"))
#     if n == 0:
#         print(f"average of number entered by you is {avg}")
#         break
#     else:
#         sum = sum + n
#         count = count + 1
#     avg = sum / count
#     i += 1
#     m += 1

# method 2
# i = 1
# count = 0
# total = 0
# n = 1
# while n > 0:
#     n = int(input(f"Enther a number (enter 0 to finish):"))
#     count = count + 1
#     total = total + n
#     i += 1
# avg = sum / count
# print(f"average of number of entered by is : {avg}")

# method 3
total = 0
count = 0
while True:
    num = int(input("Enther a number (enter 0 to finish): "))
    total = total + num
    count = count + 1
    if num == 0:
        break
print(f"Average of entered number is : {total/count}")
