"""Q2. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks
scored"""

marks = {
    "Physics": 70,
    "Chemistory": 75,
    "Math": 80,
    "Hindi": 78,
}

high_score = 0
highest_score_subject_name = ""

for subject, mark in marks.items():
    if mark > high_score:
        high_score = mark
        highest_score_subject_name = subject

print(highest_score_subject_name)
