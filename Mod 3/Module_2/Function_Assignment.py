# Write a program to sort by ascending order from the following list.
# (Create a function to solve it)

my_list = [1, 5, 2, 9, 3, 22, 13, ]


def sort_list(my_list):
    n = len(my_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

sort_list(my_list)

print("Sorted List: ", my_list)
# for i in range(len(my_list)):
#     print(my_list[i], end=" ")
