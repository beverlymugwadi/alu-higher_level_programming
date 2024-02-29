#!/usr/bin/pythonk3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = [row[i]**2 for row in matrix for i in range(3)]
print(result)
