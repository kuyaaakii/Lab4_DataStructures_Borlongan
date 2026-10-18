from constants import *
from collections import defaultdict
# Generate individualized student performance records from the student-specific inputs.
student_performance_records = {}
student_names = [c.upper() for c in LAST_NAME[0:5]]
student_scores1 = {
    "math": SEED_NUM + (ord(FAVORITE_ARTIST[1].lower()) - 28), 
    "programming": SEED_NUM + (ord(FAVORITE_ARTIST[1].lower()) - 39), 
    "electronics": SEED_NUM + (ord(FAVORITE_ARTIST[1].lower()) - 35), 
    "physics": SEED_NUM + (ord(FAVORITE_ARTIST[1].lower()) - 33), 
    "english": SEED_NUM + (ord(FAVORITE_ARTIST[1].lower()) - 37) 
}
student_scores2 = {
    "math": SEED_NUM + (ord(FAVORITE_ARTIST[2].lower()) - 28), 
    "programming": SEED_NUM + (ord(FAVORITE_ARTIST[2].lower()) - 39), 
    "electronics": SEED_NUM + (ord(FAVORITE_ARTIST[2].lower()) - 35), 
    "physics": SEED_NUM + (ord(FAVORITE_ARTIST[2].lower()) - 45), 
    "english": SEED_NUM + (ord(FAVORITE_ARTIST[2].lower()) - 37) 
}
student_scores3 = {
    "math": SEED_NUM + (ord(FAVORITE_ARTIST[3].lower()) - 28), 
    "programming": SEED_NUM + (ord(FAVORITE_ARTIST[3].lower()) - 19), 
    "electronics": SEED_NUM + (ord(FAVORITE_ARTIST[3].lower()) - 25), 
    "physics": SEED_NUM + (ord(FAVORITE_ARTIST[3].lower()) - 37), 
    "english": SEED_NUM + (ord(FAVORITE_ARTIST[3].lower()) - 27) 
}
student_scores4 = {
    "math": SEED_NUM + (ord(FAVORITE_ARTIST[4].lower()) - 12), 
    "programming": SEED_NUM + (ord(FAVORITE_ARTIST[4].lower()) - 29), 
    "electronics": SEED_NUM + (ord(FAVORITE_ARTIST[4].lower()) - 35), 
    "physics": SEED_NUM + (ord(FAVORITE_ARTIST[4].lower()) - 33), 
    "english": "MISSING" 
}
student_scores = [student_scores1, student_scores2, student_scores3, student_scores4]
print("=" * 30, "GENERATED PERFORMANCE RECORDS", "=" * 30)
print(f"Names: {student_names}")
print(student_scores1)
print(student_scores2)
print(student_scores3)
print(student_scores4)

#Organize the records so that student and subject performance can be analyzed together. And determine repeated/incomplete records
organized_student_data = {}
n = 0
for name in student_names:
    if name in organized_student_data:
        organized_student_data[name]["status"] = 'Repeated Student-Subject Record'
        break
    else:
        organized_student_data[name] = {}
        if n == 4:
            organized_student_data[name]["scores"] = student_scores[1]
            break
        organized_student_data[name]["scores"] = student_scores[n]
        organized_student_data[name]["status"] = 'Valid'
    n+=1

for student, info in organized_student_data.items():
    for subject, score in info['scores'].items():
        if score == "MISSING":
            info['scores'][subject] = "X"
            info['status'] = "1 Missing Score"

print("=" * 30, " ORGANIZED STUDENT DATA & REPEATED/INCOMPLETE RESULTS", "=" * 30)

for student, info in organized_student_data.items():
    print(f"Student Name: {student}")
    for subject, score in info['scores'].items():
        print(f"  {subject.capitalize()} Exam Score: {score}")
    print(f"  Status: {info["status"]}")
    print("-" * 30)

#Determine the performance category
for student, info in organized_student_data.items():
    info["performance"] = {}

    for subject, score in info["scores"].items():
        if score == "X" or score == "MISSING":
            category = "Incomplete"
        elif score >= 90:
            category = "Excellent"
        elif score >= 80:
            category = "Good"
        elif score >= 75:
            category = "Passed"
        else:
            category = "Failed"

        info["performance"][subject] = category

# Print scores and their performance categories
print("=" * 30, "PERFORMANCE CLASSIFICATION", "=" * 30)

for student, info in organized_student_data.items():
    print(f"Student Name: {student}")

    for subject, score in info["scores"].items():
        category = info["performance"][subject]
        print(f"  {subject.capitalize()}: {score} - {category}")

    print(f"  Status: {info['status']}")
    print("-" * 30)


# Determine performance summaries
subject_totals = defaultdict(list)

print("=" * 30, "STUDENT PERFORMANCE SUMMARIES", "=" * 30)

for student, info in organized_student_data.items():
    scores = info["scores"]

    valid_scores = [
        score for score in scores.values()
        if isinstance(score, (int, float))
    ]

    print(f"\nStudent: {student}")

    if valid_scores:
        average = sum(valid_scores) / len(valid_scores)
        highest = max(valid_scores)
        lowest = min(valid_scores)

        print(f"  Average Score: {average:.2f}")
        print(f"  Highest Score: {highest}")
        print(f"  Lowest Score: {lowest}")
        print(f"  Subjects with Scores: {len(valid_scores)}")

    for subject, score in scores.items():
        if isinstance(score, (int, float)):
            subject_totals[subject].append(score)

    if info["performance"]:
        passed = sum(
            1 for category in info["performance"].values()
            if category in ("Excellent", "Good", "Passed")
        )
        failed = sum(
            1 for category in info["performance"].values()
            if category == "Failed"
        )
        incomplete = sum(
            1 for category in info["performance"].values()
            if category == "Incomplete"
        )

        print(f"  Passed Subjects: {passed}")
        print(f"  Failed Subjects: {failed}")
        print(f"  Incomplete Subjects: {incomplete}")

print("\n" + "=" * 30, "SUBJECT PERFORMANCE SUMMARIES", "=" * 30)

for subject, scores in subject_totals.items():
    average = sum(scores) / len(scores)

    print(f"\nSubject: {subject.capitalize()}")
    print(f"  Average Score: {average:.2f}")
    print(f"  Highest Score: {max(scores)}")
    print(f"  Lowest Score: {min(scores)}")
    print(f"  Number of Recorded Scores: {len(scores)}")
