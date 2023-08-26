#Uso de arreglos multidimensionales

#Supongamos que tenemos el siguiente arreglo bidimensional: arr = [[1, 2], [3, 4]]. ¿Qué línea de código cambiaría el valor 4 por 10?

#a. arr[2][2] = 10;
#b. arr[1][1] = 10;
#c. arr[2][1] = 10;
#d. arr[1][1] = 10; (Correcto)

arr = \
    [
        [1, 2],
        [3, 4]
    ]

print(f'Arreglo inicial: {arr}')
arr[1][1] = 10
print(f'Arreglo modificado: {arr}')