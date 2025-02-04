#
# ### Create a list #####
# my_list = [
#     1,
#     2,
#     3,
#     4,
#     5,
# ]
#
# print(type(my_list))
# print(type(my_list[2]))
# print(my_list[0:-1])
# print(my_list[:: -1])
#
#
# ##### Access Elements ######
# first = my_list[0]
# last = my_list[-1]
# print(first, last)
#
# ##### Slicing #####
#
# sublist = my_list[1:4]
# print(sublist)
#
# ######## Changing elements ########
#
# my_list[2] = 10
# print(my_list)
#
# ##### List Concatenation ######
#
# list1 = [1, 2]
# list2 = [3, 4]
# combine_list = list1 + list2
# print(combine_list)
#
# #### List repetition ######
#
# repeated_list = [1] * 3
# print(repeated_list)
# repeated_list1 = my_list * 3
# print(repeated_list1)
#
# ###### List methods ##########
#
# list1.append(3)
# print(list1)
#
# list2.insert(0, 5)
# print(list2)
#
# list2.remove(3)
# print(list2)
#
# list1.pop(1)
# print(list1)
#
# list2.pop()
# print(list2)
#
# list2.index(5)
# print(list2)
#
# my_list.index(1)
# print(my_list)
#
# my_list.count(5)
# print(my_list)
#
# my_list.sort()
# print(my_list)
#
# my_list.reverse()
# print(my_list)
#
# ##### List Comprehensions ###########
#
# ##### Creating lists ########
#
# squares = [x ** 2 for x in range(5)]
# print(squares)
#
# ##### Filtering Lists #########
#
# even_num = [x for x in range(10) if x % 2 == 0]
# print(even_num)
#
# ##### Conditional Expressions ##########
#
# positive_num = [x if x > 0 else 0 for x in [-1, 2, -3, 4]]
# print(positive_num)
#
#
#
# ######  Write a function to find the maximum element in a list #####
#
# num_input = input("Enter numbers separated by spaces: ")
#
# num = [int(num) for num in num_input.split()]
#
# if not num:
#     print("The List is empty.")
# else:
#     maximum = num[0]
#     for n in num:
#         if n > maximum:
#             maximum = n
#     print(f"The maximum element is: {maximum}")
#
from itertools import count
from math import frexp
from multiprocessing.managers import ProcessLocalSet
from traceback import print_tb

#
# this_list = ['apple', 'banana', 'cherry', 'apple', 'cherry']
# print(this_list)
#
# list1 = ['apple', 'banana', 'cherry']
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# list4 = ['abc', '34', True, 40, "male"]
# string1 = ["apple"]
#
# print(list3, list4[2])
# print(list1[0])
# print(string1[0])
#
# list1 = ['apple', 'banana', 'cherry', 'mango', 'guava',]
#
# print(list1[0:2])
# print(list1[2:])
# print(list1[-1])
# print(list1[-3:-1])
# print(list1[0:5])
# print(list1[0:5:2])
# print(list1[-1:-2])
# print(list1[-1:-2:-1])
#
#
# list1 = ['apple', 'banana', 'cherry', 'mango', 'orange',]
#
# list1[0] = 'grape'
# print(list1)
# print(list1 + ['tomato', 50,])
# print(list1 * 3)
# print(list1)
# ########  LIST Methods ############
# list1.append('lichi')
# print(list1)
#
# list2 = ['apple', 'banana', 'cherry', 'mango', 'orange',]
# print(list2)
# # list2.clear('mango')
# # print(list2)
#
# x = list2.count('apple')
# print(x)
#
# list2.extend(list1)
# print(list2)
#
# x = list1.index('lichi')
# print(x)
#
# list2.insert(5, 'papaya')
# print(list2)
#
# list2.pop(2)
# print(list2)
#
# list1.remove('cherry')
# print(list1)
#
# list2.reverse()
# print(list2)
#
# list2.sort()
# print(list2)
#
# list2.sort(reverse = False)
# print(list2)


####### 2D Lists/Matrix #########

# A = [
#     [1, 4, 5, 12],
#     [-5, 8, 9, 0],
#     [-6, 7, 11, 19],
# ]
#
# print("A= ", A)
# print("A[1] = ", A[1])
# print("A[1][2]  = ", A[1][2])
# print("A[0][-1] = ", A[0][-1])
#
# column = []
# for row in A:
#     column.append(row[2])
# print("3rd column= ", column)
#
# print(type(column))
# ##### tuples ##########
#
# thistuple = (
#     'apple',
#     'banana',
#     'cherry',
# )
# print(thistuple)
# print(type(thistuple))
#
# ##### Unpacking / Comparing ##########
#
# list2 = ('apple', 'banana', 'cherry', 'mango', 'orange',)
#
# (green, yellow, red, black, white) = list2
# print(green)
# print(yellow)
# print(red)
# print(black)
# print(white)
#
#
# list1 = ('apple', 'banana', 'cherry', 'mango', 'orange',)
#
# (green, yellow, * red) = list1
# print(green)
# print(yellow)
# print(red)
#
# a = (5, 6)
# b = (1, 4)
#
# if a > b:
#     print("a is bigger")
# else:
#     print("b is bigger")
#
# ########## Set (Union/Intersection/Difference) ##########
#
# # Different types of sets in python
# # set of integers
#
# my_set = {1, 2, 3, }
# print(my_set)
# print(type(my_set))
#
# # set of mixed datatypes
# my_set1 = {1.0, 'hello', (1, 2, 3,)}
# print(my_set1)
# print(type(my_set1))
#
# # set cannot have duplicates
#
# my_set2 = {1, 2, 3, 4, 3, 2, }
# print(my_set2)
#
# # we can make set from a list
# my_set3 = set([1, 2, 3, 2])
# print(my_set3)
# print(type(my_set3))
#
# # sorting
# aa = {100, 300, 200, 700, 400, 300}
# print(sorted(aa))
#
# # union/ intersection/ difference
#
# num1 = {1, 2, 3, 4, 5, }
# num2 = {4, 5, 6, 7, }
#
# print(num1 | num2)  # union
# print(num1 & num2)  # intersection
# print(num1 - num2)  # difference
#
#
# ####### Dictionaries #######
#
# thisdict = {
#     'brand' : 'Toyota',
#     'model' : 'premio',
#     'year' : 2007,
# }
# print(thisdict)
# print(thisdict['brand'])
# print(thisdict.get('name', 'invalid key'))
# print(thisdict.get('tyre', '20/30'))
#
# thisdict1 = {
#     'Brand' : 'Ford',
#     'model' : 'Mustang',
#     'electric' : 'False',
#     'year' : 1964,
#     'color' : ['red', 'white', 'blue'],
# }
#
# print(thisdict1.items())
# print(thisdict1.keys())
# print(thisdict1.values())
#
# thisdict2 = {
#     'brand' : 'Toyota',
#     'model' : 'premio',
#     'year' : 2007,
#     'year' : 2008,
# }
# print(thisdict2)
#
# # for x, y in thisdict2.items():
# #     print(x, y)
#
# for a, b in thisdict1.items():
#     print(a, b)
#
# ###########
#
# text = ('The banana is common fruit of Bangladesh. It is grown in all the districts and all the seasons. Munsigonj and Narsingdi are famous for banana. Banana has several varieties such as Sagore, Sabri, Chapa, Agniswar etc. It is very nutritious and sweet. The Papaw is grown in all the districts and in all seasons. The coconut is a common fruit of Bangladesh. It grows in all seasons. Its water is a sweet drink and its kernel is a tasty food. The mango , the orange , the lichi , the black-berry , the jack fruits, the pineapple etc. grow in different seasons.  ')
#
# fruits = ['banana', 'Banana' ,'Papaw', "coconut", "black-berry", "pineapple", "lichi", "orange", "mango"]
# text = text.split(" ")
# fruitlist = []
# for x in text:
#     if x in fruits:
#         fruitlist.append(x)
# print(fruitlist)
#
# ### SET
# fruitlist = set({})
#
# for x in text:
#     if x in fruits:
#         fruitlist.add(x)
# print(fruitlist)
#
# #
#
# fruitlist = {}
# for x in text:
#     if x in fruits:
#         fruitlist[x] = 1
# print(fruitlist)
#
# fruitlist = {}
# for x in text:
#     if x in fruits:
#         if x not in fruitlist.keys():
#             fruitlist[x] = 1
#         else:
#             fruitlist[x] += 1
# print(fruitlist)

### Access the first and last elements of the list using python ###

favorite_fruits = ["apples", "bananas", "strawberries", "mangoes", "grapes", "watermelons", "oranges", "cherries"]

# Access the first element
first_fruit = favorite_fruits[0]
print(first_fruit)  # Output: apples

# Access the last element
last_fruit = favorite_fruits[-1]
print(last_fruit)  # Output: cherries

# Slicing the list to extract elements from index 3 to 6
sliced_fruits = favorite_fruits[3:-2]
print(sliced_fruits)

# Add a new fruits to the end of the list
favorite_fruits.append("Kiwi")

print(favorite_fruits)

# Insert a fruits at index 4
favorite_fruits.insert(4, 'pineapple')

print(favorite_fruits)

# Remove the fruits 'pineapple' from the list
favorite_fruits.remove('pineapple')
print(favorite_fruits)

# Remove the fruits at index 8
favorite_fruits.pop(8)
print(favorite_fruits)

# Sort the list in ascending order
favorite_fruits.sort()
print(favorite_fruits)

# Reverse the order of the elements in the list
favorite_fruits.reverse()
print(favorite_fruits)

# Find the length of the list
length = len(favorite_fruits)
print(length)

### Check if 'pineapple' is present in the list
is_pineapple_present = 'pineapple' in favorite_fruits

if is_pineapple_present:
    print("pineapple is present in the list.")
else:
    print("pineapple is not present in the list.")

### Create a new list containing the squares of the number's

numbers = [1, 2, 3 ,4 ,5, ]
squares = [num**2 for num in numbers]
print(squares)

## Merge two list into a single list.
list1 = [1, 2 ,3, ]
list2 = [4, 5, 6, ]

merged_list = list1 + list2
print(merged_list)

## count the occurrences of a specific element in the list.
numbers = [1, 2, 3, 2, 4, 2, 5, ]

count = numbers.count(2)
print(count)

## Create a list comprehension to generate a list of even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]

even_numbers = [num for num in numbers if num %2 == 0 ]

print(even_numbers)


####    TUPLES ##########

# Create a tuples of your favorite colors and print it.
favorite_colors = ('blue', 'green', 'purple',)
print(favorite_colors)

## Access the first and last elements of the tuple.

# Access the first element
first_color = favorite_colors[0]
print(first_color)

# Access the last element
last_color = favorite_colors[-1]
print(last_color)

## Slice the tuple to extract a specific range of elements.

favorite_colors = ("blue", "green", "purple", "yellow", "orange")

# Slice the tuple to extract elements from index 2 to 4 (exclusive)
sliced_colors = favorite_colors[2:-1]
print(sliced_colors)
print(favorite_colors)

# Try to modify an element of the tuple(should raise an error)
#favorite_colors[1] = 'red'
## TUPLES are IMMUTABLE ##

# Creating a new tuple by concatenating two existing tuples.

tuple1 = (1, 2, 3, )
tuple2 = (4, 5, 6, )

concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

# Finding the length of the tuple
length_of_tuple = len(favorite_colors)
print(length_of_tuple)

# Check if a specific color is present in the tuple.

is_red_present = 'red' in favorite_colors

if is_red_present:
    print("'RED' is present in the tuple.")
else:
    print("'RED' is not present in the tuple. ")

# Creating a tuple comprehension to generate a tuple of squares of numbers.

numbers = (1, 2, 3, 4, 5, )

squares = tuple(num**2 for num in numbers)
print(squares)

############    SETS    ##########

#Create a set of unique vowels and print it
vowels = {"a", "e", "i", "o", "u"}

print(vowels)

# Add a new vowel to the set
vowels.add('y')
print(vowels)

# Remove a vowel from the set.
vowels.remove('y')
print(vowels)

# Check if a specific vowel is present in the set.
is_x_present = 'x' in vowels
if is_x_present:
    print("'X' is present in the set. ")
else:
    print("'X' is not present in the set.")

# Find the union of two sets.
set1 = {1, 2, 3, }
set2 = {3, 4, 5, }

union_set = set1.union(set2)
print(union_set)

# Find the intersection of two sets.
intersection_set = set1.intersection(set2)
print(intersection_set)

# Find the difference between two sets.
difference_set = set1.difference(set2)
print(difference_set)

# set2 and set1
difference_set = set2.difference(set1)
print(difference_set)

# Check if one set is a subset of another
set1 = {1, 2, 3, }
set2 = {1, 2, 3, 4, 5, }

is_subset = set1.issubset(set2)

if is_subset:
    print("SET1 is a subset of SET2")
else:
    print("Set1 is not a subset of Set2")

#  Create a set comprehension to generate a set of even numbers
even_numbers = {num for num in range(1, 11) if num %2 == 0}
print(even_numbers)

####### DICTIONARIES ############

# Create a dictionary containing the names of your friends and their ages.
friends = {
    'Amit'  : 26,
    'Rimon' : 29,
    'Nahid' : 25,
    'Dipta' : 24,
}
print(friends)

# Access the age of a specific friend.
amit_age = friends['Amit']
print(amit_age)

# Add a new friend and their age to the dictionary.
friends['Rafe'] = 27
print(friends)

# Update the age of an existing friend.
friends['Rimon'] = 30
print(friends)

# Remove a friend from the dictionary.
remove_age = friends.pop('Rafe')
print(friends)

# Check if a specific friend is present in the dictionary.
is_rafe_present = 'Rafe' in friends

if is_rafe_present:
    print("'Rafe' is present in friends.")
else:
    print("'Rafe' is not present in friends.")

# Get a list of all keys (friend names) in the dictionary.
friend_names = friends.keys()
print(friend_names)

# Get a list of all values (ages) in the dictionary.
friend_ages = friends.values()
print(friend_ages)

# Create a dictionary comprehension to generate a dictionary of squares of numbers as keys and their cubes as values.
numbers = [1, 2, 3, 4, 5, ]

squares_to_cubes = {num**2: num**3 for num in numbers}
print(squares_to_cubes)