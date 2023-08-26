#Asignación de valores en un arreglo multidimensional

#Si tenemos el siguiente arreglo bidimensional: arr = [[1, 2, 3], [4, 5, 6]], ¿qué línea de código cambiaría el valor 5 por 10?

#a. arr[2][1] = 10
#b. arr[1][5] = 10
#c. arr[1][2] = 10
#d. arr[1][1] = 10 (Correcta)

arr = \
    [
        [1, 2, 3],
        [4, 5, 6]
    ]

print(arr)
arr[1][1] = 10
print(arr)