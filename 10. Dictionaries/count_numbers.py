arr = [1, 4, 5, 5, 4, 6, 3, 1, 1, 1, 2, 9]
n = len(arr)
freq_map = dict()  # { }

""" Method 1 - (basic)"""
for index in range(n):
    if arr[index] in freq_map:
        freq_map[arr[index]] = freq_map[arr[index]] + 1
    else:
        freq_map[arr[index]] = 1


""" Method 2 - (advance)"""

for index in range(n):
    freq_map[arr[index]] = freq_map.get(arr[index], 0) + 1

"""main"""
print(freq_map)
