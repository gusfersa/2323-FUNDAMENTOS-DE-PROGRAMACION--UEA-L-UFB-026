#Acceso a elementos de un arreglo tridimensional

#Si tenemos el siguiente arreglo tridimensional: arr = [[[10, 20], [30, 40]], [[50, 60], [70, 80]]]. ¿Cómo accederíamos al valor 70?

#a. arr[2][2][1]
#b. arr[1][2][2]
#c. arr[1][1][2]
#d. arr[1][1][0] (Correcta)

arr = \
    [
        [
            [10, 20],
            [30, 40]
        ],
        [
            [50, 60],
            [70, 80]
        ]
    ]

print(arr[1][1][0])