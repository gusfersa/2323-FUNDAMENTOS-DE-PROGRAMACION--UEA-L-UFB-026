# Ejemplo de Lectura de Archivos en Python usando read() y readline()

# Definimos el nombre del archivo
file_name = "ejemplo_lectura.txt"

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(file_name, "w")

# Escribimos algunas líneas en el archivo
archivo_escritura.write("Línea 1: Esto es una prueba.\n")
archivo_escritura.write("Línea 2: Aprendiendo lectura de archivos en Python.\n")

# Cerramos el archivo de escritura
archivo_escritura.close()

# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Método read(): lee todo el contenido del archivo
contenido_completo = archivo_lectura.read()
print("Contenido completo usando read():")
print(contenido_completo)

# Método readline(): lee una línea a la vez
archivo_lectura.seek(0)  # Reiniciamos el cursor al principio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()

print("\nContenido línea por línea usando readline():")
print(linea_1.strip())  # strip() elimina el salto de línea al final
print(linea_2.strip())

# Cerramos el archivo de lectura
archivo_lectura.close()
