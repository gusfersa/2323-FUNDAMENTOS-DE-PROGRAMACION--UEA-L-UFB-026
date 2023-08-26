#Acceso a elementos de un arreglo tridimensional

#Acceso a elementos de un arreglo tridimensional

#Si tenemos el siguiente arreglo tridimensional:
# arr = [[[10, 20], [30, 40]], [[50, 60], [70, 80]]].
# ¿Cómo accederíamos al valor 70?

# 2 x 2 x 2 = 8

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

print(arr)
arr[1][1][0] = 0
print(arr)