# Definición de una función simple que saluda al usuario
def saludar(nombre):
    """
    Esta función toma un nombre como argumento
    y muestra un saludo personalizado.
    """
    mensaje = f"Hola, {nombre}! ¿Cómo estás?"
    return mensaje

# Llamada a la función
nombre_usuario = "Juan"
saludo = saludar(nombre_usuario)

# Mostrar el resultado
print(saludo)