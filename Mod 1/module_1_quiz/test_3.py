"""
Write a Program to take a user score 
and find a student's grade using Python code. 
Following is the grade information.
"""

# taking input from user
number = float(input("Enter the number/marks of the student: "))

if number > 100 or number < 0:
	print("Enter the number/marks between from 0 to 100")
elif number >= 90 and number <= 100:
	print("Your Grade is: A")
elif number >= 80 and number < 90:
	print("Your Grade is B")
elif number >= 70 and number < 80:
	print("Your Grade is C")
elif number >= 60 and number < 70:
	print("Your Grade is D")
elif number >= 50 and number < 60:
	print("Your Grade is E")
elif number >= 40 and number < 50:
	print("Your Grade is E-")
elif number < 40 and number >= 0:
	print("Your Grade is F (Fail). Try hard again. You have to pass.")

print("Thanks for using the program.")