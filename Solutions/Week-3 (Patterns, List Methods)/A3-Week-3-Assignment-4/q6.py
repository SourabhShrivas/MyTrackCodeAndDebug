# Q6. Create a function sumCountOddEven that accepts an List of Integers
# and calculate sum of even and odd numbers


def sumCountOddEven(l):
    length_list = len(l)
    sum_of_even = 0
    sum_of_odd = 0

    for i in range(0, length_list):
        if l[i] % 2 == 0:
            # print(f"even number {l[i]}")
            sum_of_even += l[i]
        else:
            # print(f"odd number {l[i]}")
            sum_of_odd += l[i]

    print(f"sum of even numbers are {sum_of_even}")
    print(f"sum of odd numbers are {sum_of_odd}")


my_list = [34, 11, 91, 59, 33, 22]
sumCountOddEven(my_list)
