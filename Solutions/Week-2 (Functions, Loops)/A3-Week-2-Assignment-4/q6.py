# Q6. Don’t create a function, just print
# the following pattern
# 1  11  111  1111  11111....n times (Ask n from user)
n = int(input("Enter the value of n: "))

#  with for loop
# x = "1"
# for i in range(1, n + 1):
#     print(x * i, end=" ")
# print(n)

# with while loop - method 1
# i = 1
# while i <= n:
#     # x = str("1") * i
#     print(str("1") * i)
#     i += 1

# with while loop - method 1
i = 1
x = 1
while i <= n:
    print(x)
    x = (x * 10) + 1
    i += 1
