# Definir una matriz 3D con valores numéricos
matriz_3d = [
    [
        [11, 12, 13],
        [14, 15, 16]
    ],
    [
        [21, 22, 23],
        [24, 25, 26]
    ]
]

# Inicializar la variable "maximo" con el valor mínimo posible
maximo = float('-inf')

# Iterar a través de capas, filas y columnas para encontrar el elemento máximo
for capa in matriz_3d:
    for fila in capa:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento

# Mostrar el resultado del elemento máximo
print("El elemento máximo en la matriz 3D es:", maximo)
