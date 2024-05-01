# Q2. Given a number, return a list containing the two halves of the number.
# If the number is odd, make the rightmost number higher.Examples

# series_resistance([1, 5, 6, 3]) ➞ "15 ohms"
# series_resistance([16, 3.5, 6]) ➞ "25.5 ohms"
# series_resistance([0.5, 0.5]) ➞ "1.0 ohm"
# number_split(4) ➞ [2, 2]
# number_split(10) ➞ [5, 5]
# All numbers will be integers.


def series_resistance(n: int):
    split_num = []

    n1 = int(n / 2)
    n2 = n - n1

    if n1 > n2 and n % 2 != 0:
        split_num.append(n2)
        split_num.append(n1)
    else:
        if n >= 0:
            split_num.append(n1)
            split_num.append(n2)
        else:
            split_num.append(n2)
            split_num.append(n1)

    print(split_num)


# def series_resistance(n):
#     return [n // 2, n - n // 2]


print(series_resistance(-9))
