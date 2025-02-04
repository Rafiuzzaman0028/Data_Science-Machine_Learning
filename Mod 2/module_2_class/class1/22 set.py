# Rules of Set in Python

# 1. Unordered: Elements in a set do not have a specific order.
# 2. Unique: A set cannot contain duplicate elements.
# 3. Mutable: You can add or remove elements from a set after it's created.
# 4. Heterogeneous: A set can contain elements of different data types (e.g., integers, strings, floats).
# 5. Iterable: You can iterate through the elements of a set using loops.

# example of set
fruits_set = {"apple", "banana", "jackfruit"}
print('set: ', fruits_set)
print('type of set:', type(fruits_set))

# Example: Add elements
fruits_set.add("orange")
print("Set with added orange:", fruits_set)

# Example: Remove elements
fruits_set.remove("banana")
print("Set with removed banana:", fruits_set)


# print a new line
print()

# example of list
fruits_list = ["apple", "banana", "jackfruit"]
print('list: ', fruits_list)
print('type of list:', type(fruits_list))
# print a new line
print()

# example of tuple
fruits_tuple = ("apple", "banana", "jackfruit")
print('tuple: ', fruits_tuple)
print('type of tuple:', type(fruits_tuple))
# print a new line
print()