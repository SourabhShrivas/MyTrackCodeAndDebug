details = {
    "Anirudh": [10, 20, 50, 30, 87],
    "Arun": [10, 95, 30, 45],
    "Ankit": [20, 90, 80],
    "Ram": [50, 20, 55, 30, 77],
    "Shyam": [10, 88, 50, 20, 87],
}

# print(details.values())
for name, marks in details.items():
    totalMarks = sum(marks)
    print(f"{name} has scored {totalMarks}")

# print(sum([10, 20, 50]))
