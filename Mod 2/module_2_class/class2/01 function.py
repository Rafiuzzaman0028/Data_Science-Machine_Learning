# Basic rules for defining functions in Python:

# 1. Use the `def` keyword followed by the function name and parentheses ().
# 2. The function name should follow Python's naming conventions (e.g., lowercase with underscores).
# 3. Function parameters (inputs) are listed within the parentheses.
# 4. A colon (:) indicates the end of the function header.
# 5. The function body is indented (typically 4 spaces).
# 6. Use the `return` keyword to specify the output of the function (optional).
# 7. Comments within functions should explain what the code does.

# Example:

def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")
    return f"Greeting sent to {name}"

# take the name from the user input
name = input("Enter your name:")

# # the first letter of the name should be uppercase
# name = name.capitalize()

# the first letter of each word should be capitalize
name = name.title()

# Calling a function
# greeting = greet("Alice")
greeting = greet(name)
print(greeting)
