num = int(input('Ingrese un número: '))
match num:
    case num if (num > 0):
        print(f'El número {num} es positivo')
    case num if (num == 0):
        print(f'El número {num} es cero')
    case _:
        print(f'El número {num} es negativo')

num = int(input('Ingrese un número: '))
if (num > 0):
    print(f'El número {num} es positivo')
elif (num == 0):
    print(f'El número {num} es cero')
else:
    print(f'El número {num} es negativo')