"""
Write a program to make another list of duplicate elements from the following list
[1, 5, 6, 5, 1, 2, 3]
"""

# initializing the given_list variable
given_list = [1, 5, 6, 5, 1, 2, 3]
# initialize the duplicate_list variable
duplicate_list = []

# showing the given list  
print("\nGiven List = [1, 5, 6, 5, 1, 2, 3]\n")

# loop through the given list
for i in given_list:
    print("from the given_list, the number ", i, " is found ", given_list.count(i), "x times.")
    # check if the count of the element is greater than 1
    if given_list.count(i) > 1:
        # check if the element is already in the duplicate list or not
        if i not in duplicate_list:
        # append the element to the duplicate list
            duplicate_list.append(i)

# print a new line 
print("\n")

# show the duplicate list
print("The Duplicate list is: ", duplicate_list)

# print a new line 
print("\nThank you.\n")