"""
Practice Problem
-------------------------------
        Score Tracker
-------------------------------
You are asked to create a Score Tracker. You'll take the name and the score of a student as input. Store those by name and print all the student's names with their scores. The input ends when the student's name is "stop."
"""


# initializing the students_score dictionary
score_tracker = {}

print("If you want to stop this program, type 'stop'")

while True:
    # taking the student's name and score as input
    students_name = input("Enter student's name: ")
    # if the student's name is "stop", the system will close the input system
    if students_name.lower() == "stop":
        break
    # taking the student's score as input
    students_score = int(input("Enter students score: "))

    # showing the student's_name and students_score
    print("students_name: ", students_name, "students_score: ", students_score)

    # adding the students_name and students_score in the students_score dictionary
    score_tracker[students_name] = students_score

#  printing the score_tracker dictionary
print("Score of the students: ", score_tracker)

# printing the score_tracker separately
for students_name, students_score in score_tracker.items():
    print(students_name, ":", students_score)