n = 13
for i in range(1, n // 2 + 1 + 1):
    for j in range(1, n // 2 - i + 1 + 1):
        print(" ", end=(" "))

    for k in range(1, 2 * i - 1 + 1):
        print(i, end=" ")

    print()

for i in range(n // 2, 0, -1):
    for j in range(1, n // 2 - i + 2):
        print(" ", end=" ")

    for k in range(1, 2 * i - 1 + 1):
        print(i, end=" ")

    print()
