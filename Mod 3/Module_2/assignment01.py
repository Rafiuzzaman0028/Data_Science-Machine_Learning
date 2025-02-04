# my_list = [1, 5, 6, 5, 1, 2, 3, ]
# #
# # seen = set()
# duplicates = []
# #
# # for item in my_list:
# #     if item in seen:
# #         duplicates.append(item)
# #     else:
# #         seen.add(item)
# # print(duplicates)
# #
# for item in my_list:
#     if my_list.count(item) > 1 and item not in duplicates:
#         duplicates.append(item)
# print(duplicates)

my_list = [1, 5, 6, 5, 1, 2, 3, ]
duplicates = [ ]
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
	    duplicates.append(item)
print(duplicates)
