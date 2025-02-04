"""
# python math function
x = 2.9
print(round(2.9))
print(abs(-2.9))

# python math module

import math

print(math.ceil(x))
print(math.floor(x))

#if-elif-else statement practice

i = 10

if i > 15:
    print("10 is less than 15")
print("I am Not in if")

i = 20

if i <15:
    print("I is smaller than 15")
    print("'i' in if Block")
else:
    print("i is greater than 15")
    print("'i' in else Block")
print("This 'i' not in if-else Block")

i = 20

if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")
print("end practice")

# Match Case

#num = int(input())
num = 3
match num:
    #patter 1
    case 1:
        print("One")
    #pattern 2
    case 2:
        print("Two")
    #pattern 3
    case 3:
        print('Three')
    #pattern default
    case _:
        print('Number not between 1 and 3')

# Comparison

a = 9
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(type(a))


#Logical Operators

# AND Practice
a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The number are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print('Atleast one number is not greater than 0')

# OR Practice

a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the numbers is greater than 0")
else:
    print('No number is greater than zero')

# NOT practice

a = 10

if not (a % 3 == 0 or a % 5 == 0):
    print('10 is not divisible by either 3 or 5')
else:
    print('10 is divisible by either 3 or 5')

#Assignment Operator
x = 5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
"""
"""
# Numeric Complex Data Type

a = 6 + 7j
print(a)
print(a.real)
print(a.imag)
print(type(a))

b = 5 + 5j
print(a + b)

#While Loop

count = 0
while count <= 9:
    print('The count is :', count)
    count = count + 1

print('Good Bye!')
"""

"""
# Sum of n Number of Program

#Take input
n = int(input('Enter the n Number :'))

#declare variable
sum = 0
i = 1

# Loop
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
"""

"""
# Break & Continue statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
"""

""""
sum = 0

while True:
    num = int(input("Enter a Number :"))
    if num == "quit":
        break
    try:
        num = int(num)
    except:
        print("Enter a valid number please.")
        continue
    sum = sum + num
    print(sum)
    
"""
"""""
#### FOR LOOPS ######

#Looping Through a string

for x in "banana":
    print(x)

#Looping Through a List
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
"""""

""""
#The break Statement
#Exit the loop when x is 'banana'
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

# The continue Statement
#Do not print banana

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)


# FOR-While comparison
num = [10, 20, 30, 40, 50]
index = 0
n = len(num)
while index < n:
    print(num[index])
    index = index + 1

num = [10, 20, 30, 40, 50]
for x in num:
    print(x)
"""
""""
### FOR with Range Function ###

for x in range(6):
    print(x)
# Using the start parameter
for x in range(2, 6):
    print(x)

#Increament the sequence with 3
for x in range(2, 21, 3):
    print(x)
"""
"""
#FOR with Enumerate

num = [30, 10, 70, 12]
for i, x in enumerate(num):
    print(i, x)

### Nested LOOPS

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)

a = 'hello world'
print(a)
print(a[0])
print(a[-1])
print(a[0:3])
print(a[0:])
print(a[1:])
print(a[:4])
print(a[0:-1])
"""
"""
num_int = 123
num_flo = 1.00

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))
"""

### Explicit type

# num_int = 123
# num_str = '456'
#
# print("Data type of num_int:", type(num_int))
# print("Data type of num_str :", type(num_str))
#
# print(num_int, num_str)
#
# print("Data types of num_int:", type(num_int))
# print("Data type of num_str before Type Casting:", type(num_str))
#
# num_str = int(num_str)
# print("Data type of num_str after type Casting:", type(num_str))
#
# num_sum = num_int + num_str
#
# print("Sum of num_int and num_str :", num_sum)
# print("Data type of the sum :", type(num_sum))
#

import math
x = -4.3

print(math.ceil(x))
print(math.floor(x))

print(abs(x))
print(round(x))