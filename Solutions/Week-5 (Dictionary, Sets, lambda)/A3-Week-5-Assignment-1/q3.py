"""Q3. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject which has marks
more than passing marks (above 33)."""

marks = {
    "Physics": 70,
    "Chemistory": 75,
    "Math": 80,
    "Hindi": 20,
}

for subject, mark in marks.items():
    if mark > 33:
        print(subject)
