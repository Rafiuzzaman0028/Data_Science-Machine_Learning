my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print('my_matrix: ', my_matrix)

# Print the matrix
for row in my_matrix:
    print('row: ', row)

new_matrix = [
    [[1, 2], 3],
    [[4, 5, 6], 7],
    [[8, 9], 10]
]

print('new_matrix: ', new_matrix)

# Print the matrix
for row in new_matrix:
    print('row: ', row)

print('new_matrix: ', new_matrix[0])
print('new_matrix: ', new_matrix[0][0])
print('new_matrix: ', new_matrix[0][0][1])