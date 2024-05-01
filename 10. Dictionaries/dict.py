marks = {
    "science": 78,
    "english": 91,
    "maths": 56,
    "hindi": 84,
    "gender": "Male",
    "adult": False,
    "phone_number": [985698, 774455, 4111125],
}

print(marks["science"])
print(marks.get("sciencje", "key in not available"))
