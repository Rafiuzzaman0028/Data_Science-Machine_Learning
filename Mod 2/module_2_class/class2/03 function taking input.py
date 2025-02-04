# function to add two numbers
print("Program for adding(sum) of two numbers")
def Add(x, y):
    """
    This function takes two numbers as input and prints their sum.
    """
    print(x + y)

# take input from the user
a = input("Enter first number: ")
b = input("Enter second number: ")

# convert the input strings to integers
a = int(a)
b = int(b)

# call the function to add the two numbers
Add(a, b)



# another program
# function to multiply two numbers

print("Program for multiplying(result) of two numbers")

def multiply(x, y):
    """
    This function takes two numbers as input and prints their product.
    """
    # print(x * y)
    return x * y 
    
# take input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# call the function to multiply the two numbers
result = multiply(a, b)

# show the rsult 
print("Restult: ", result)