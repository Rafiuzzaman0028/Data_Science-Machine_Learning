# calcualte the total odd numbers between 1 to 10
total = 0

for i in range(1, 10):
    if i % 2 != 0:
        print("i: ", i)
        total += i

print("Result: ", total)

# calcualte the total odd numbers between 1 to 10
total = 0

for i in range(1, 10, 2):
    print("i: ", i)
    total += i

print("Result: ", total)

# calculate the total odd numbers 
print("calculate the total odd numbers ")
n = int(input("Enter the value of n:"))
total = 0

for i in range(1, n, 2):
    print("i: ", i)
    total += i

print("Result: ", total)

# calculate the total even numbers 
print("calculate the total even numbers")
n = int(input("Enter the value of n:"))
total = 0

for i in range(2, n+1, 2):
    print("i: ", i)
    total += i

print("Result: ", total)

