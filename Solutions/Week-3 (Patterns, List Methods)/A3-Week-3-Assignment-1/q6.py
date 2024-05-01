def pattern(n=5):
    for i in range(1, n + 1):
        for j in range(n, n + 2 - i, -1):  # need to think
            print(j, end=" ")
        print()


pattern()
