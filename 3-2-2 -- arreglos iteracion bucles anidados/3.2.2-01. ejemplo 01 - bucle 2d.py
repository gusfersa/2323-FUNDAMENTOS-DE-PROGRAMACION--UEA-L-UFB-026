# Ejemplo de exploración de una matriz 2D (matriz bidimensional)
matrix_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Exploración de una matriz 2D:")
for row in matrix_2d:
    for element in row:
        print(element, end=' ')
    print()