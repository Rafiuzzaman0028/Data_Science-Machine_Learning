bazar_list = [
    'chini', 
    'lobon', 
    'morich',
    'ada'
]

first_item, *rest_of_the_item = bazar_list
# first_item, second_item, *rest_of_the_item = bazar_list

print(first_item)
print(type(first_item))
print(rest_of_the_item)
print(type(rest_of_the_item))

player_names = list((
    "rahim", "karim", "saddam", "rimon", "amil", "joy"
))

print('player_names:', player_names)
print("type:", type(player_names))

first_player, secondPlayer, *restOfThePlayer = player_names

print(first_player)
print(secondPlayer)

print('restOfThePlayer: ', restOfThePlayer)
print('type of restOfThePlayer: ', type(restOfThePlayer         ))