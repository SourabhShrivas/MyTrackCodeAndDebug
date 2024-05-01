"""Q1. Make a dictionary with keys as subject name (physics, chemistry, etc.) 
and values as their marks. Print the highest marks scored."""

marks = {
    "Physics": 70,
    "Chemistory": 75,
    "Math": 80,
    "Hindi": 78,
}

# method 1
# print(max(list(marks.values())))

# method 2
high_score = 0
for mark in marks.values():
    if mark > high_score:
        high_score = mark
print(f"highest score is :{high_score}")
