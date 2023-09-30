# Crear una matriz bidimensional (3x3) para el ejemplo.txt
matriz = [
    [5, 2, 9],
    [3, 7, 1],
    [8, 4, 6]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)


# En este ejemplo.txt:
# Creamos una matriz 3x3 para representar nuestros datos.
# Implementamos la función bubble_sort_fila que utiliza el algoritmo del Método de la Burbuja para ordenar una fila de manera ascendente.
# Utilizamos un bucle para recorrer cada fila de la matriz y aplicar bubble_sort_fila para ordenar las filas individualmente.
# Mostramos la matriz original y luego la matriz ordenada por filas.
# El algoritmo Bubble Sort compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Repite este proceso hasta que la matriz esté completamente ordenada. Es importante recordar que este algoritmo puede no ser eficiente en arreglos grandes debido a su complejidad de tiempo cuadrática.