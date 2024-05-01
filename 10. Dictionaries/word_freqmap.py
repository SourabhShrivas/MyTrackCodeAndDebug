str = "aaaa bd c ba"
freq_map = dict()

for ch in str:
    freq_map[ch] = freq_map.get(ch, 0) + 1

print(freq_map)
