# Crear una matriz bidimensional (3x3) para el ejemplo.txt
matriz = [
    [4, 7, 2],
    [1, 9, 6],
    [8, 3, 5]
]

# Valor que estamos buscando
valor_buscado = 9

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")


# En este ejemplo.txt:
# - Creamos una matriz 3x3 para representar nuestros datos.
# - Especificamos el valor que estamos buscando (en este caso, 9).
# - Usamos dos bucles "for" anidados para recorrer la matriz y buscar el valor deseado.
# - Cuando encontramos el valor, guardamos la fila y columna en las variables fila_encontrada y columna_encontrada.
# - Detenemos la búsqueda una vez que se encuentra el valor usando las declaraciones break.
# - Al final, verificamos si se encontró el valor y mostramos su posición, o informamos si el valor no se encontró en la matriz.