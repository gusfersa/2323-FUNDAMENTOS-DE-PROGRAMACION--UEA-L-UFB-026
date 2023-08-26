#Acceso a elementos de un arreglo multidimensional

#Supongamos que tenemos el siguiente arreglo bidimensional: arr = [[10, 20, 30], [40, 50, 60]]. ¿Cómo accederíamos al valor 50?

#a. arr[1][0]
#b. arr[0][1]
#c. arr[1][1] (Correcta)
#d. arr[2][1]

arr = \
    [
        [10, 20, 30],
        [40, 50, 60]
    ]

print(arr[1][1])