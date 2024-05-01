def add_digit(n: int):
    sum = 0
    num = n
    while num > 0:
        # print(sum)
        sum = sum + num % 10
        # print(num)
        num = num // 10
        # print("--------------------")
    print(f"{sum}")


add_digit(12883)
