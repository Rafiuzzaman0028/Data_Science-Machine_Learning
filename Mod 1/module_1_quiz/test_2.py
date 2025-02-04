# Sum all the odd numbers from 0 to 100 and print it to the screen.

# initialize the starting number(i) and the total odd sum(total)
i = 1
total = 0

"""
using while loop to find the 
sum of all odd numbers 
from 0 to 100 and print it
"""
while i <= 100:
	# add the total sum to the total variable
	total = total + i 
	# increament by 2 to get the next odd number
	i = i + 2

# print the total sum of odd numbers from 0 to 100
print(total)