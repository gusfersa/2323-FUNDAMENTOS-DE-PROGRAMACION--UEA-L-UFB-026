#Creación de arreglo tridimensional

#¿Cuál es la forma correcta de crear un arreglo tridimensional de tamaño 2x3x4 en Python, inicializado con unos?

#a. arr = [[[1 for _ in range(4)] for _ in range(3)] for _ in range(2)]
#b. arr = [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]]]
#c. arr = [[[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]]]
#d. arr = [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]] (Correcta)

import random

arr = [[[1 for _ in range(4)] for _ in range(3)] for _ in range(2)]

print(arr)

arr = \
    [
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ],
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
    ]

print(arr)

arr = [[[random.randint(1, 99) for _ in range(4)] for _ in range(3)] for _ in range(2)]

print(arr)
