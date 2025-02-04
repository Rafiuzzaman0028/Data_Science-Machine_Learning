student = {
    "name": "MD Rimon",
    "age": 25,
    "subject": "CSE"
}

print(student)
print("student's name: ", student["name"])
print("student's age: ", student["age"])
print("student's subject: ", student["subject"])

student["age"] = 26
print("student's age: ", student["age"])

print("student's items: ", student.items())

# print(student["is_valid"]) # KeyError: 'is_valid'

print(student.get("is_valid")) # None
print(student.get("is_valid", False)) # False
print(student.get("is_valid", True)) # True

# Check if the key "is_valid" exists in the dictionary
if "is_valid" in student:
    # If the key exists, print its value
    print(student["is_valid"])
else:
    # If the key doesn't exist, print False
    print(False)

# check the type of dictionary
print(type(student)) # <class 'dict'>

print(student.keys()) # dict_keys(['name', 'age', 'subject'])
print(student.values()) # dict_values(['MD Rimon', 26, 'CSE'])

# check the length of dictionary
print(len(student)) # 3

# remove the given key from the dictionary
print(student.pop("name")) # MD Rimon
print(student) # {'age': 26, 'subject': 'CSE'}

# delete the given key from the dictionary
del student["age"]
print(student) # {'subject': 'CSE'}

# remove the last item from the dictionary
print(student.popitem()) # ('subject', 'CSE')
print(student) # {}

# remove all the items from the dictionary
student.clear()
print(student) # {}


# new dictionary
student = dict(name="MD Rimon", age=25, subject="CSE")
print(student)
print(type(student))
print(len(student.items()))

# convert the dictionary into list
print(list(student.items())) # [('name', 'MD Rimon'), ('age', 25), ('subject', 'CSE')]

# convert the dictionary into tuple
print(tuple(student.items())) # (('name', 'MD Rimon'), ('age', 25), ('subject', 'CSE'))

# convert the dictionary into set
print(set(student.items())) # {('name', 'MD Rimon'), ('subject', 'CSE'), ('age', 25))


