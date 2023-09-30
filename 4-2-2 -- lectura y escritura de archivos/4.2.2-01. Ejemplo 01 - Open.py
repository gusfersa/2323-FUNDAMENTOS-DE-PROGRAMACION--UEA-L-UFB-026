# Ejemplo de Apertura de Archivos en Python

# Definimos el nombre del archivo
file_name = "ejemplo.txt"

# Modo de apertura: "w" para escritura (write)
# Si el archivo no existe, se creará; si existe, se sobrescribirá
archivo = open(file_name, "w")

# Escribimos en el archivo
archivo.write("¡Hola, mundo!\n")
archivo.write("Este es un ejemplo.txt de apertura y escritura en Python.")

# Cerramos el archivo para liberar recursos
archivo.close()

# Modo de apertura: "r" para lectura (read)
# Abrimos el archivo que acabamos de crear
archivo = open(file_name, "r")

# Leemos el contenido e imprimimos en la consola
contenido = archivo.read()
print(contenido)

# Cerramos el archivo después de leer
archivo.close()
