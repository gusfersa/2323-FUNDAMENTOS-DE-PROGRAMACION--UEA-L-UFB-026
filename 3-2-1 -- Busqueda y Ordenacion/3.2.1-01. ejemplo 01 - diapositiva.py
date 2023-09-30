# Crear una matriz bidimensional (2x2) para el ejemplo.txt
matriz = [
    [5, 2],
    [3, 1]
]

# Búsqueda de un valor específico en la matriz
valor_buscado = 3
if any(valor_buscado in fila for fila in matriz):
    print(f"Se encontró {valor_buscado} en la matriz.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")

# Ordenar las filas de la matriz por el valor máximo en cada fila
matriz.sort(key=lambda fila: max(fila))

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Valor Máximo en Cada Fila:")
for fila in matriz:
    print(fila)

