# sort function will sort the list in ascending order

# sort bazar_list in ascending order
bazar_list = list((
    "chini", "lobon", "ada"
))

print('bazar_list: ', bazar_list)

bazar_list.sort()
print("bazar_list after using sort function: ", bazar_list)

# sort bazar_list in descending order
bazar_list.sort(reverse=True)
print("bazar_list after using sort function with reverse=True: ", bazar_list)

# reverse function will reverse the list
bazar_list.reverse()
print("bazar_list after using reverse function: ", bazar_list)