"""
Practice Problem-1
-------------------------------
    Shopping List Manager:
-------------------------------
You are asked to create a shopping list manager.
The user can add items to the shopping list. When "done" is typed, the input system closes, and you need to display the list along with the total number of items.
"""

# initializing the shopping_list variable
shopping_list = []

print("If you want to stop this program, type 'done'")

while True:
    # user input
    shopping_item = input("Enter shopping item: ")
    
    # if user typed "done", the system will close the input system
    if shopping_item.lower() == "done":
        if len(shopping_list) == 0:
            # if there is no item in the list, the system will display "No items"
            print("No items in the shopping list.")
            break
        else:
            # Display the shopping list and the total number of items
            print("Shopping List:", shopping_list)
            print("Total items:", len(shopping_list))
            # break the loop
            break
    else:
        # Add the shopping_item to the shopping_list
        shopping_list.append(shopping_item)

print("Happy Shopping.")