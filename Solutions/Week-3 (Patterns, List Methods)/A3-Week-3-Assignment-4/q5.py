# Q5. Create a function countOddEven that accepts an List of Integers and print
# how many even and odd numbers are there.

my_list = [34, 11, 91, 59, 33, 22]


def countOddEven(l):
    length_list = len(l)
    number_of_even = 0
    number_of_odd = 0

    for i in range(0, length_list):
        if l[i] % 2 == 0:
            # print(f"even number {l[i]}")
            number_of_even += 1
        else:
            # print(f"odd number {l[i]}")
            number_of_odd += 1

    print(f"Number of even numbers are {number_of_even}")
    print(f"Number of odd numbers are {number_of_odd}")


countOddEven(my_list)
