# ##### LISTS & TUPLES ###########
# from list_practice import union_set, intersection_set, difference_set
#
# # List Reversal: Reverse a list without using the built-in reverse() method.
# my_list = [1, 2, 3, 4, 5, ]
#
# left = 0
# right = len(my_list)-1
#
# while left < right:
#     my_list[left], my_list[right] = my_list[right], my_list[left]
#     left += 1
#     right -= 1
# print(my_list)
#
# # List Comprehension: Write a list comprehension to create a list of squares of even numbers from 1 to 20.
# squares_of_even_numbers = [num**2 for num in range(1, 21) if num %2 == 0]
# print(squares_of_even_numbers)
#
# # Tuple Unpacking: Unpack a tuple into multiple variables and print their values.
# my_tuple = (1, 2, 3, 4, )
#
# a, b, c, d = my_tuple
# print(a, b, c, d)
#
# # List Slicing: Create a new list from an existing list, starting from the third element and ending before the last two elements.
# my_list = [1, 2, 3, 4, 5, 6, 7, ]
#
# new_list = my_list[2:len(my_list)-2]
# print(new_list)
#
# # Tuple Swapping: Swap the values of two elements in a tuple without using a temporary variable.
# my_tuple = (1, 2, )
# my_tuple = (my_tuple[1], my_tuple[0])
# print(my_tuple)
#
# ##### SETS ##########
#
# # Set Operations: Given two sets, find their union, intersection, and difference.
# set1 = {1, 2, 3, 4, }
# set2 = {3, 4, 5, 6, }
#
# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# difference_set = set1.difference(set2)
#
# print(union_set, intersection_set, difference_set)
#
# # Symmetric Difference: Find the symmetric difference between two sets (elements present in one set or the other, but not both).
# symmetric_difference_set = set1.symmetric_difference(set2)
# print("symmetric difference: ", symmetric_difference_set)
#
# # Subset Check: Determine if one set is a subset of another.
# is_subset = set1.issubset(set2)
#
# if is_subset:
#     print("Set1 is a subset of set2")
# else:
#     print("Set1 is not a subset of Set2")
#
# # Set Comprehension: Create a set of prime numbers using a set comprehension.
# prime_numbers = {num for num in range(2, 101) if all(num %i != 0 for i in range(2, int(num**0.5)+1))}
# print(prime_numbers)
#
# ###### DICTIONARIES #############
#
# # Dictionary Sorting: Sort a dictionary by its keys or values.
# my_dict = {'c': 3, 'a': 1, 'b': 2}
# sorted_dict_by_keys = sorted(my_dict.items())
# print(sorted_dict_by_keys)
#
# # Dictionary Comprehension: Create a dictionary where the keys are words and the values are their lengths.
# words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'mango', ]
# word_lengths = {word: len(word) for word in words}
# print(word_lengths)
#
# # Dictionary Merging: Merge two dictionaries, giving priority to values from the second dictionary if there are duplicate keys.
# dict1 = {'a': 1, 'b': 2, }
# dict2 = {'b': 3, 'c': 4, }
#
# merged_dict = dict1.copy()
# merged_dict.update(dict2)
# print(merged_dict)
#
# # Inverting a Dictionary: Create a new dictionary where the keys and values are swapped.
# inverted_dict = {value: key for key, value in my_dict.items()}
# print(inverted_dict)
#
# #### ADVANCE TOPIC #########
#
# # Lambda Functions: Use lambda functions to create anonymous functions and pass them to other functions.
# my_list = [3, 1, 4, 1, 5, 9, ]
# sorted_list = sorted(my_list, key=lambda x: x % 2)
# print(sorted_list)
#
# # Decorators: Write a decorator to time the execution of a function.
# import time
#
# def my_function():
#     time.sleep(2)
# start_time = time.time()
# my_function()
# end_time = time.time()
# excution_time = end_time - start_time
# print(f"Execution Time: {excution_time: .5f}seconds")
#
# # Generators: Create a generator function to produce Fibonacci numbers.
# a, b = 0, 1
# for i in range(10):
#     print(a)
#     a, b = b, a + b
#
# # Context Managers: Implement a custom context manager to handle resource management (e.g., file I/O).
# filename = 'my_file.txt'
# mode = 'w'
# file = open(filename, mode)
#
# try:
#     file.write("Hello, world!")
# finally:
#     file.close()
from idlelib.debugger_r import restart_subprocess_debugger

from list_practice import even_numbers

############
# class FileHandler:
#   """Custom context manager for handling file I/O."""
#
#   def __init__(self, filename, mode="r"):
#     self.filename = filename
#     self.mode = mode
#
#   def __enter__(self):
#     self.file = open(self.filename, self.mode)
#     return self.file
#
#   def __exit__(self, exc_type, exc_val, exc_tb):
#     self.file.close()
#
# # Example usage:
# with FileHandler("my_file.txt", "w") as file:
#   file.write("Hello, world!")

######### List Manipulation ########

# List Rotation: Rotate a list to the left or right by a given number of positions.
my_list = [1, 2, 3, 4, 5, ]
k = 2
n = len(my_list)
k %= n
rotated_list = my_list[k:] + my_list[:k]
print(rotated_list)

# List Partitioning: Partition a list around a pivot element, such that all elements smaller than the pivot are to its left and all elements greater than or equal to the pivot are to its right.
my_list1 = [10, 2, 7, 8, 9, 1, 5, ]
pivot = my_list1[-1]
i = -1
for j in range(len(my_list1) - 1):
    if my_list1[j] < pivot:
        i += 1
        my_list1[i], my_list1[j] = my_list1[j], my_list1[i]
my_list1[i + 1], my_list1[-1] = my_list1[-1], my_list1[i + 1]
print(my_list1)

# List Flatten: Flatten a nested list into a single-level list.
nested_list = [[1, 2,], [3, 4,], [5, [6, 7, ]]]
flattened_list = []

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            flattened_list.append(item)
flatten(nested_list)
print(flattened_list)

#######  DICTIONARIES ############

# Dictionary Grouping: Group elements in a list based on a key function.
my_dict = [
    {'name': 'Amit', 'age': 26 },
    {'name': 'Rimon', 'age': 28 },
    {'name': 'Dipta', 'age': 24 },
    {'name': 'Nahid', 'age': 24 },
]
group_by_age = {}

for item in my_dict:
    key = item['age']
    if key not in group_by_age:
        group_by_age[key] = []
        group_by_age[key].append(item)
print(group_by_age)

# Dictionary Inversion: Safely invert a dictionary, handling duplicate values.
my_dict1 = {'a': 1, 'b': 2, 'c': 1, }
inverted_dict = { }

for key, value in my_dict1.items():
    if value not in inverted_dict:
        inverted_dict[value] = key
    else:
        if not isinstance(inverted_dict[value], list):
            inverted_dict[value] = [inverted_dict[value]]
        inverted_dict[value].append(key)
print(inverted_dict)

# Dictionary Filtering: Filter a dictionary based on a condition.
my_dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }

filtered_dict3 = {key: value for key, value in my_dict2.items() if key.startswith('a')}
print(filtered_dict3)

filtered_dict4 = {key: value for key, value in my_dict2.items() if value > 2 }
print(filtered_dict4)

########## SETS #############

# power set: Generate the power set of a given set(all possible subsets)
my_set = {1, 2, 3, }
power_set = [[]]

for item in my_set:
    for subset in power_set.copy():
        power_set.append(subset + [item])
print(power_set)

# Cartesian Product: Find the Cartesian product of two sets.
set1 = {1, 2, 3, }
set2 = {4, 5, }
cartesian_product = []

for item1  in set1:
    for item2 in set2:
        cartesian_product.append((item1, item2))
print(cartesian_product)

########### ADVANCE TOPICS ###########

# Regular Expressions: Use regular expressions to match and extract patterns from text.
import re

text = "The quick brown fox jumps over the lazy dog."
# Find all words that start with "t"
matches = re.findall(r"\bj\w+", text )
print(matches)

# Extract email addresses
text1 = "my email is rafiuzzaman0028@gmail.com. you can contact using that"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_matches = re.findall(email_pattern, text1)
print(email_matches)

# Object-Oriented Programming (OOP): Create classes and objects to model real-world entities and their relationships.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} barks!")

# Create objects (instances) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

# Access attributes and call methods directly
print(dog1.name)
dog2.bark()

# Functional Programming: Explore functional programming concepts like higher-order functions, lambda functions, and recursion.
## Recursion
# n = int(input("Enter your Number: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(f"The factorial of {n} is {factorial}")

## Higher-Order Functions
numbers = [1, 2, 3, 4, 5, ]
squared_numbers = list(map(lambda x: x ** 2, numbers))
cube_numbers = list(map(lambda x: x ** 3, numbers))
print(squared_numbers, cube_numbers)

# Combining Concept
even_numbers = []
for num in numbers:
    if num %2 == 0:
        even_numbers.append(num)
squared_even_numbers = [num ** 2 for num in even_numbers]
print(squared_even_numbers)

