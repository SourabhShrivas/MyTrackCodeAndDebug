"""Q6. Ask a string from user. Store the frequency of each character in the dictionary. 
Then print the character with the maximum frequency."""


def func() -> str:
    str = input("Enter a string : ")
    freq_map = dict()

    for ch in str:
        freq_map[ch] = freq_map.get(ch, 0) + 1

    max_frequency = 0
    max_frequency_char = ""

    print(freq_map)

    for ch, frequency in freq_map.items():
        if frequency > max_frequency:
            max_frequency = frequency
            max_frequency_char = ch

    # print(freq_map)

    return max_frequency_char


print(func())


# def filter_string_values(d):
#     return {k: v for k, v in d.items() if isinstance(v, str)}


# d = {"science": 5, "english": 2, "Physics": "40"}

# print({k: v for k, v in d.items() if type(v) == int})

# lst = [1, 2, 3, 4, 5, 6]
# print([x * x for x in lst if x < 4])


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# a = [ for x ]

# print(newlist)
