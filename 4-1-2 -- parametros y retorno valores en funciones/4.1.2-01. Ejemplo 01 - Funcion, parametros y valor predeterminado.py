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
