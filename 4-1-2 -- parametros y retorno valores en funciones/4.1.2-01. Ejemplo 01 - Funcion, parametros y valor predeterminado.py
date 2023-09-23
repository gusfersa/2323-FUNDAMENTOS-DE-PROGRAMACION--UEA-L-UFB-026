# Definición de una función con parámetros
def saludar(nombre, edad):
    print(f"Hola, {nombre} tienes {edad} años.")

# Llamada a la función y paso de argumentos
saludar("Juan", 25)
saludar("María", 30)

# Parámetros predeterminados
def saludar_con_saludo(nombre, edad, saludo="Hola"):
    print(f"{saludo}, {nombre} tienes {edad} años.")

# Llamada a la función con parámetro predeterminado
saludar_con_saludo("Pedro", 28)
saludar_con_saludo("Ana", 22, "¡Hola!")


# Explicación:
#
# Hemos definido una función llamada saludar que toma dos parámetros: nombre y edad.
# Esta función simplemente imprime un saludo personalizado que incluye el nombre y la edad.
# Luego, llamamos a la función saludar dos veces, pasando diferentes argumentos en cada llamada.
#
# Después, hemos definido una segunda función llamada saludar_con_saludo que toma tres parámetros:
# nombre, edad y saludo.
# El tercer parámetro, saludo, tiene un valor predeterminado de "Hola".
# Cuando llamamos a la función saludar_con_saludo, podemos pasar solo dos argumentos si estamos
# satisfechos con el saludo predeterminado, o podemos proporcionar un tercer argumento para
# personalizar el saludo.
#
# Este ejemplo ilustra cómo definir funciones con parámetros, cómo pasar argumentos a esas
# funciones y cómo usar parámetros predeterminados para hacer que las funciones sean más flexibles.