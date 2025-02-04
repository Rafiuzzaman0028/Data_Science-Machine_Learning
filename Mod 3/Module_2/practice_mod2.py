# #### Shopping List Manager ######
#
# shopping_list = []
#
# # input in a condition method
# while True:
#     item = input("Enter an item ( or type 'done' to finish): ")
#
#     if item.lower() == 'done':       # as it is case sensitive any case turn into lower
#         break
#     else:
#         shopping_list.append(item)   # adding items from user in variable shopping_list
#
# print("\n your shopping list: ")
# for item in shopping_list:
#     print("-" + item)
#
# print("\nTotal number of items: ", len(shopping_list))

##### Score Tracker ######

scores = {}

while True:
    name = str(input("Enter Name: "))

    if name.lower() == 'stop':
        break

    score = float(input("Enter Score: "))
    scores[name] = score

print("\nStudents Scores: ")
for name, score in scores.items():
    print(f"{name}: {score} ")

