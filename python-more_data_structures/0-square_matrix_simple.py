#!/usr/bin/pythonk3
def square_matrix(matrix):
    result_matrix = []

    for row in matrix:
        squared_row = [num ** 2 for num in row]
        result_matrix.append(squared_row)

    return result_matrix

result = square_matrix(input_matrix)
print(result)
