# dictionary
student = dict(
    name="MD Rimon",
    subject="CSE",
    year=2024,
    is_valid=True
) 

print('student: ', student)
print('name: ', student["name"])

# dictionary
new_student = {
    "subject": "Data Science",
    "year": 2025,
    "platform": "Frontend Developer",
}

# update the dictionary
student.update(new_student)
print("Update the dictionary: ", student)

