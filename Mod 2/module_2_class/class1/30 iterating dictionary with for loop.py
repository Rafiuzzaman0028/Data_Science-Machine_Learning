student = dict(
    name="MD Rimon",
    subject="CSE",
    year=2025
)

print('student: ', student)

# Iterate through the dictionary and print keys
for item in student:
    print('item: ', item)

# Iterate through the dictionary and print values
for item in student:
    print('item: ', student[item])

# Iterate through the dictionary and print keys and values
for item in student:
    print('item: ', item, student[item])

# Iterate through the dictionary and print keys and values
for key, value in student.items():
    print('key: ', key, 'value: ', value)

for item in student.items():
    print("item: ", item) 

for item in student.keys():
    print("keys: ", item) 

for item in student.values():
    print("values: ", item)

# check the type of the student item
for item in student.items():
    print("type of item: ", type(item)) 
    """
    # output
    type of item:  <class 'tuple'>
    type of item:  <class 'tuple'>
    type of item:  <class 'tuple'>
    """


bazar_list = {
    "first": "rice",
    "second": "chicken",
    "third": "fish"
}

print("bazar_list: ", bazar_list)

# bazar_list = ("rice", "chicken", "fish")
# first_item, second_item = bazar_list

for keys, values in bazar_list.items():
    print("Keys: ", keys, "Values: ", values)


student = dict(
    name="MD Rimon",
    subject="CSE",
    year=2025
)

for keys, values in student.items():
    print("Keys: ", keys, "Values: ", values)

