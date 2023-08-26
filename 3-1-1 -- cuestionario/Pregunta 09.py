#Modificación de arreglos multidimensionales

#Si tenemos el siguiente arreglo tridimensional: arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]], ¿qué línea de código cambiaría el valor 6 por 15?

#a. arr[1][1][1] = 15;
#b. arr[1][2][1] = 15;
#c. arr[2][1][2] = 15;
#d. arr[1][0][1] = 15; (Correcto)

arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

arr = \
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]

print(f'Arreglo original: {arr}')
arr[1][0][1] = 15
print(f'Arreglo modificado: {arr}')