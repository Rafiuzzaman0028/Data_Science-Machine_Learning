# def calculate_grade(score):
#   """Calculates the grade based on the given score.
#
#   Args:
#     score: The student's score.
#
#   Returns:
#     The corresponding grade.
#   """
#
#   if score >= 90:
#     return 'A'
#   elif score >= 80:
#     return 'B'
#   elif score >= 70:
#     return 'C'
#   elif score >= 60:
#     return 'D'
#   elif score >= 50:
#       return 'E'
#   elif score >= 40:
#       return 'E-'
#   else:
#     return 'F'
#
# # Get the user's score
# score = float(input("Enter the student's score: "))
#
# # Calculate and print the grade
# grade = calculate_grade(score)
# print("The student's grade is:", grade)
#



















# Get the user's score
score = float(input("Enter the student's score: "))

# Determine the grade based on the score

if score >= 90:
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
elif score >= 60:
  grade = 'D'
elif score >= 50:
  grade = 'E'
elif score >= 40:
  grade = 'E-'
else:
  grade = 'F'

# Print the calculated grade
print("The student's grade is:", grade)




