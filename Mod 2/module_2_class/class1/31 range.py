
"""
range function rules:

1. range(stop) - generates a sequence of numbers from 0 up to (but not including) stop
2. range(start, stop) - generates a sequence of numbers from start up to (but not including) stop
3. range(start, stop, step) - generates a sequence of numbers from start up to (but not including) stop, incrementing by step

"""

print(range(5)) # range(0, 5)
for i in range(5):
    # print("i: ", i)  
    print(i) # 0, 1, 2, 3, 4

print(list(range(5)))

range_values = range(0, 5)
print("range_values: ", list(range_values)) # range_values:  [0, 1, 2, 3, 4]

range_values = range(2)
print("range_values: ", list(range_values)) # range_values:  [0, 1]

range_values = range(1, 10, 2)
print("range_values: ", list(range_values)) # range_values:  [1, 3, 5, 7, 9]

range_values = range(10, 1, -2)
print("range_values: ", list(range_values))

for i in range(5):
    print("Number is: ", i)

for i in range(1, 5):
    print("Number is: ", i)

for i in range(1, 10, 2):
    print("Number is: ", i)

for i in range(10, 1, -2):
    print("Number is: ", i)

for i in range(10, 1, 2):
    print("Number is: ", i)




# using range function
print("\nUsing range function:")
total = 0
for i in range(1, 10, 3):
    print("The number is: ", i)
    total+=i

print("The total number is: ", total)

print("Done")