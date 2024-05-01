# Break, Continue -> LOOPS
def pattern() -> None:
    i = 1
    while i <= 10:
        print(i)
        if i == 5:
            break
        i += 1
    print("Done1")
    print("Done2")


pattern()


i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1


n = 10
