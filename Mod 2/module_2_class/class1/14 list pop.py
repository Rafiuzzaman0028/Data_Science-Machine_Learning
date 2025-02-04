# pop function will remove the given index number of item from the list
# if no index is given, it will remove the last item from the list
# it takes one argument, index number

# remove item from the list using pop() function
bazar_list = [
    'lebu',
    'ada', 
    'daruchini'
]

print('bazar_list: ', bazar_list)

item_remove = bazar_list.pop(1)

print('after removing the last item: ', bazar_list)
print('removed item from list: ', item_remove)

