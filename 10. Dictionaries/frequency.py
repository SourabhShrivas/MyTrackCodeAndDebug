arr = [1, 4, 5, 5, 4, 6, 3, 1, 1, 1, 2, 9]
n = len(arr)
freq_map = dict()

# method 1
# for index in range(n):
#     if arr[index] in freq_map:
#         freq_map[arr[index]] = freq_map[arr[index]] + 1
#     else:
#         freq_map[arr[index]] = 1

# print(freq_map)

# method 2
# for index in range(n):
#     freq_map[arr[index]] = freq_map.get(arr[index], 0) + 1

# print(freq_map)

# method 3
for item in arr:
    freq_map[item] = freq_map.get(item, 0) + 1
    # 1       = 0+1

print(freq_map)
