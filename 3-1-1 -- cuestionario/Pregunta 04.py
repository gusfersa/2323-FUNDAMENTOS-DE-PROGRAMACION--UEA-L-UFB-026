#Asignación de valores en un arreglo tridimensional

#Si tenemos el siguiente arreglo tridimensional: arr = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], ¿qué línea de código cambiaría el valor 11 por 20?

#a. arr[2][2][1] = 20;
#b. arr[1][1][2] = 20;
#c. arr[2][1][2] = 20;
#d. arr[1][1][1] = 20; (Correcta)

arr = \
    [
        [
            [1, 2, 3],
            [4, 5, 6]],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ]

print(arr)
arr[1][1][1] = 20
print(arr)