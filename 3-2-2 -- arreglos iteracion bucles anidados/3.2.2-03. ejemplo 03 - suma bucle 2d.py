# Definir una matriz 2D con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicializar la variable de suma
suma = 0

# Iterar a través de filas y columnas para sumar elementos
for fila in matriz:
    for elemento in fila:
        suma += elemento

# Mostrar el resultado de la suma
print("La suma de todos los elementos de la matriz es:", suma)
