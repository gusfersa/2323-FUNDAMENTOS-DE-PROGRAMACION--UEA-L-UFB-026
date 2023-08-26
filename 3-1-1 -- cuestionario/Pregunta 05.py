#Creación de arreglo multidimensional

#¿Cuál es la forma correcta de crear un arreglo bidimensional de tamaño 3x4 en Python, inicializado con ceros?

#a. arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#b. arr = [[0, 0], [0, 0], [0, 0]]
#c. arr = [[0 for _ in range(4)] for _ in range(3)] (Correcta)
#d. arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

arr = [[0 for _ in range(4)] for _ in range(3)]

print(arr)