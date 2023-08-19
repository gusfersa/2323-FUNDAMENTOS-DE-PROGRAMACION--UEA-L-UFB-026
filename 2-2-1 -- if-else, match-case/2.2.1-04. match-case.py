mes = int(input('Ingrese un número: '))
match mes:
    case 1:
        print(f'El mes {mes} es enero')
    case 2:
        print(f'El mes {mes} es febrero')
    case 3:
        print(f'El mes {mes} es marzo')
    case 4:
        print(f'El mes {mes} es abril')
    case 5:
        print(f'El mes {mes} es mayo')
    case 6:
        print(f'El mes {mes} es junio')
    case 7:
        print(f'El mes {mes} es julio')
    case 8:
        print(f'El mes {mes} es agosto')
    case 9:
        print(f'El mes {mes} es septiembre')
    case 10:
        print(f'El mes {mes} es octubre')
    case 11:
        print(f'El mes {mes} es noviembre')
    case 12:
        print(f'El mes {mes} es diciembre')
    case _:
        print(f'Número ingresado inválido')