# update the specific value of a list - program (array)

bazar_list = [
    'chini',
    'lobon',
    'morich',
    25,
    3.14156,
    True,
]

# update the first value of the list 
bazar_list[0] = "ada"
print(bazar_list)

bazar_list[3] = bazar_list[3] + 5
print(bazar_list)

bazar_list[2] = "lobongo"
print(bazar_list)


new_bazar_list = list((
    "item1",
    "item2",
    "item3"
))

print(new_bazar_list)
print(type(new_bazar_list))
print("hello")