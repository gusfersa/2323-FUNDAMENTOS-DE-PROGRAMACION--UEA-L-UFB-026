# Ejemplo de exploración de una matriz 3D (matriz tridimensional)
matrix_3d = [
    [
        [11, 12, 13],
        [14, 15, 16]
    ],
    [
        [21, 22, 23],
        [24, 25, 26]
    ]
]

print("\nExploración de una matriz 3D:")
for layer in matrix_3d:
    for row in layer:
        for element in row:
            print(element, end=' ')
        print()